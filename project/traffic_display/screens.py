import lvgl as lv
from traffic_display.assets import APP_VERSION

# ----- HOME SCREEN -----

def home(controls, page):
    # Welcome text X/Y.
    controls.label(page, 'Welcome', 24, 72, 552, 'LV_FONT_MONTSERRAT_28')
    # Region text X/Y.
    controls.label(page, 'Karlskrona - Region Transport', 24, 106, 552, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted)
    # Welcome card
    c = controls.panel(page, 24, 130, 552, 290)
    # App wordmark
    controls.brand(c, 0, 64, 'LV_FONT_MONTSERRAT_28', True)
    # Swipe instruction
    controls.label(c, 'Swipe to get started', 0, 124, 552, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted, True)
    # Team member names
    controls.label(c, 'BY  Johan  Andrée  Liza  Ludwig  Angël', 0, 166, 552, 'SPECIAL_LETTER_MONTSERRAT_14', controls.secondary, True)
    # Welcome card divider
    controls.box(c, 0, 245, 552, 1, controls.border)
    # Left footer: Group 13
    controls.label(c, 'Group 13', 18, 261, 350, 'SPECIAL_LETTER_MONTSERRAT_14', controls.secondary)
    # Right footer: app version
    version = controls.label(c, 'v' + APP_VERSION, 450, 261, 84, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted)
    version.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)



# ----- DEPARTURES SCREEN -----

