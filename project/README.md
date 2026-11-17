# TrafficDisplay - MicroPython

An LVGL user interface designed in [LCD Wizard](https://lcdwizard.com/) for **Custom / breadboard wiring**, exported
as MicroPython for [lvgl_micropython](https://github.com/lvgl-micropython/lvgl_micropython)
(LVGL 9.4.0).

- Panel: RM690B0 600x450, rotation 0 degrees
- Touch: CST226SE
- Screens: TrafficLabDisplay

## 1. Firmware, with this UI frozen into it

lvgl_micropython compiles the display and touch drivers into the firmware, so it is
built for this board - and the same build can take the UI's Python with it.
`manifest.py` freezes every module here except `main.py`, so they run from flash
and the board needs no RAM to compile them. Importing the largest of them as a .py
instead needs about 103 KB free while it compiles.

It needs Linux or macOS (on Windows, WSL) with the ESP-IDF prerequisites in
lvgl_micropython's README.

```bash
git clone https://github.com/lvgl-micropython/lvgl_micropython
cd lvgl_micropython
git checkout d2d26467    # the version this export was written against
python3 make.py esp32 BOARD=ESP32_GENERIC_S3 BOARD_VARIANT=SPIRAM_OCT --flash-size=16 FROZEN_MANIFEST=/path/to/TrafficDisplay_micropython/manifest.py deploy
```

`FROZEN_MANIFEST` wants the full path to `manifest.py` in this folder. `deploy` flashes
the board once the build finishes (add `PORT=/dev/ttyUSB0` if it is not found). `--flash-size` and the PSRAM variant are for an N16R8 module, as set on the Hardware tab.
Change the design and you build again.

The frozen UI is part of the firmware image, and make.py sizes the app partition to
fit it - the partition layout on the Hardware tab is for the Arduino export. The
filesystem the next step copies to gets what is left of the flash, so a large design
on a 4 MB module leaves less room there (`mpremote df` shows it).

The CST226SE is read by a small driver written into `board.py`, so no
`INDEV=` is needed.

## 2. Copy what is not frozen

With [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html):

```bash
pip install mpremote
mpremote cp main.py :
mpremote cp output_smallpngtools.bin :
mpremote cp -r fonts :
mpremote reset
```

A `.py` copied to the board replaces the frozen module of the same name, so
`ui_events.py` (or anything else) can be changed without a rebuild.

**Without freezing** - a board with PSRAM and a small design - build the firmware
without `FROZEN_MANIFEST` and copy everything: `mpremote cp -r . :`.

`main.py` runs at boot and brings the screen up. The UI runs on an LVGL timer, so
the REPL stays free: `mpremote repl`, then for example `import ui` and poke at
`ui.ui_TrafficLabDisplay`.

## What is here

| File | What it does |
|---|---|
| `main.py` | Starts the board, the S: drive for fonts and images, the UI and the task handler |
| `board.py` | Display, touch and backlight bring-up - pins and bus settings at the top |
| `ui.py` | Every object as a module global, the theme, and `init()` |
| `ui_TrafficLabDisplay.py` | Screen "TrafficLabDisplay" |
| `ui_TrafficLabDisplay__part2.py` | Part 2 of screen "TrafficLabDisplay", too big for one module |
| `ui_TrafficLabDisplay__part3.py` | Part 3 of screen "TrafficLabDisplay", too big for one module |
| `ui_helpers.py` | What event code calls: flags, screen changes, increments |
| `ui_i18n.py` | The languages: every translated text, `set_language()` and `next_language()` |
| `ui_imgmem.py` | Screen "ui_imgmem" |
| `ui_fonts.py` | Fonts loaded from `/fonts`, and a `UI_ICON_*` string per icon |
| `lw_math.py` | Formula arithmetic that behaves like the C export (no exceptions from a bad reading) |
| `app_vars.py` | Your variables - `import app_vars as V`, then read or set `V.var_name` |
| `app_logic.py` | Variable refresh, bindings and automations |
| `manifest.py` | Freezes the modules above (all but `main.py`) into the firmware |
| `fonts/` | Fonts the firmware does not have built in, as LVGL binary fonts |
| `*.bin` | Images in LVGL 9's binary format, read from drive S: |

## Differences from the Arduino export

- Fonts other than Montserrat 12, 14 and 16 are files in `/fonts`, loaded at start-up.
- Images are always files, including ones set to compile in.
- Custom calendar day names are not available; LVGL's own are shown.
- Encoder and button inputs are not exported yet, nor the BME280, BMP280, SCD4x, VL53L0X,
  RS485 / Modbus and CAN bus among the peripherals. The others, and every I/O expander, are a driver
  module each, written from the Arduino library or driver that reads the same part.
- A deleted screen's objects go back to `None`, so an event aimed at one is skipped
  instead of touching freed memory.

## Something wrong?

- **Blank or white screen:** check the pins at the top of `board.py`, and try the other
  `display.init()` type if the driver has two.
- **Colours inverted or red and blue swapped:** `set_color_inversion()` and
  `color_byte_order` in `board.py`.
- **A font missing:** `ui_fonts` prints which file did not load - check `/fonts` was copied.
- **An error in the REPL, then the screen stops:** the task handler stops on an exception;
  the traceback names the file and line.

---

Made with [LCD Wizard](https://lcdwizard.com/) - the LVGL designer for Arduino and MicroPython display boards.
