# DISPLAY RESOURCES
import gc
import os

import lvgl as lv
from debug_log import log


# ----- APP SETTINGS -----
# Version, dropdown choices and colours.

APP_VERSION: str = '1.1.0'
TRANSPORT_NAMES: tuple[str, ...] = ('Bus', 'Train', 'Ferry', 'All')
TRANSPORT_KINDS: tuple[str, ...] = ('bus', 'train', 'ferry', 'all')
TRANSPORT_COLORS: tuple[int, ...] = (0xE0213B, 0x00C9A7, 0x4DA6FF, 0xA855F7)

ICONS, BUFFERS, FONTS = {}, {}, {}
FONT_FS = None

# Font and pixel size
for size in (12, 14, 16, 20, 28):
    FONTS['LV_FONT_MONTSERRAT_%d' % size] = getattr(lv, 'font_montserrat_%d' % size)
modes = getattr(lv.label, 'LONG_MODE', None)
if modes is None:
    modes = getattr(lv.label, 'LONG', None)
LABEL_WRAP = getattr(modes, 'WRAP', 0)
LABEL_DOTS = getattr(modes, 'DOTS', None)
if LABEL_DOTS is None:
    LABEL_DOTS = getattr(modes, 'DOT', 1)

# width, height, file offset, compressed byte length.
ICON_INDEX: dict[str, tuple[int, int, int, int]] = {'bus_20': (20, 20, 0, 271), 'train_20': (20, 20, 271, 246), 'ferry_20': (20, 20, 517, 262), 'all_20': (20, 20, 779, 217), 'bus_22': (22, 22, 996, 279), 'train_22': (22, 22, 1275, 253), 'ferry_22': (22, 22, 1528, 287), 'all_22': (22, 22, 1815, 257), 'pin': (18, 18, 2072, 218), 'logo_28': (28, 28, 2290, 502), 'down': (13, 13, 2792, 84), 'back': (15, 15, 2876, 109), 'right': (10, 10, 2985, 80), 'sun': (14, 14, 3065, 164), 'moon': (13, 13, 3229, 125)}


def asset_path(name: str) -> str:
    """Resolve an asset beside this module, including relative MicroPython paths."""
    location = globals().get('__file__', '')
    directory = location.rsplit('/', 1)[0] if '/' in location else 'traffic_display'
    # Some embedded builds expose a relative module path; anchor it to the
    # current filesystem directory before opening the resource.
    if not directory.startswith('/'):
        directory = os.getcwd().rstrip('/') + '/' + directory
    path = directory + '/' + name
    os.stat(path)
    return path


def unpack_icon(encoded, size):
    """Expand the icon's byte run-length encoding into an alpha map."""
    result = bytearray(size)
    i = pos = 0
    while i < len(encoded):
        control = encoded[i]
        i += 1
        # Controls below 128 introduce literal bytes; higher controls encode a
        # run of transparent (zero-valued) pixels.
        count = control+1 if control < 128 else control-127
        if pos+count > size:
            raise ValueError('Invalid icon length')
        if control < 128:
            if i+count > len(encoded):
                raise ValueError('Truncated icon')
            result[pos:pos+count] = encoded[i:i+count]
            i += count
        pos += count
    if pos != size:
        raise ValueError('Incomplete icon')
    return result


def load_icons() -> None:
    """Load indexed icon data once and create LVGL ARGB8888 descriptors."""
    if ICONS:
        return
    with open(asset_path('icons.bin'), 'rb') as source:
        for key, (w, h, offset, length) in ICON_INDEX.items():
            # Each index entry points at a compressed alpha-only image in the
            # shared binary. Expand it, then make its visible pixels white so
            # LVGL can recolor them at draw time.
            source.seek(offset)
            encoded = source.read(length)
            if len(encoded) != length:
                raise ValueError('Incomplete icons.bin')
            alpha = unpack_icon(encoded, w*h)
            data = bytearray(w*h*4)
            for pixel, opacity in enumerate(alpha):
                if opacity:
                    pos = pixel*4
                    data[pos] = data[pos+1] = data[pos+2] = 255
                    data[pos+3] = opacity
            BUFFERS[key] = data
            ICONS[key] = lv.image_dsc_t({
                'header': {'magic': 0x19, 'cf': lv.COLOR_FORMAT.ARGB8888,
                           'w': w, 'h': h, 'stride': w*4},
                'data_size': len(data), 'data': data})
    gc.collect()


def load_fonts() -> None:
    """Register the asset filesystem and load the custom Unicode font once."""
    global FONT_FS
    if 'SPECIAL_LETTER_MONTSERRAT_14' in FONTS:
        return
    import fs_driver
    # LVGL's binary font loader reads through a registered filesystem driver;
    # retain that driver object for as long as the loaded font may use it.
    FONT_FS = lv.fs_drv_t()
    fs_driver.fs_register(FONT_FS, 'S')
    font = lv.binfont_create('S:' + asset_path('special_letter_montserrat.bin'))
    if not font:
        raise RuntimeError('Could not load special_letter_montserrat.bin')
    FONTS['SPECIAL_LETTER_MONTSERRAT_14'] = font
    gc.collect()
    log('Unicode fonts ready')


def get_font(name):
    """Return a previously registered LVGL font by its application key."""
    return FONTS[name]
