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
    def __init__(self) -> None:
        """Initialize hardware, resources, connectivity, and the application UI."""
        # Initialize assets around board setup: icons are prepared before the
        # display starts, while the custom font is loaded after its filesystem.
        self.display = self.touch = self.handler = None
        # Load image resources
        load_icons()
        self.display, self.touch, self.handler = start_board()
        load_fonts()
        self.station = self.connect_wifi()
        self.create_ui()
        log("student application ready")

    def create_ui(self) -> None:
        """Create the Controls instance that owns the app's screens and state."""
        self.ui: Controls = Controls(
            self.display, self.touch, self.handler, self.station, WIFI_SSID)

    @staticmethod
    def connect_wifi() -> network.WLAN | None:
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
    def show_error(error: Exception) -> None:
        """Show a startup error on the active display when LVGL is available."""
        try:
            # Replace any partially initialized screen with a simple readable
            # message; serial logging remains the fallback if display setup fails.
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
    app: Application = Application()
except Exception as error:
    log("FATAL: %r" % (error,))
    sys.print_exception(error)
    Application.show_error(error)
    raise