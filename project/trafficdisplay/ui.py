import lvgl as lv

from .image import Image
from .style import Style
from .bindings import Bindings
from .event import Event


class UI:
    screen_traffic_display: lv.obj = None

    tileview_traffic_display: lv.tileview = None
    image_logo: lv.image = None
    label_brand_traffic_22: lv.label = None
    label_brand_display_22: lv.label = None
    panel_line_tile: lv.obj = None
    container_paginator_tileview: lv.obj = None
    button_paginator_tileview_home: lv.button = None
    button_paginator_tileview_departures: lv.button = None
    button_paginator_tileview_settings: lv.button = None

    tile_home: lv.obj = None
    label_heading_home: lv.label = None
    label_subheading_home: lv.label = None

    panel_information_home: lv.obj = None
    label_brand_traffic_48: lv.label = None
    label_brand_display_48: lv.label = None
    label_swipe: lv.label = None
    label_by: lv.label = None
    label_names: lv.label = None
    panel_line_information_home: lv.obj = None

    container_group_info: lv.obj = None
    circle_initials_first: lv.obj = None
    label_initials_first: lv.label = None

    circle_initials_second: lv.obj = None
    label_initials_second: lv.label = None

    circle_initials_third: lv.obj = None
    label_initials_third: lv.label = None

    circle_initials_fourth: lv.obj = None
    label_initials_fourth: lv.label = None

    circle_initials_fifth: lv.obj = None
    label_initials_fifth: lv.label = None

    label_group_num: lv.label = None
    label_version: lv.label = None

    tile_departures: lv.obj = None
    label_heading_departures: lv.label = None
    label_subheading_departures: lv.label = None

    panel_location: lv.obj = None
    label_location_icon: lv.label = None
    label_location_stop: lv.label = None
    label_location_type: lv.label = None

    panel_information_departures: lv.obj = None

    panel_departure_column: lv.obj = None
    label_time: lv.label = None
    label_line: lv.label = None
    label_destination: lv.label = None
    label_pos: lv.label = None

    container_departures: lv.obj = None

    tile_settings: lv.obj = None

    label_heading_settings: lv.label = None
    label_subheading_settings: lv.label = None
    button_save_to_default: lv.button = None
    label_save_to_default: lv.label = None

    button_reset_to_default: lv.button = None
    label_reset_to_default: lv.label = None

    label_transport_type: lv.label = None
    label_stop: lv.label = None

    dropdown_type: lv.dropdown = None
    dropdown_type_icon: lv.label = None

    dropdown_stop: lv.dropdown = None
    dropdown_stop_icon: lv.label = None

    @staticmethod
    def init() -> lv.obj:
        UI.screen_traffic_display: lv.obj = lv.screen_active()

        UI.tileview_traffic_display: lv.tileview = UI.tileview(
            UI.screen_traffic_display
        )
        UI.image_logo: lv.image = UI.image(
            UI.screen_traffic_display,
            Image.traffic_display_logo,
            Style.IMAGE_LOGO
        )
        UI.label_brand_traffic_22: lv.label = UI.label(
            UI.screen_traffic_display,
            "Traffic",
            Style.LABEL_BRAND_TRAFFIC_22
        )
        UI.label_brand_display_22: lv.label = UI.label(
            UI.screen_traffic_display,
            "Display",
            Style.LABEL_BRAND_DISPLAY_22
        )
        UI.panel_line_tile: lv.obj = UI.obj(
            UI.screen_traffic_display,
            Style.PANEL_LINE_TILE
        )

        UI.container_paginator_tileview, \
            UI.button_paginator_tileview_home, \
            UI.button_paginator_tileview_departures, \
            UI.button_paginator_tileview_settings = \
            UI.build_paginator_tileview_traffic_display(
                UI.screen_traffic_display
            )

        UI.tile_home: lv.obj = UI.tile(
            UI.tileview_traffic_display, 0, 0, lv.DIR.RIGHT
        )
        UI.label_heading_home: lv.label = UI.label(
            UI.tile_home,
            "Welcome",
            Style.LABEL_HEADING
        )
        UI.label_subheading_home: lv.label = UI.label(
            UI.tile_home,
            "Karlskrona · Region Transport",
            Style.LABEL_SUBHEADING
        )

        UI.panel_information_home: lv.obj = UI.obj(
            UI.tile_home,
            Style.PANEL_INFORMATION
        )
        UI.label_brand_traffic_48: lv.label = UI.label(
            UI.panel_information_home,
            "Traffic",
            Style.LABEL_BRAND_TRAFFIC_48
        )
        UI.label_brand_display_48: lv.label = UI.label(
            UI.panel_information_home,
            "Display",
            Style.LABEL_BRAND_DISPLAY_48
        )
        UI.label_swipe: lv.label = UI.label(
            UI.panel_information_home,
            "Swipe to get started",
            Style.LABEL_SWIPE
        )
        UI.label_by: lv.label = UI.label(
            UI.panel_information_home,
            "BY",
            Style.LABEL_BY
        )
        UI.label_names: lv.label = UI.label(
            UI.panel_information_home,
            "Johan · Andrée · Liza · Ludwig · Angël",
            Style.LABEL_NAMES
        )
        UI.panel_line_information_home: lv.obj = UI.obj(
            UI.panel_information_home,
            Style.PANEL_LINE_INFORMATION
        )

        UI.container_group_info: lv.obj = UI.obj(
            UI.panel_information_home,
            Style.CONTAINER_GROUP_INFO
        )
        UI.circle_initials_first: lv.obj = UI.obj(
            UI.container_group_info,
            (
                Style.CIRCLE_INITIALS,
                Style.CIRCLE_INITIALS_FIRST,
                Style.INITIALS_RED
            )
        )
        UI.label_initials_first: lv.label = UI.label(
            UI.circle_initials_first,
            "J",
            (
                Style.LABEL_INITIALS_LETTER,
                Style.INITIALS_RED
            )
        )

        UI.circle_initials_second: lv.obj = UI.obj(
            UI.container_group_info,
            (
                Style.CIRCLE_INITIALS,
                Style.CIRCLE_INITIALS_SECOND,
                Style.INITIALS_TURQUOISE
            )
        )
        UI.label_initials_second: lv.label = UI.label(
            UI.circle_initials_second,
            "A",
            (
                Style.LABEL_INITIALS_LETTER,
                Style.INITIALS_TURQUOISE
            )
        )

        UI.circle_initials_third: lv.obj = UI.obj(
            UI.container_group_info,
            (
                Style.CIRCLE_INITIALS,
                Style.CIRCLE_INITIALS_THIRD,
                Style.INITIALS_BLUE
            )
        )
        UI.label_initials_third: lv.label = UI.label(
            UI.circle_initials_third, 
            "L",
            (
                Style.LABEL_INITIALS_LETTER, 
                Style.INITIALS_BLUE
            )
        )

        UI.circle_initials_fourth: lv.obj = UI.obj(
            UI.container_group_info,
            (
                Style.CIRCLE_INITIALS,
                Style.CIRCLE_INITIALS_FOURTH,
                Style.INITIALS_ORANGE
            )
        )
        UI.label_initials_fourth: lv.label = UI.label(
            UI.circle_initials_fourth,
            "L",
            (
                Style.LABEL_INITIALS_LETTER,
                Style.INITIALS_ORANGE
            )
        )

        UI.circle_initials_fifth: lv.obj = UI.obj(
            UI.container_group_info, 
            (
                Style.CIRCLE_INITIALS, 
                Style.CIRCLE_INITIALS_FIFTH, 
                Style.INITIALS_PURPLE
            )
        )
        UI.label_initials_fifth: lv.label = UI.label(
            UI.circle_initials_fifth,
            "A",
            (
                Style.LABEL_INITIALS_LETTER,
                Style.INITIALS_PURPLE
            )
        )

        UI.label_group_num: lv.label = UI.label(
            UI.container_group_info, 
            "Group 13", 
            Style.LABEL_GROUP_NUM
        )
        UI.label_version: lv.label = UI.label(
            UI.panel_information_home,
            "v1.0.12",
            Style.LABEL_VERSION
        )

        UI.tile_departures: lv.obj = UI.tile(
            UI.tileview_traffic_display, 1, 0, lv.DIR.HOR
        )
        UI.label_heading_departures: lv.label = UI.label(
            UI.tile_departures,
            "Departures",
            Style.LABEL_HEADING
        )
        UI.label_subheading_departures: lv.label = UI.label(
            UI.tile_departures,
            Bindings.transport_type_and_stop_selected_text,
            Style.LABEL_SUBHEADING
        )

        UI.panel_location: lv.obj = UI.obj(
            UI.tile_departures,
            Style.PANEL_LOCATION
        )
        UI.label_location_icon: lv.label = UI.label(
            UI.panel_location,
            "\uE902",
            Style.LABEL_LOCATION_ICON
        )
        UI.label_location_stop: lv.label = UI.label(
            UI.panel_location,
            Bindings.stop_selected_text_bare,
            Style.LABEL_LOCATION_STOP
        )
        UI.label_location_type: lv.label = UI.label(
            UI.panel_location, 
            Bindings.transport_type_selected_text_bare,
            Style.LABEL_LOCATION_TYPE
        )

        UI.panel_information_departures: lv.obj = UI.obj(
            UI.tile_departures,
            Style.PANEL_INFORMATION
        )

        UI.panel_departure_column: lv.obj = UI.obj(
            UI.panel_information_departures,
            Style.PANEL_DEPARTURE_COLUMN
        )
        UI.container_departures: lv.obj = UI.obj(
            UI.panel_information_departures,
            Style.CONTAINER_DEPARTURES,
            remove_flags=None,
            scroll_direction=lv.DIR.VER
        )
        UI.label_time: lv.label = UI.label(
            UI.panel_departure_column,
            "TIME",
            Style.LABEL_TIME
        )
        UI.label_line: lv.label = UI.label(
            UI.panel_departure_column,
            "LINE",
            Style.LABEL_LINE
        )
        UI.label_destination: lv.label = UI.label(
            UI.panel_departure_column,
            "DESTINATION",
            Style.LABEL_DESTINATION
        )
        UI.label_pos: lv.label = UI.label(
            UI.panel_departure_column,
            "POS.",
            Style.LABEL_POS
        )

        UI.tile_settings: lv.obj = UI.tile(
            UI.tileview_traffic_display, 2, 0, lv.DIR.LEFT
        )

        UI.label_heading_settings: lv.label = UI.label(
            UI.tile_settings,
            "Settings",
            Style.LABEL_HEADING
        )
        UI.label_subheading_settings: lv.label = UI.label(
            UI.tile_settings,
            "Preferences for this session",
            Style.LABEL_SUBHEADING
        )
        UI.button_save_to_default, UI.label_save_to_default = \
        UI.build_button_save(
            UI.tile_settings
        )

        UI.button_reset_to_default, UI.label_reset_to_default = \
        UI.build_button_reset(
            UI.tile_settings
        )

        UI.label_transport_type: lv.label = UI.label(
            UI.tile_settings,
            "TRANSPORT TYPE",
            Style.LABEL_TRANSPORT_TYPE
        )
        UI.label_stop: lv.label = UI.label(
            UI.tile_settings,
            "STOP",
            Style.LABEL_STOP
        )

        UI.dropdown_type, UI.dropdown_type_icon = UI.build_dropdown_type(
            UI.tile_settings
        )

        UI.dropdown_stop, UI.dropdown_stop_icon = UI.build_dropdown_stop(
            UI.tile_settings
        )
        UI.dropdown_stop_observer_initialize()

        return UI.screen_traffic_display

    @staticmethod
    def tileview(parent: lv.obj) -> lv.tileview:
        tileview = lv.tileview(parent)
        tileview.add_style(Style.TILEVIEW_TRAFFIC_DISPLAY, lv.PART.MAIN)
        tileview.add_style(Style.SCROLLBAR_TRANSPARENT, lv.PART.SCROLLBAR)

        tileview.add_event_cb(
            Event.tileview_value_changed,
            lv.EVENT.VALUE_CHANGED,
            None
        )

        return tileview

    @staticmethod
    def tile(
            parent: lv.tileview,
            column: int,
            row: int,
            direction: int
            ) -> lv.obj:

        return parent.add_tile(column, row, direction)

    @staticmethod
    def label(
            parent: lv.obj,
            text_or_binding: str | lv.subject_t | None = None,
            styles: lv.style_t | tuple[lv.style_t, ...] | None = None,
            parts: lv.part_t | lv.style_selector_t |
            tuple[lv.part_t | lv.style_selector_t, ...] = lv.PART.MAIN
    ) -> lv.label:

        label = lv.label(parent)
        styles_is_tuple = isinstance(styles, tuple)
        parts_is_tuple = isinstance(parts, tuple)

        if styles_is_tuple and parts_is_tuple:
            for i in range(len(styles)):
                label.add_style(styles[i], parts[i])

        elif styles_is_tuple:
            for style in styles:
                label.add_style(style, parts)

        elif isinstance(styles, lv.style_t):
            label.add_style(styles, parts)

        if isinstance(text_or_binding, lv.subject_t):
            label.bind_text(text_or_binding, None)

        elif isinstance(text_or_binding, str):
            label.set_text(text_or_binding)

        return label

    @staticmethod
    def button(
            parent: lv.obj,
            text_or_binding: str | lv.subject_t | None = None,
            styles_button: lv.style_t | tuple[lv.style_t, ...] | None = None,
            styles_label: lv.style_t | tuple[lv.style_t, ...] | None = None,
            parts_button: lv.part_t | lv.style_selector_t |
            tuple[lv.part_t | lv.style_selector_t, ...] = lv.PART.MAIN,
            parts_label: lv.part_t | lv.style_selector_t |
            tuple[lv.part_t | lv.style_selector_t, ...] = lv.PART.MAIN,
            add_flags: "lv.obj_flag_t | None" = None,
            remove_flags: "lv.obj_flag_t | None" = None
    ) -> lv.button | tuple[lv.button, lv.label]:

        lv_button = lv.button(parent)
        styles_is_tuple = isinstance(styles_button, tuple)
        parts_is_tuple = isinstance(parts_button, tuple)

        if add_flags:
            lv_button.add_flag(add_flags)

        if remove_flags:
            lv_button.remove_flag(remove_flags)

        if styles_is_tuple and parts_is_tuple:
            for i in range(len(styles_button)):
                lv_button.add_style(styles_button[i], parts_button[i])

        elif styles_is_tuple:
            for style in styles_button:
                lv_button.add_style(style, parts_button)

        elif isinstance(styles_button, lv.style_t):
            lv_button.add_style(styles_button, parts_button)

        if text_or_binding:
            lv_label = UI.label(
                lv_button,
                text_or_binding,
                styles_label,
                parts_label
            )

            return lv_button, lv_label

        return lv_button

    @staticmethod
    def obj(
        parent: lv.obj, 
        styles: lv.style_t | tuple[lv.style_t, ...] | None = None,
        parts: lv.part_t | lv.style_selector_t |
        tuple[lv.part_t | lv.style_selector_t, ...] = lv.PART.MAIN,
        add_flags: "lv.obj_flag_t | None" = None,
        remove_flags: "lv.obj_flag_t | None" = lv.obj.FLAG.SCROLLABLE,
        scroll_direction: lv.dir_t | None = None
    ) -> lv.obj:

        lv_object = lv.obj(parent)
        styles_is_tuple = isinstance(styles, tuple)
        parts_is_tuple = isinstance(parts, tuple)

        if add_flags:
            lv_object.add_flag(add_flags)

        if remove_flags:
            lv_object.remove_flag(remove_flags)

        if styles_is_tuple and parts_is_tuple:
            for i in range(len(styles)):
                lv_object.add_style(styles[i], parts[i])

        elif styles_is_tuple:
            for style in styles:
                lv_object.add_style(style, parts)

        elif isinstance(styles, lv.style_t):
            lv_object.add_style(styles, parts)

        if scroll_direction:
            lv_object.set_scroll_dir(scroll_direction)

        return lv_object

    @staticmethod
    def message_box_save(
            message: str | None = None,
            button_text_agree: str | None = None,
            button_text_disagree: str | None = None,
        ):

        Event.message_box_save: lv.msgbox = lv.msgbox(None)
        Event.message_box_save.add_style(
            Style.PANEL_MESSAGE_BOX_SAVE,
            lv.PART.MAIN
        )

        if message:
            Event.message_box_save.add_text(message)

        message_box_save_parent = Event.message_box_save.get_parent()
        message_box_save_parent.set_style_bg_opa(
            lv.OPA.TRANSP,
            lv.PART.MAIN
        )
        message_box_save_parent.add_event_cb(
            Event.button_save_disagree_clicked,
            lv.EVENT.CLICKED,
            None
        )

        if button_text_agree:
            message_box_save_button_agree = \
                Event.message_box_save.add_footer_button(
                    button_text_agree
                )
            message_box_save_button_agree.add_style(
                Style.BUTTON_MESSAGE_BOX,
                lv.PART.MAIN
            )
            message_box_save_button_agree.add_event_cb(
                Event.button_save_agree_clicked,
                lv.EVENT.CLICKED,
                None
            )

        if button_text_disagree:
            message_box_save_button_disagree: lv.button = \
                Event.message_box_save.add_footer_button(
                button_text_disagree
            )
            message_box_save_button_disagree.add_style(
                Style.BUTTON_MESSAGE_BOX,
                lv.PART.MAIN
            )
            message_box_save_button_disagree.add_event_cb(
                Event.button_save_disagree_clicked,
                lv.EVENT.CLICKED,
                None
            )

    @staticmethod
    def message_box_save_result_success(parent: lv.obj, message: str):
        message_box: lv.msgbox = lv.msgbox(parent)
        Event.message_box_save_result_success_queue.enqueue(message_box)
        message_box.remove_flag(lv.obj.FLAG.CLICKABLE)
        message_box.get_content().remove_flag(lv.obj.FLAG.CLICKABLE)
        message_box.add_style(
            Style.PANEL_MESSAGE_BOX_SAVE_RESULT_SUCCESS,
            lv.PART.MAIN
        )
        message_box.align(lv.ALIGN.TOP_MID, 0, 358)
        message_box.add_text(message)
        message_box.fade_in(100, 0)

        timer: lv.timer_t = lv.timer_create(
            Event.button_save_result_success_close,
            2000,
            None
        )

        timer.set_repeat_count(1)
        timer.set_auto_delete(True)

    @staticmethod
    def build_paginator_tileview_traffic_display(
        parent: lv.obj
    ) -> tuple[lv.obj, lv.button, lv.button, lv.button]:

        container_paginator_tileview = UI.obj(
            parent,
            Style.CONTAINER_PAGINATOR_TILEVIEW,
        )

        button_paginator_tileview_home = UI.button(
            container_paginator_tileview,
            styles_button=(
                Style.BUTTON_PAGINATOR_TILEVIEW,
                Style.BUTTON_PAGINATOR_TILEVIEW_CHECKED
            ),
            parts_button=(
                lv.PART.MAIN,
                lv.PART.MAIN | lv.STATE.CHECKED
            ),
            remove_flags=lv.obj.FLAG.CLICKABLE
        )

        button_paginator_tileview_departures = UI.button(
            container_paginator_tileview,
            styles_button=(
                Style.BUTTON_PAGINATOR_TILEVIEW,
                Style.BUTTON_PAGINATOR_TILEVIEW_CHECKED
            ),
            parts_button=(
                lv.PART.MAIN,
                lv.PART.MAIN | lv.STATE.CHECKED
            ),
                remove_flags=lv.obj.FLAG.CLICKABLE
        )

        button_paginator_tileview_settings = UI.button(
            container_paginator_tileview,
                styles_button=(
                    Style.BUTTON_PAGINATOR_TILEVIEW,
                    Style.BUTTON_PAGINATOR_TILEVIEW_CHECKED
                ),
                parts_button=(
                    lv.PART.MAIN,
                    lv.PART.MAIN | lv.STATE.CHECKED
                ),
                    remove_flags=lv.obj.FLAG.CLICKABLE
        )

        button_paginator_tileview_home.add_state(lv.STATE.CHECKED)

        return (
            container_paginator_tileview,
            button_paginator_tileview_home,
            button_paginator_tileview_departures,
            button_paginator_tileview_settings
        )

    @staticmethod
    def build_button_save(parent: lv.obj) -> tuple[lv.button, lv.label]:
        lv_button, lv_label = UI.button(
            parent,
            "Save",
            (
                Style.BUTTON_SAVE_TO_DEFAULT,
                Style.BUTTON_SAVE_AND_RESET_PRESSED
            ),
            Style.LABEL_SAVE_AND_RESET,
            (
                lv.PART.MAIN,
                lv.PART.MAIN | lv.STATE.PRESSED
            )
        )

        lv_button.add_event_cb(
            Event.button_save_clicked,
            lv.EVENT.CLICKED,
            None
        )

        return lv_button, lv_label

    @staticmethod
    def build_button_reset(parent: lv.obj) -> tuple[lv.button, lv.label]:
        lv_button, lv_label = UI.button(
            parent,
            "Reset",
            (
                Style.BUTTON_RESET_TO_DEFAULT,
                Style.BUTTON_SAVE_AND_RESET_PRESSED
            ),
            Style.LABEL_SAVE_AND_RESET,
            (
                lv.PART.MAIN,
                lv.PART.MAIN | lv.STATE.PRESSED
            )
        )

        lv_button.add_event_cb(
            Event.button_reset_clicked,
            lv.EVENT.CLICKED,
            None
        )

        return lv_button, lv_label


    @staticmethod
    def build_dropdown_type(parent: lv.obj) -> tuple[lv.dropdown, lv.label]:
        dropdown_type = lv.dropdown(parent)
        dropdown_type.set_options_static(
            "\uE901   Bus\n\uE903   Train\n\uE904   Ferry\n\uE900   All"
        )
        dropdown_type.bind_value(Bindings.transport_type_selected_index)
        dropdown_type.set_dir(lv.DIR.BOTTOM)
        dropdown_type.set_selected(
            Bindings.transport_type_selected_index.get_int()
        )
        dropdown_type.add_style(
            Style.DROPDOWN_TYPE_MAIN,
            lv.PART.MAIN
        )
        dropdown_type.add_style(
            Style.DROPDOWN_MAIN_CHECKED,
            lv.PART.MAIN | lv.STATE.CHECKED
        )
        dropdown_type.add_style(
            Style.DROPDOWN_MAIN_PRESSED,
            lv.PART.MAIN | lv.STATE.PRESSED
        )
        dropdown_type.add_style(
            Style.DROPDOWN_ARROW,
            lv.PART.INDICATOR
        )

        dropdown_type_icon = UI.label(
            dropdown_type,
            styles=Style.DROPDOWN_ICON
        )

        for event in (lv.EVENT.READY, lv.EVENT.CANCEL):
            dropdown_type.add_event_cb(
                Event.dropdown_arrow_rotation,
                event,
                None
            )

        dropdown_type.add_event_cb(
            Event.dropdown_selected,
            lv.EVENT.VALUE_CHANGED,
            None
        )

        dropdown_type_list = dropdown_type.get_list()
        dropdown_type_list.add_style(
            Style.DROPDOWN_TYPE_MAIN,
            lv.PART.MAIN
        )
        dropdown_type_list.add_style(
            Style.DROPDOWN_LIST_SELECTED_CHECKED,
            lv.PART.SELECTED | lv.STATE.CHECKED
        )
        dropdown_type_list.add_style(
            Style.DROPDOWN_LIST_SELECTED_PRESSED,
            lv.PART.SELECTED | lv.STATE.PRESSED
        )

        dropdown_type.send_event(lv.EVENT.VALUE_CHANGED, None)

        return dropdown_type, dropdown_type_icon

    @staticmethod
    def build_dropdown_stop(parent: lv.obj) -> tuple[lv.dropdown, lv.label]:
        dropdown_stop = lv.dropdown(parent)
        dropdown_stop.bind_value(Bindings.stop_selected_index)
        dropdown_stop.add_style(
            Style.DROPDOWN_STOP_MAIN,
            lv.PART.MAIN
        )
        dropdown_stop.add_style(
            Style.DROPDOWN_MAIN_CHECKED,
            lv.PART.MAIN | lv.STATE.CHECKED
        )
        dropdown_stop.add_style(
            Style.DROPDOWN_MAIN_PRESSED,
            lv.PART.MAIN | lv.STATE.PRESSED
        )
        dropdown_stop.add_style(
            Style.DROPDOWN_ARROW,
            lv.PART.INDICATOR
        )

        dropdown_stop_icon = UI.label(
            dropdown_stop,
            styles=Style.DROPDOWN_ICON
        )

        for event in (lv.EVENT.READY, lv.EVENT.CANCEL):
            dropdown_stop.add_event_cb(
                Event.dropdown_arrow_rotation,
                event,
                None
            )

        dropdown_stop.add_event_cb(
            Event.dropdown_selected,
            lv.EVENT.VALUE_CHANGED,
            None
        )

        dropdown_stop_list = dropdown_stop.get_list()
        dropdown_stop_list.add_style(
            Style.DROPDOWN_STOP_MAIN,
            lv.PART.MAIN
        )
        dropdown_stop_list.add_style(
            Style.DROPDOWN_LIST_SELECTED_CHECKED,
            lv.PART.SELECTED | lv.STATE.CHECKED
        )
        dropdown_stop_list.add_style(
            Style.DROPDOWN_LIST_SELECTED_PRESSED,
            lv.PART.SELECTED | lv.STATE.PRESSED
        )

        return dropdown_stop, dropdown_stop_icon

    @staticmethod
    def dropdown_stop_observer_initialize():
        Bindings.dropdown_stop_options_text.add_observer_obj(
            UI.dropdown_stop_options_changed,
            UI.dropdown_stop,
            None
        )

    @staticmethod
    def dropdown_stop_options_changed(
        observer: lv.observer_t,
        subject: lv.subject_t
    ):
        dropdown_stop_options = subject.get_string()

        if not dropdown_stop_options:
            return

        UI.dropdown_stop.set_options(
            dropdown_stop_options
        )
        UI.dropdown_stop.set_selected(
            Bindings.stop_selected_index_new.get_int()
        )
        UI.dropdown_stop.send_event(
            lv.EVENT.VALUE_CHANGED,
            None
        )

    def image(parent: lv.obj, 
              image_dsc: str | lv.image_dsc_t,
              style: lv.style_t,
              part: lv.part_t | lv.style_selector_t = lv.PART.MAIN
              ) -> lv.image:

        image = lv.image(parent)
        image.set_src(image_dsc)
        image.add_style(style, part)
        image.set_antialias(True)

        return image

    @staticmethod
    def container_departures_add_row(
        transport_type: str | None = None,
        time: str | None = None,
        delay_mins: int | None = None,
        line: str | None = None,
        destination: str | None = None,
        position: str | None = None,
        train_number: str | None = None
    ):
        panel_departures_item = UI.obj(
            UI.container_departures,
            Style.PANEL_DEPARTURES_ITEM
        )
        transport_type_selected = \
        Bindings.transport_type_selected_text_bare.get_string().lower()

        time = time or "-"
        line = line or "-"
        destination = destination or "-"
        position = position or "-"
        train_number = train_number or "-"

        if delay_mins is None or time == "-":
            UI.label(
                panel_departures_item,
                time, Style.LABEL_TIME_ITEM
            )

        else:
            hours, mins = time.split(":")
            total_time_mins = int(hours) * 60 + int(mins) + delay_mins

            hours = (total_time_mins % 1440) // 60
            mins = (total_time_mins % 1440) % 60

            hours = str(hours)
            mins = str(mins)

            if len(hours) == 1:
                hours = "0" + hours

            if len(mins) == 1:
                mins = "0" + mins

            time_estimated = ":".join([hours, mins])

            UI.label(
                panel_departures_item,
                time_estimated,
                Style.LABEL_TIME_ITEM_DELAY
            )

            UI.label(
                panel_departures_item,
                time,
                Style.LABEL_TIME_ITEM_POST
            )

        if transport_type == "bus":
            UI.label(
                panel_departures_item,
                line,
                (
                    Style.LABEL_LINE_ITEM,
                    Style.INITIALS_RED
                    )
            )

        elif transport_type == "train":
            UI.label(
                panel_departures_item,
                line,
                (
                    Style.LABEL_LINE_ITEM_TRAIN,
                    Style.INITIALS_TURQUOISE
                    )
            )
            UI.label(
                panel_departures_item,
                train_number,
                Style.LABEL_LINE_ITEM_TRAIN_ID
            )

        elif transport_type == "ferry":
            UI.label(
                panel_departures_item,
                line,
                (
                    Style.LABEL_LINE_ITEM,
                    Style.INITIALS_BLUE
                )
            )

        else:
            UI.label(
                panel_departures_item,
                line,
                (
                    Style.LABEL_LINE_ITEM,
                    Style.INITIALS_PURPLE
                )
            )

        UI.label(
            panel_departures_item,
            destination,
            Style.LABEL_DESTINATION_ITEM
        )

        UI.label(
            panel_departures_item,
            position,
            Style.LABEL_POS_ITEM
        )
