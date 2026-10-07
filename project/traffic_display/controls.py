import lvgl as lv
from traffic_display import screens, api
from traffic_display.assets import ICONS, LABEL_DOTS, LABEL_WRAP, get_font
from traffic_display.assets import TRANSPORT_COLORS, TRANSPORT_KINDS, TRANSPORT_NAMES


class Controls:
    names = TRANSPORT_NAMES
    kinds = TRANSPORT_KINDS
    accents = TRANSPORT_COLORS

    # --- DRAWING HELPERS ---
    def blend(self, color, alpha):
        return sum((((color >> s & 255) * alpha + (self.card >> s & 255) * (255 - alpha)) // 255 << s for s in (0, 8, 16)))


    def box(self, parent, x, y, w, h, color=None, radius=0, outline=False):
        # Rectangle
        o = lv.obj(parent)
        o.remove_style_all()
        o.set_pos(x, y)
        o.set_size(w, h)
        o.set_style_bg_color(lv.color_hex(self.card if color is None else color), 0)
        o.set_style_bg_opa(lv.OPA.COVER, 0)
        o.set_style_radius(radius, 0)
        # Keep child backgrounds inside the rounded corners.
        o.set_style_clip_corner(radius > 0, 0)
        o.set_style_pad_all(0, 0)
        o.remove_flag(lv.obj.FLAG.SCROLLABLE)
        o.remove_flag(lv.obj.FLAG.CLICKABLE)
        o.add_flag(lv.obj.FLAG.EVENT_BUBBLE)
        if outline:
            o.set_style_border_width(1, 0)
            o.set_style_border_side(lv.BORDER_SIDE.FULL, 0)
            # Draw the border after children so it stays visible.
            o.set_style_border_post(True, 0)
            o.set_style_border_color(lv.color_hex(self.border), 0)
        return o


    def panel(self, parent, x, y, w, h, radius=10):
        # Border.
        return self.box(parent, x, y, w, h, radius=radius, outline=True)


    def label(self, p, value, x, y, w=0, font='SPECIAL_LETTER_MONTSERRAT_14', color=None, center=False):
        # Text label
        o = lv.label(p)
        o.remove_style_all()
        o.set_text(value)
        o.set_pos(x, y)
        if w:
            o.set_width(w)
            o.set_long_mode(LABEL_DOTS)
        # Text font.
        o.set_style_text_font(get_font(font), 0)
        o.set_style_text_color(lv.color_hex(self.text if color is None else color), 0)
        if center:
            o.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        o.remove_flag(lv.obj.FLAG.CLICKABLE)
        o.add_flag(lv.obj.FLAG.EVENT_BUBBLE)
        return o


    def icon(self, p, key, x, y, color):
        # Icon
        o = lv.image(p)
        o.set_src(ICONS[key])
        o.set_pos(x, y)
        o.set_style_image_recolor(lv.color_hex(color), 0)
        o.set_style_image_recolor_opa(lv.OPA.COVER, 0)
        o.remove_flag(lv.obj.FLAG.CLICKABLE)
        return o


    def click(self, o, fn):
        o.add_flag(lv.obj.FLAG.CLICKABLE)
        # Attach tap callback.
        o.add_event_cb(lambda e: fn() if abs(self.delta) < 10 else None, lv.EVENT.CLICKED, None)


    def scroll(self, o):
        o.add_flag(lv.obj.FLAG.CLICKABLE)
        o.add_flag(lv.obj.FLAG.SCROLLABLE)
        # Scroll vertically.
        o.set_scroll_dir(lv.DIR.VER)
        o.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


    def brand(self, p, x, y, font, center=False):
        # Traffic text
        a = self.label(p, 'Traffic', x, y, font=font)
        # Display text
        b = self.label(p, 'Display', 0, y, font=font, color=14688571)
        if center:
            a.set_style_text_letter_space(-1, 0)
            b.set_style_text_letter_space(-1, 0)
        a.update_layout()
        b.update_layout()
        if center:
            x = (p.get_width() - a.get_width() - b.get_width()) // 2
        a.set_x(x)
        b.set_x(x + a.get_width())


    def section(self, p, text, y, x=24):
        # Section heading text
        o = self.label(p, text, x, y, 552, 'SPECIAL_LETTER_MONTSERRAT_14', self.muted)
        o.set_style_text_letter_space(1, 0)


    def paragraph(self, p, text, x, y, w, font, color):
        # Wrapping paragraph text
        o = self.label(p, text, x, y, w, font, color)
        o.set_long_mode(LABEL_WRAP)
        o.set_style_text_line_space(5, 0)
        o.update_layout()
        return o.get_height()


    # === HEADER ===
    def header(self, p, back=False):
        # Header box
        h = self.box(p, 0, 0, 600, 62, self.bg)
        if back:
            # Back button box
            b = self.panel(h, 24, 13, 96, 36, radius=18)
            # Back arrow icon
            self.icon(b, 'back', 13, 10, self.secondary)
            # Back button text
            self.label(b, 'Back', 36, 9, 48, 'SPECIAL_LETTER_MONTSERRAT_14', self.secondary)
            # Back tap action
            self.click(b, lambda: self.change('terms_open', False))
        else:
            # Logo icon
            self.icon(h, 'logo_28', 24, 17, self.text)
            # App wordmark
            self.brand(h, 62, 18, 'LV_FONT_MONTSERRAT_20')
        # Theme switch box
        #t = self.box(h, 522, 16, 54, 30, self.border if self.dark else 13160672, 15)
        # Sun / moon icon
        #self.icon(t, 'moon' if self.dark else 'sun', 6 if self.dark else 34, 8, self.text)
        # Switch knob
        #self.box(t, 28 if self.dark else 4, 4, 22, 22, 4144966 if self.dark else 16777215, 11)
        # Toggle light / dark
        #self.click(t, lambda: self.change('dark', not self.dark))
        # Line below header
        #self.box(h, 0, 61, 600, 1, self.border)


    # --- DROPDOWNS ---
    def open_menu(self, menu):
        self.menu = menu
        self.request()


    def close_menu(self, event):
        if event.get_target() == self.overlay:
            self.menu = 0
            self.request()


    def draw_menu(self):
        # Dropdown overlay
        self.overlay = self.box(self.root, 0, 62, 600, 388, self.bg)
        self.overlay.add_flag(lv.obj.FLAG.CLICKABLE)
        self.overlay.set_style_bg_opa(lv.OPA.TRANSP, 0)
        self.overlay.add_event_cb(self.close_menu, lv.EVENT.CLICKED, None)
        # Dropdown box
        panel = self.panel(self.overlay, 24, 143, 552, 232)
        # Dropdown title
        self.label(panel, 'Transport type' if self.menu == 1 else 'Select stop',
                   13, 10, 485, 'SPECIAL_LETTER_MONTSERRAT_14')
        # Close button
        close = self.box(panel, 510, 1, 40, 34)
        # Close symbol
        self.label(close, 'x', 0, 6, 40, 'SPECIAL_LETTER_MONTSERRAT_14', self.muted, True)
        # Close dropdown action
        self.click(close, lambda: self.change('menu', 0))
        # Line below menu title
        self.box(panel, 1, 35, 550, 1, self.border)
        # Options area
        body = self.box(panel, 1, 36, 550, 194)
        # Menu scrolling
        self.scroll(body)
        options = list(enumerate(self.names)) if self.menu == 1 else [(stop['id'], stop['name']) for stop in self.stops]
        selected = self.mode if self.menu == 1 else self.stop_id
        for index, (value, name) in enumerate(options):
            # Dropdown option
            row = self.box(body, 0, index * 43, 550, 43)
            color = self.accents[self.mode] if value == selected else self.text
            icon = self.kinds[value] + '_20' if self.menu == 1 else 'pin'
            # Option transport / pin icon
            self.icon(row, icon, 13, 12, color)
            # Option name
            self.label(row, name, 42, 14, 490, 'SPECIAL_LETTER_MONTSERRAT_14', color)
            field = 'mode' if self.menu == 1 else 'stop_id'
            # Select option action
            self.click(row, lambda field=field, value=value: self.change(field, value))
            # Line between options
            self.box(row, 0, 42, 550, 1, self.border)
        if not options:
            # No stops
            self.label(body, 'No prototype stops available.', 13, 14, 524,
                       'SPECIAL_LETTER_MONTSERRAT_14', self.muted)


    # --- SWIPE PREVIEW ---
    def pointer(self, e):
        if self.terms_open or self.menu:
            return
        indev = lv.indev_active()
        if not indev:
            return
        p = lv.point_t()
        indev.get_point(p)
        code = e.get_code()
        if code == lv.EVENT.PRESSED:
            self.start = (p.x, p.y)
            self.lock = 0
            self.delta = 0
        elif code == lv.EVENT.PRESSING and self.start:
            dx, dy = (p.x - self.start[0], p.y - self.start[1])
            if not self.lock and max(abs(dx), abs(dy)) > 6:
                self.lock = 1 if abs(dx) >= abs(dy) else 2
            if self.lock == 1:
                self.delta = dx
                self.pages.set_x(max(-1200, min(0, -600 * self.page + dx)))
        elif code in (lv.EVENT.RELEASED, lv.EVENT.PRESS_LOST) and self.start:
            if self.lock == 1:
                dx = p.x - self.start[0]
                if dx < -150:
                    self.page = min(2, self.page + 1)
                elif dx > 150:
                    self.page = max(0, self.page - 1)
            self.start = None
            self.pages.set_x(-600 * self.page)
            self.update_dots()


    def update_dots(self):
        x = 273
        for i, o in enumerate(self.dots):
            w = 18 if i == self.page else 7
            o.set_pos(x, 430)
            o.set_size(w, 6)
            o.set_style_bg_color(lv.color_hex(self.secondary if i == self.page else self.border), 0)
            x += w + 9


    # Screen switch
    def __init__(self, display, touch, handler):
        self.display, self.touch, self.handler = (display, touch, handler)
        self.page, self.mode, self.dark = (0, 0, True)
        self.stop_id = None
        self.load_data()
        # menu: 0 = closed, 1 = transport dropdown, 2 = stop dropdown.
        self.terms_open, self.menu = (False, 0)
        self.start = None
        # Top-level screen
        self.screen = lv.obj()
        self.screen.remove_style_all()
        self.screen.remove_flag(lv.obj.FLAG.SCROLLABLE)
        lv.screen_load(self.screen)
        self.timer = lv.timer_create(self.redraw, 1, None)
        self.timer.pause()
        self.draw()


    def request(self):
        # Defer widget changes until the current LVGL event is finished.
        self.timer.resume()
        self.timer.ready()


    def redraw(self, timer):
        # Redraw only after a prototype interaction.
        timer.pause()
        self.draw()


    # --- DATA DISPLAY INTERFACE ---
    def load_data(self):
        kind = self.kinds[self.mode]
        self.stops = api.get_stops(kind)
        ids = [stop['id'] for stop in self.stops]
        if self.stop_id not in ids:
            self.stop_id = ids[0] if ids else None
        self.stop = next((stop['name'] for stop in self.stops
                          if stop['id'] == self.stop_id), 'Select stop')
        self.departures = api.get_departures(kind, self.stop_id) if ids else []
        self.status = api.STATUS


    def change(self, key, value):
        # Only transport/stop selections request a new data snapshot.
        setattr(self, key, value)
        if key in ('mode', 'stop_id'):
            self.load_data()
        self.menu = 0
        self.request()


    def reset(self):
        self.mode = 0
        self.change('stop_id', None)


    def draw(self):
        # Rebuild the three pages using the current state and theme.
        self.delta = 0
        self.start = None
        self.bg, self.card, self.border, self.text, self.secondary, self.muted = (789516, 1579035, 2565930, 16777215, 10461097, 5395036) if self.dark else (15921911, 16777215, 15000807, 789516, 5395036, 10592682)
        self.screen.clean()
        self.screen.set_style_bg_color(lv.color_hex(self.bg), 0)
        self.screen.set_style_bg_opa(lv.OPA.COVER, 0)
        # Whole-screen background
        self.root = self.box(self.screen, 0, 0, 600, 450, self.bg, 0)
        self.root.add_flag(lv.obj.FLAG.CLICKABLE)
        self.root.set_style_clip_corner(False, 0)
        self.root.add_event_cb(self.pointer, lv.EVENT.ALL, None)
        if self.terms_open:
            # Terms screen content
            screens.terms(self, self.root)
            # Header with Back button
            self.header(self.root, True)
        else:
            # Horizontal page container
            self.pages = self.box(self.root, -600 * self.page, 0, 1800, 450, self.bg)
            for i, show_screen in enumerate((screens.home, screens.departures, screens.settings)):
                # Welcome / Departures / Settings page
                p = self.box(self.pages, 600 * i, 0, 600, 450, self.bg)
                p.add_flag(lv.obj.FLAG.CLICKABLE)
                show_screen(self, p)
            # Main header and theme switch
            self.header(self.root)
            # Bottom page indicators
            self.dots = [self.box(self.root, 0, 430, 7, 6, self.border, 3) for i in range(3)]
            self.update_dots()
            if self.menu:
                # Open dropdown overlay
                self.draw_menu()