def departures(controls, page):
    # Departures title X/Y
    controls.label(page, 'Departures', 24, 72, 552, 'LV_FONT_MONTSERRAT_28')
    # Transport / stop X/Y
    controls.label(page, controls.names[controls.mode] + ' · ' + controls.stop, 24, 106, 552, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted)
    color = controls.accents[controls.mode]
    # Stop summary box
    chip = controls.panel(page, 366, 80, 210, 38)
    chip.set_style_border_color(lv.color_hex(color), 0)
    # Stop icon
    controls.icon(chip, 'pin', 12, 10, color)
    # Selected stop name
    controls.label(chip, controls.stop, 38, 11, 103, 'SPECIAL_LETTER_MONTSERRAT_14')
    # Transport badge
    pill = controls.box(chip, 149, 9, 49, 20, controls.blend(color, 24), 10)
    # Transport badge text
    mode_label = controls.label(pill, controls.names[controls.mode], 0, 0, font='SPECIAL_LETTER_MONTSERRAT_14', color=color)
    mode_label.update_layout()
    mode_label.center()
    # Departure table
    table = controls.panel(page, 24, 130, 552, 263)
    # Table heading background
    head = controls.box(table, 1, 1, 550, 32, controls.blend(color, 13))
    for text, x, w, center in [('TIME', 13, 54, False), ('TRAIN' if controls.mode == 1 else 'LINE', 67, 64, True), ('DESTINATION', 131, 350, False), ('TRACK' if controls.mode == 1 else '' if controls.mode == 2 else 'POS.', 482, 54, True)]:
        # Column heading text
        controls.label(head, text, x, 9, w, 'LV_FONT_MONTSERRAT_12', color, center)
    # Line under headings
    controls.box(table, 1, 33, 550, 1, controls.border)
    # Departure list area
    body = controls.box(table, 1, 34, 550, 228)
    # List scrolling
    controls.scroll(body)
    y = 0
    for d in controls.departures:
        kind = controls.kinds.index(d['kind'])
        delay = d.get('delayMins', 0)
        train = kind == 1
        h = 47 if delay else 42 if train else 40
        # One departure row
        r = controls.box(body, 0, y, 550, h)
        dc = controls.accents[kind]
        if delay:
            # Original delayed time
            old = controls.label(r, d['time'], 14, 9, 54, 'LV_FONT_MONTSERRAT_12', controls.muted)
            old.set_style_text_decor(lv.TEXT_DECOR.STRIKETHROUGH, 0)
            hh, mm = [int(v) for v in d['time'].split(':')]
            mins = (hh * 60 + mm + delay) % 1440
            # New delayed time
            controls.label(r, '%02d:%02d' % (mins // 60, mins % 60), 14, 24, 54, 'LV_FONT_MONTSERRAT_14', 16749824)
        else:
            # Normal departure time
            controls.label(r, d['time'], 14, (h - 18) // 2, 54, 'LV_FONT_MONTSERRAT_14')
        if train:
            # Train line / operator
            controls.label(r, d['line'], 68, 7, 64, 'SPECIAL_LETTER_MONTSERRAT_14', dc, True)
            # Train number
            controls.label(r, d.get('train_number', ''), 68, 25, 64, 'SPECIAL_LETTER_MONTSERRAT_14', controls.secondary, True)
        else:
            # Measure bus/ferry line
            measure = controls.label(r, d['line'], 0, 0, font='SPECIAL_LETTER_MONTSERRAT_14')
            measure.update_layout()
            w = min(64, max(24, measure.get_width() + 16))
            measure.delete()
            # Line badge rectangle
            badge = controls.box(r, 68 + (64 - w) // 2, (h - 20) // 2, w, 20, controls.blend(dc, 32), 6)
            # Line badge text
            line_label = controls.label(badge, d['line'], 0, 0, w-8, font='SPECIAL_LETTER_MONTSERRAT_14', color=dc, center=True)
            line_label.update_layout()
            line_label.center()
        # Departure destination
        controls.label(r, d['destination'], 132, (h - 17) // 2, 350, 'SPECIAL_LETTER_MONTSERRAT_14')
        # Platform / position
        controls.label(r, d.get('platform', ''), 482, (h - 16) // 2, 54, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted, True)
        # Line between departures
        controls.box(r, 0, h - 1, 550, 1, controls.border)
        y += h
    if not y:
        # No departures
        controls.label(body, 'No departures available', 14, 16, 520, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted)
    # Data status dot
    controls.box(page, 24, 406, 6, 6, 14688571, 3)
    # Data status text
    controls.label(page, controls.status, 36, 402, 540, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted)



# ----- SETTINGS SCREEN -----

def settings(controls, page):
    # Settings title X/Y
    controls.label(page, 'Settings', 24, 72, 552, 'LV_FONT_MONTSERRAT_28')
    # Preferences X/Y
    controls.label(page, 'Preferences for this session', 24, 106, 552, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted)
    # Reset button
    reset = controls.panel(page, 512, 78, 64, 30, radius=15)
    # Reset text
    controls.label(reset, 'Reset', 0, 8, 64, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted, True)
    # Reset tap action
    controls.click(reset, controls.reset)
    # Transport heading
    controls.section(page, 'TRANSPORT TYPE', 135)
    # Transport selector
    m = controls.panel(page, 24, 155, 552, 46)
    # Transport icon
    controls.icon(m, controls.kinds[controls.mode] + '_22', 13, 12, controls.accents[controls.mode])
    # Selected transport
    controls.label(m, controls.names[controls.mode], 44, 15, 470, 'SPECIAL_LETTER_MONTSERRAT_14')
    # Dropdown arrow
    controls.icon(m, 'down', 526, 17, controls.muted)
    # Open transport dropdown
    controls.click(m, lambda: controls.open_menu(1))
    # Stop heading
    controls.section(page, 'STOP', 214)
    # Stop dropdown box
    s = controls.panel(page, 24, 234, 552, 46)
    # Stop icon
    controls.icon(s, 'pin', 13, 14, controls.accents[controls.mode])
    # Selected stop
    controls.label(s, controls.stop, 40, 15, 472, 'SPECIAL_LETTER_MONTSERRAT_14')
    # Dropdown arrow
    controls.icon(s, 'down', 526, 17, controls.muted)
    # Open stop dropdown
    controls.click(s, lambda: controls.open_menu(2))
    # Terms heading
    controls.section(page, 'ABOUT', 293)
    # Terms link box
    c = controls.panel(page, 24, 313, 552, 48)
    # Terms link row
    r = controls.box(c, 1, 1, 550, 46)
    # Terms link text
    controls.label(r, 'Terms & Conditions', 14, 16, 480, 'SPECIAL_LETTER_MONTSERRAT_14')
    # Terms link arrow
    controls.icon(r, 'right', 530, 20, controls.muted)
    # Open Terms screen
    controls.click(r, lambda: controls.change('terms_open', True))


# ----- SETTINGS: TERMS & CONDITIONS -----
# Terms & Condition text 1 -> n.
TERMS = [
    ('1. ', ''),
    ('2. ', ''),
    ('3. ', ''),
    ('4. ', ''),
    ('5. ', ''),
    ('6. ', ''),
    ('7. ', ''),
]

def terms(controls, page):
    # Terms title X/Y
    controls.label(page, 'Terms & Conditions', 24, 72, 552, 'LV_FONT_MONTSERRAT_28')
    # Last updated X/Y
    controls.label(page, 'Last updated — 2026', 24, 106, 552, 'SPECIAL_LETTER_MONTSERRAT_14', controls.muted)
    # Scrollable terms area
    body = controls.box(page, 24, 130, 552, 302, controls.bg)
    # Terms scrolling
    controls.scroll(body)
    y = 0
    for title, text in TERMS:
        # Rectangle: one term
        c = controls.panel(body, 0, y, 552, 90)
        # Term heading
        controls.label(c, title, 12, 12, 528, 'LV_FONT_MONTSERRAT_12')
        # Term text; fit its box.
        h = 32 + controls.paragraph(c, text, 12, 32, 528, 'SPECIAL_LETTER_MONTSERRAT_14', controls.secondary) + 12
        c.set_height(h)
        y += h + 8

