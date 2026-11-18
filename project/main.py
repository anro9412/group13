import sys
import time
import lvgl as lv
import network
import errno

from board_lvgl import start_board
from debug_log import log
from secrets import WIFI_SSID, WIFI_PASSWORD

from trafficdisplay.fonts import Fonts
from trafficdisplay.image import Image
from trafficdisplay.style import Style
from trafficdisplay.settings import Settings
from trafficdisplay.bindings import Bindings
from trafficdisplay.ui import UI
from trafficdisplay.traffic_manager import TrafficManager


class Application:
    def __init__(self):
        self.display = self.touch = self.handler = None
        self.display, self.touch, self.handler = start_board()
        self.station = self.connect_wifi()

        lv_refresh_timer = self.display.get_refr_timer()
        lv_refresh_timer.set_period(10)

        self.create_ui()
        log("student application ready")

    def create_ui(self):
        import fs_driver
        self.fs_drv = lv.fs_drv_t()
        fs_driver.fs_register(self.fs_drv, 'S')
        Fonts.init()
        Image.init()
        Style.init()
        exceptions = Settings.init()
        for exception in exceptions:
            if isinstance(
                exception,
                OSError
            ) and not (
                exception.args and
                exception.args[0] == errno.ENOENT
            ):
                raise exception

        Bindings.init()
        screen_traffic_display: lv.screen = UI.init()
        TrafficManager.init(UI.container_departures)

        return screen_traffic_display

    @staticmethod
    def connect_wifi():
        """Connect to the configured Wi-Fi network and return its station object.

        Wait for at most 15 seconds so startup can continue even when the network
        is unavailable; the returned object can still report later connectivity.
        """
        try:
            station = network.WLAN(network.STA_IF)
            station.active(True)
            station.connect(WIFI_SSID, WIFI_PASSWORD)
            # Use short sleeps to periodically check the connection.
            started = time.ticks_ms()
            while (not station.isconnected() and
                   time.ticks_diff(time.ticks_ms(), started) < 15_000):
                time.sleep_ms(250)
        except OSError:
            return None
        return station

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
