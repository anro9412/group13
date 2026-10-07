# DISPLAY RESOURCES
import gc
import os
import lvgl as lv
from debug_log import log


# ----- APP SETTINGS -----
# Version, dropdown choices and colours.

APP_VERSION = '1.1.0'
TRANSPORT_NAMES = ('Bus', 'Train', 'Ferry', 'All')
TRANSPORT_KINDS = ('bus', 'train', 'ferry', 'all')
TRANSPORT_COLORS = (0xE0213B, 0x00C9A7, 0x4DA6FF, 0xA855F7)

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
ICON_INDEX = {'bus_20': (20, 20, 0, 271), 'train_20': (20, 20, 271, 246), 'ferry_20': (20, 20, 517, 262), 'all_20': (20, 20, 779, 217), 'bus_22': (22, 22, 996, 279), 'train_22': (22, 22, 1275, 253), 'ferry_22': (22, 22, 1528, 287), 'all_22': (22, 22, 1815, 257), 'pin': (18, 18, 2072, 218), 'logo_28': (28, 28, 2290, 502), 'down': (13, 13, 2792, 84), 'back': (15, 15, 2876, 109), 'right': (10, 10, 2985, 80), 'sun': (14, 14, 3065, 164), 'moon': (13, 13, 3229, 125)}


def asset_path(name):
    location = globals().get('__file__', '')
    directory = location.rsplit('/', 1)[0] if '/' in location else 'traffic_display'
    if not directory.startswith('/'):
        directory = os.getcwd().rstrip('/') + '/' + directory
    path = directory + '/' + name
    os.stat(path)
    return path


def unpack_icon(encoded, size):
    result = bytearray(size)
    i = pos = 0
    while i < len(encoded):
        control = encoded[i]
        i += 1
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


def load_icons():
    if ICONS:
        return
    with open(asset_path('icons.bin'), 'rb') as source:
        for key, (w, h, offset, length) in ICON_INDEX.items():
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


def load_fonts():
    global FONT_FS
    if 'SPECIAL_LETTER_MONTSERRAT_14' in FONTS:
        return
    import fs_driver
    FONT_FS = lv.fs_drv_t()
    fs_driver.fs_register(FONT_FS, 'S')
    font = lv.binfont_create('S:' + asset_path('special_letter_montserrat.bin'))
    if not font:
        raise RuntimeError('Could not load special_letter_montserrat.bin')
    FONTS['SPECIAL_LETTER_MONTSERRAT_14'] = font
    gc.collect()
    log('Unicode fonts ready')


def get_font(name):
    return FONTS[name]
