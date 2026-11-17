import lvgl as lv

from .colors import Colors
from .style import Style


class Theme:
    current_theme = Colors.TYPE
    bus = Colors.BUS
    train = Colors.TRAIN
    ferry = Colors.FERRY
    all = Colors.ALL

    @staticmethod
    def select(index: int):
        if index == 0:
            Theme.current_theme = Theme.bus

        elif index == 1:
            Theme.current_theme = Theme.train

        elif index == 2:
            Theme.current_theme = Theme.ferry

        elif index == 3:
            Theme.current_theme = Theme.all

        else:
            return

        Colors.TYPE = Theme.current_theme

        Style.LABEL_TIME.set_text_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.LABEL_LINE.set_text_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.LABEL_DESTINATION.set_text_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.LABEL_POS.set_text_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.PANEL_DEPARTURE_COLUMN.set_bg_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.DROPDOWN_MAIN_CHECKED.set_border_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.DROPDOWN_LIST_SELECTED_CHECKED.set_text_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        # Style.DROPDOWN_LIST_SELECTED_PRESSED.set_text_color(lv.color_hex(Colors.TYPE))
        Style.DROPDOWN_ICON.set_text_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.PANEL_LOCATION.set_border_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.LABEL_LOCATION_ICON.set_text_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.LABEL_LOCATION_TYPE.set_bg_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.LABEL_LOCATION_TYPE.set_text_color(
            lv.color_hex(
                Colors.TYPE
            )
        )
        Style.PANEL_MESSAGE_BOX_SAVE_RESULT_SUCCESS.set_bg_color(
            lv.color_hex(
                Colors.TYPE
            )
        )

        interlinked_styles = (
            Style.LABEL_TIME,
            Style.LABEL_LINE,
            Style.LABEL_DESTINATION,
            Style.LABEL_POS,
            Style.PANEL_DEPARTURE_COLUMN,
            Style.DROPDOWN_MAIN_CHECKED,
            Style.DROPDOWN_LIST_SELECTED_CHECKED,
            Style.DROPDOWN_ICON,
            Style.PANEL_LOCATION,
            Style.LABEL_LOCATION_ICON,
            Style.LABEL_LOCATION_TYPE,
            Style.PANEL_MESSAGE_BOX_SAVE_RESULT_SUCCESS
        )

        for style in interlinked_styles:
            lv.obj.report_style_change(style)
