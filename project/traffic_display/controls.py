import errno
import json

import lvgl as lv
from traffic_display import screens, api
from traffic_display.assets import ICONS, LABEL_DOTS, LABEL_WRAP, get_font
from traffic_display.assets import TRANSPORT_COLORS, TRANSPORT_KINDS, TRANSPORT_NAMES


SETTINGS_FILE: str = '/settings.json'
WIFI_DOT_X: int = 574
WIFI_LABEL_X: int = 410
WIFI_LABEL_MAX_WIDTH: int = 152
WIFI_LABEL_GAP: int = 12
WIFI_HEADER_RIGHT_MARGIN: int = 18
WIFI_NAME_MAX_LENGTH: int = 32


class Controls:
    names: tuple[str, ...] = TRANSPORT_NAMES
    kinds: tuple[str, ...] = TRANSPORT_KINDS
    accents: tuple[int, ...] = TRANSPORT_COLORS

    # --- DRAWING HELPERS ---
    def blend(self, color, alpha):
        """Mix an RGB color with the current card color using an opacity value."""
        # Blend each 8-bit channel independently; alpha=255 keeps the requested
        # color and alpha=0 returns the card background.
        return sum((((color >> s & 255) * alpha + (self.card >> s & 255) * (255 - alpha)) // 255 << s for s in (0, 8, 16)))


    def box(self, parent, x, y, w, h, color=None, radius=0, outline=False):
        """Create a non-scrollable LVGL container with shared app styling."""
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
        """Create a card-style box with the standard border."""
        # Border.
        return self.box(parent, x, y, w, h, radius=radius, outline=True)


    def label(self, p, value, x, y, w=0, font='SPECIAL_LETTER_MONTSERRAT_14', color=None, center=False):
        """Create a styled label, optionally constraining and centering its text."""
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
        """Create a recolored image widget from the preloaded icon collection."""
        # Icon
        o = lv.image(p)
        o.set_src(ICONS[key])
        o.set_pos(x, y)
        o.set_style_image_recolor(lv.color_hex(color), 0)
        o.set_style_image_recolor_opa(lv.OPA.COVER, 0)
        o.remove_flag(lv.obj.FLAG.CLICKABLE)
        return o


    def click(self, o, fn):
        """Make a widget clickable and invoke its callback on click events."""
        # The callback intentionally receives no event argument because app
        # actions use the same zero-argument interface throughout the UI.
        o.add_flag(lv.obj.FLAG.CLICKABLE)
        o.add_event_cb(lambda _event: fn(), lv.EVENT.CLICKED, None)


    def scroll(self, o):
        """Enable vertical scrolling and automatic scrollbar visibility."""
        o.add_flag(lv.obj.FLAG.CLICKABLE)
        o.add_flag(lv.obj.FLAG.SCROLLABLE)
        # Scroll vertically.
        o.set_scroll_dir(lv.DIR.VER)
        o.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


    def brand(self, p, x, y, font, center=False):
        """Render the two-color Traffic Display wordmark as adjacent labels."""
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
        """Draw a muted, letter-spaced settings section heading."""
        # Section heading text
        o = self.label(p, text, x, y, 552, 'SPECIAL_LETTER_MONTSERRAT_14', self.muted)
        o.set_style_text_letter_space(1, 0)


    def paragraph(self, p, text, x, y, w, font, color):
        """Add a wrapped paragraph and return its computed rendered height."""
        # Wrapping paragraph text
        o = self.label(p, text, x, y, w, font, color)
        o.set_long_mode(LABEL_WRAP)
        o.set_style_text_line_space(5, 0)
        o.update_layout()
        return o.get_height()


    # === HEADER ===
    def header(self, p, back=False):
        """Draw the shared header, including navigation and live Wi-Fi status."""
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
        # Wi-Fi status indicator
        self.wifi_dot = self.box(h, WIFI_DOT_X, 27, 8, 8, radius=4)
        self.wifi_label = self.label(
            h, '', WIFI_LABEL_X, 22, WIFI_LABEL_MAX_WIDTH,
            'SPECIAL_LETTER_MONTSERRAT_14')
        self.wifi_label.set_width(min(
            WIFI_LABEL_MAX_WIDTH,
            max(0, WIFI_DOT_X - WIFI_LABEL_X - WIFI_LABEL_GAP)))
        self.wifi_label.set_long_mode(LABEL_DOTS)
        self.wifi_label.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)
        # Keep the status dot against the right margin while the name uses the
        # available space to its left, preventing overlap on narrower displays.
        self.wifi_dot.set_pos(
            min(WIFI_DOT_X, h.get_width() - 8 - WIFI_HEADER_RIGHT_MARGIN), 27)
        self.update_wifi_status()
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
        """Set the active dropdown type and schedule the UI to redraw."""
        self.menu = menu
        self.request()


    def close_menu(self, event):
        """Close the dropdown only when the user clicks its transparent overlay."""
        if event.get_target() == self.overlay:
            self.menu = 0
            self.request()


    def draw_menu(self):
        """Draw a scrollable modal menu for transport or stop selection."""
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
        # Bind each option's value at creation time so later loop iterations do
        # not change the selection captured by its click callback.
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


    def tile_changed(self, _event):
        """Update the selected page index and its indicator after a swipe."""
        tile = self.tileview.get_tile_active()
        page = tile.get_index()
        if page < len(self.page_tiles) and page != self.page:
            self.page: int = page
            self.update_dots()


    def update_dots(self):
        """Resize and position the page indicators to highlight the active page."""
        x = 273
        for i, o in enumerate(self.dots):
            w = 18 if i == self.page else 7
            o.set_pos(x, 430)
            o.set_size(w, 6)
            o.set_style_bg_color(lv.color_hex(self.secondary if i == self.page else self.border), 0)
            x += w + 9


    # Screen switch
    def __init__(self, display, touch, handler, wifi_station=None,
                 wifi_name: str = ''):
        """Initialize screen state, restore preferences, load data, and draw UI."""
        self.display, self.touch, self.handler = (display, touch, handler)
        self.wifi_station, self.wifi_name = (wifi_station, wifi_name)
        self.wifi_connected = None
        self.page, self.dark = (0, True)
        self.default_mode, self.default_stop_id = (0, None)
        self.settings_message: str = ''
        self.settings_message_color: int = 0
        # Restore saved selections before fetching matching data; load_data
        # repairs a missing or incompatible stop ID.
        self.load_settings()
        self.mode, self.stop_id = (self.default_mode, self.default_stop_id)
        self.load_data()
        self.default_stop_id: "str | None" = self.stop_id
        # menu: 0 = closed, 1 = transport dropdown, 2 = stop dropdown.
        self.terms_open, self.menu = (False, 0)
        # Top-level screen
        self.screen = lv.obj()
        self.screen.remove_style_all()
        self.screen.remove_flag(lv.obj.FLAG.SCROLLABLE)
        lv.screen_load(self.screen)
        self.timer = lv.timer_create(self.redraw, 1, None)
        self.timer.pause()
        self.draw()
        self.wifi_timer = lv.timer_create(self.update_wifi_status, 1000, None)


    def request(self):
        """Schedule one redraw at the next safe LVGL timer opportunity."""
        # Defer widget changes until the current LVGL event is finished.
        self.timer.resume()
        self.timer.ready()


    def redraw(self, timer):
        """Pause the one-shot redraw timer and rebuild the current screen."""
        # Redraw only after a prototype interaction.
        timer.pause()
        self.draw()

    def update_wifi_status(self, _timer=None):
        """Refresh the header's connection dot and SSID/no-network label."""
        connected = self.wifi_is_connected()
        connection_changed = (
            self.wifi_connected is not None and
            connected != self.wifi_connected)
        self.wifi_connected = connected
        if connected:
            color = 0x00C853
            text = self.wifi_name[:WIFI_NAME_MAX_LENGTH]
            text_color = self.text
        else:
            color = 0xF44336
            text = 'No Wi-Fi'
            text_color = self.muted
        self.wifi_dot.set_style_bg_color(lv.color_hex(color), 0)
        self.wifi_label.set_text(text)
        self.wifi_label.set_style_text_color(lv.color_hex(text_color), 0)
        if connection_changed:
            self.load_data()
            self.request()

    def wifi_is_connected(self):
        """Return the station's connection state, treating driver errors as offline."""
        try:
            return (self.wifi_station is not None and
                    self.wifi_station.isconnected())
        except OSError:
            return False


    # --- DATA DISPLAY INTERFACE ---
    def load_data(self):
        """Load stops and normalized departures for the current transport/stop."""
        kind = self.kinds[self.mode]
        self.stops: list[dict[str, str]] = api.get_stops(kind)
        ids = [stop['id'] for stop in self.stops]
        # If a saved stop does not belong to this transport, select its first
        # available stop; an empty stop list is represented by None.
        if self.stop_id not in ids:
            self.stop_id: "str | None" = ids[0] if ids else None
        self.stop: str = next((stop['name'] for stop in self.stops
                               if stop['id'] == self.stop_id), 'Select stop')
        self.status: str = api.STATUS
        self.departures: list = []
        if not ids or self.stop_id is None:
            return
        if not self.wifi_is_connected():
            self.status = 'No Wi-Fi connection'
            return
        try:
            self.departures = api.get_departures(kind, self.stop_id)
        except OSError:
            self.status = 'No network connection'


    def change(self, key, value):
        """Update one UI state value, refreshing data when selection changes."""
        # Only transport/stop selections request a new data snapshot.
        setattr(self, key, value)
        if key in ('mode', 'stop_id'):
            self.settings_message = ''
            self.load_data()
        self.menu = 0
        self.request()

    def load_settings(self):
        """Load persisted transport and stop preferences if present."""
        try:
            with open(SETTINGS_FILE, 'r') as source:
                saved = json.load(source)
        except OSError as error:
            if error.args and error.args[0] == errno.ENOENT:
                return
            raise
        self.default_mode = saved.get('mode', self.default_mode)
        self.default_stop_id = saved.get('stop_id', self.default_stop_id)

    def save_settings(self):
        """Persist current selections and expose success or failure in the UI."""
        saved = {'mode': self.mode, 'stop_id': self.stop_id}
        serialized = json.dumps(saved)
        try:
            with open(SETTINGS_FILE, 'w') as destination:
                destination.write(serialized)
        except OSError as error:
            self.settings_message = 'Could not save settings: %s' % error
            self.settings_message_color = 16749824
        else:
            self.default_mode, self.default_stop_id = (
                self.mode, self.stop_id)
            self.settings_message = 'Settings saved'
            self.settings_message_color = 0x00C9A7
        self.request()

    def reset(self):
        """Restore the last saved selections and reload their matching data."""
        self.mode: int = self.default_mode
        self.change('stop_id', self.default_stop_id)


    def draw(self):
        """Rebuild the current page, shared header, navigation, and any menu."""
        # Rebuild the three pages using the current state and theme.
        self.bg, self.card, self.border, self.text, self.secondary, self.muted = (789516, 1579035, 2565930, 16777215, 10461097, 5395036) if self.dark else (15921911, 16777215, 15000807, 789516, 5395036, 10592682)
        self.screen.clean()
        self.screen.set_style_bg_color(lv.color_hex(self.bg), 0)
        self.screen.set_style_bg_opa(lv.OPA.COVER, 0)
        # Whole-screen background
        self.root = self.box(self.screen, 0, 0, 600, 450, self.bg, 0)
        self.root.set_style_clip_corner(False, 0)
        if self.terms_open:
            # Terms screen content
            screens.terms(self, self.root)
            # Header with Back button
            self.header(self.root, True)
        else:
            # Native LVGL horizontal tile navigation.
            self.tileview = lv.tileview(self.root)
            self.tileview.remove_style_all()
            self.tileview.set_pos(0, 0)
            self.tileview.set_size(600, 450)
            self.tileview.set_style_bg_color(lv.color_hex(self.bg), 0)
            self.tileview.set_style_bg_opa(lv.OPA.COVER, 0)
            self.tileview.set_style_pad_all(0, 0)
            self.tileview.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
            directions = (lv.DIR.RIGHT, lv.DIR.LEFT | lv.DIR.RIGHT, lv.DIR.LEFT)
            self.page_tiles = [
                self.tileview.add_tile(index, 0, directions[index])
                for index in range(3)
            ]
            for tile in self.page_tiles:
                tile.set_style_bg_color(lv.color_hex(self.bg), 0)
                tile.set_style_bg_opa(lv.OPA.COVER, 0)
                tile.set_style_pad_all(0, 0)
            for tile, show_screen in zip(
                    self.page_tiles,
                    (screens.home, screens.departures, screens.settings)):
                show_screen(self, tile)
            self.tileview.set_tile_by_index(self.page, 0, 0)
            self.tileview.add_event_cb(
                self.tile_changed, lv.EVENT.VALUE_CHANGED, None)
            # Main header and theme switch
            self.header(self.root)
            # Bottom page indicators
            self.dots = [self.box(self.root, 0, 430, 7, 6, self.border, 3) for _ in range(3)]
            self.update_dots()
            if self.menu:
                # Open dropdown overlay
                self.draw_menu()
