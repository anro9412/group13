import sys
import time

import lvgl as lv
import network

from board_lvgl import start_board
from debug_log import log
from secrets import WIFI_SSID, WIFI_PASSWORD
from traffic_display.assets import load_icons, load_fonts
from traffic_display.controls import Controls

class Application:
    def __init__(self):
        self.display = self.touch = self.handler = None
        # Load image resources
        load_icons()
        self.display, self.touch, self.handler = start_board()
        load_fonts()
        self.create_ui()
        self.connect_wifi()
        log("student application ready")

    def create_ui(self):
        """Function: Creates UI"""
        self.ui = Controls(self.display, self.touch, self.handler)

    @staticmethod
    def connect_wifi():
        'Function: Connects to WiFi'
        log("connecting to Wi-Fi SSID: " + WIFI_SSID)
        station = network.WLAN(network.STA_IF)
        station.active(True)
        station.connect(WIFI_SSID, WIFI_PASSWORD)
        started = time.ticks_ms()
        while (not station.isconnected() and
               time.ticks_diff(time.ticks_ms(), started) < 15_000):
            time.sleep_ms(250)
        log("Wi-Fi connected" if station.isconnected()
            else "Wi-Fi could not connect (timeout)")

    @staticmethod
    def show_error(error):
        """Function: Shows startup errors on the display when possible."""
        try:
            screen = lv.screen_active()
            screen.clean()
            screen.set_style_bg_color(lv.color_hex(0x000000), 0)
            screen.set_style_bg_opa(lv.OPA.COVER, 0)
            label = lv.label(screen)
            label.set_width(552)
            label.set_style_text_font(lv.font_montserrat_20, 0)
            label.set_style_text_color(lv.color_hex(0xFFFFFF), 0)
            label.set_text("Startup failed: %r\nSee Serial Monitor." % error)
            label.center()
        except Exception:
            pass


try:
    app = Application()
except Exception as error:
    log("FATAL: %r" % (error,))
    sys.print_exception(error)
    Application.show_error(error)
    raise
