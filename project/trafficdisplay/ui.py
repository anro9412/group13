import lvgl as lv

from .image import Image
from .style import Style
from .bindings import Bindings
from .event import Event


class UI:
    """UI is a static class that holds responsibility for all the UI elements
    within Traffic Display, hence creating, configuring and initializing the
    elements.

    Right now UI has access to:
    * LVGL
    * Image class
    * Style class
    * Bindings class
    * Event class

    Hierarchy of attribute elements sorted by parents:
    ```
    screen_traffic_display
    |__ image_logo
    |__ label_brand_traffic_22
    |__ label_brand_display_22
    |__ panel_line_tile
    |__ container_paginator_tileview
    |   |__ button_paginator_tileview_home
    |   |__ button_paginator_tileview_departures
    |   |__ button_paginator_tileview_settings
    |__ tileview_traffic_display
        |__ tile_home
        |   |__ label_heading_home
        |   |__ label_subheading_home
        |   |__ panel_information_home
        |       |__ label_brand_traffic_48
        |       |__ label_brand_display_48
        |       |__ label_swipe
        |       |__ label_by
        |       |__ label_names
        |       |__ panel_line_information_home
        |       |__ container_group_info
        |       |   |__ circle_initials_first
        |       |   |   |__ label_initials_first
        |       |   |__ circle_initials_second
        |       |   |   |__ label_initials_second
        |       |   |__ circle_initials_third
        |       |   |   |__ label_initials_third
        |       |   |__ circle_initials_fourth
        |       |   |   |__ label_initials_fourth
        |       |   |__ circle_initials_fifth
        |       |   |   |__ label_initials_fifth
        |       |   |__ label_group_num
        |       |__ label_version
        |__ tile_departures
        |   |__ label_heading_departures
        |   |__ label_subheading_departures
        |   |__ panel_location
        |   |   |__ label_location_icon
        |   |   |__ label_location_stop
        |   |   |__ label_location_type
        |   |__ panel_information_departures
        |       |__ panel_departure_column
        |       |   |__ label_time
        |       |   |__ label_line
        |       |   |__ label_destination
        |       |   |__ label_pos
        |       |__ container_departures
        |__ tile_settings
            |__ label_heading_settings
            |__ label_subheading_settings
            |__ button_save_to_default
            |   |__ label_save_to_default
            |__ button_reset_to_default
            |   |__ label_reset_to_default
            |__ label_transport_type
            |__ label_stop
            |__ dropdown_type
            |   |__ dropdown_type_icon
            |__ dropdown_stop
                |__ dropdown_stop_icon
    ```
    """
    # Hierarchy sorted by parents
    # Main screen_traffic_display
    screen_traffic_display: lv.obj = None

    # screen_traffic_display <-- ...
    tileview_traffic_display: lv.tileview = None
    image_logo: lv.image = None
    label_brand_traffic_22: lv.label = None
    label_brand_display_22: lv.label = None
    panel_line_tile: lv.obj = None
    container_paginator_tileview: lv.obj = None

    # screen_traffic_display <-- container_paginator_tileview <-- ...
    button_paginator_tileview_home: lv.button = None
    button_paginator_tileview_departures: lv.button = None
    button_paginator_tileview_settings: lv.button = None

    # tileview_traffic_display <-- tile_home
    tile_home: lv.obj = None

    # tile_home <-- ...
    label_heading_home: lv.label = None
    label_subheading_home: lv.label = None

    # tile_home <-- panel_information_home <-- ...
    panel_information_home: lv.obj = None
    label_brand_traffic_48: lv.label = None
    label_brand_display_48: lv.label = None
    label_swipe: lv.label = None
    label_by: lv.label = None
    label_names: lv.label = None
    panel_line_information_home: lv.obj = None

    # tile_home <-- panel_information_home <-- container_group_info <-- ...
    container_group_info: lv.obj = None
    circle_initials_first: lv.obj = None  # circle_initials_first
    label_initials_first: lv.label = None  # ... <-- label_initials_first

    circle_initials_second: lv.obj = None  # circle_initials_second
    label_initials_second: lv.label = None  # ... <-- label_initials_second

    circle_initials_third: lv.obj = None  # circle_initials_third
    label_initials_third: lv.label = None  # ... <-- label_initials_third

    circle_initials_fourth: lv.obj = None  # circle_initials_fourth
    label_initials_fourth: lv.label = None  # ... <-- label_initials_fourth

    circle_initials_fifth: lv.obj = None  # circle_initials_fifth
    label_initials_fifth: lv.label = None  # ... <-- label_initials_fifth

    # container_group_info <-- label_group_num
    label_group_num: lv.label = None

    # tile_home <-- panel_information_home <-- label_version
    label_version: lv.label = None

    # tileview_traffic_display <-- tile_departures
    tile_departures: lv.obj = None

    # tile_departures <-- ...
    label_heading_departures: lv.label = None
    label_subheading_departures: lv.label = None

    # tile_departures <-- panel_location <-- ...
    panel_location: lv.obj = None
    label_location_icon: lv.label = None  # ... <-- label_location_icon
    label_location_stop: lv.label = None  # ... <-- label_location_stop
    label_location_type: lv.label = None  # ... <-- label_location_type

    # tile_departures <-- panel_information_departures
    panel_information_departures: lv.obj = None

    # tile_departures <-- panel_information_departures <-- ...
    panel_departure_column: lv.obj = None  # panel_departure_column <-- ...
    label_time: lv.label = None  # ... <-- label_time
    label_line: lv.label = None  # ... <-- label_line
    label_destination: lv.label = None  # ... <-- label_destination
    label_pos: lv.label = None  # ... <-- label_pos

    # tile_departures <-- panel_information_departures <-- ...
    container_departures: lv.obj = None

    # tileview_traffic_display <-- tile_settings
    tile_settings: lv.obj = None

    # tileview_traffic_display <-- tile_settings <-- ...
    label_heading_settings: lv.label = None
    label_subheading_settings: lv.label = None
    button_save_to_default: lv.button = None  # button_save_to_default <-- ...
    label_save_to_default: lv.label = None  # ... <-- label_save_to_default

    # tileview_traffic_display <-- tile_settings <-- ...
    button_reset_to_default: lv.button = None  # button_reset_to_default
    label_reset_to_default: lv.label = None  # ... <-- label_reset_to_default

    # tileview_traffic_display <-- tile_settings <-- ...
    label_transport_type: lv.label = None
    label_stop: lv.label = None

    # tileview_traffic_display <-- tile_settings <-- ...
    dropdown_type: lv.dropdown = None  # dropdown_type <-- ...
    dropdown_type_icon: lv.label = None  # ... <-- dropdown_type_icon

    dropdown_stop: lv.dropdown = None  # dropdown_stop <-- ...
    dropdown_stop_icon: lv.label = None  # ... <-- dropdown_stop_icon

    @staticmethod
    def init() -> lv.obj:
        """UI.init is a static method which creates and initializes all major
        UI elements that are present within the Traffic Display UI.

        All major UI elements:
        ```
        screen_traffic_display
        |__ image_logo
        |__ label_brand_traffic_22
        |__ label_brand_display_22
        |__ panel_line_tile
        |__ container_paginator_tileview
        |   |__ button_paginator_tileview_home
        |   |__ button_paginator_tileview_departures
        |   |__ button_paginator_tileview_settings
        |__ tileview_traffic_display
            |__ tile_home
            |   |__ label_heading_home
            |   |__ label_subheading_home
            |   |__ panel_information_home
            |       |__ label_brand_traffic_48
            |       |__ label_brand_display_48
            |       |__ label_swipe
            |       |__ label_by
            |       |__ label_names
            |       |__ panel_line_information_home
            |       |__ container_group_info
            |       |   |__ circle_initials_first
            |       |   |   |__ label_initials_first
            |       |   |__ circle_initials_second
            |       |   |   |__ label_initials_second
            |       |   |__ circle_initials_third
            |       |   |   |__ label_initials_third
            |       |   |__ circle_initials_fourth
            |       |   |   |__ label_initials_fourth
            |       |   |__ circle_initials_fifth
            |       |   |   |__ label_initials_fifth
            |       |   |__ label_group_num
            |       |__ label_version
            |__ tile_departures
            |   |__ label_heading_departures
            |   |__ label_subheading_departures
            |   |__ panel_location
            |   |   |__ label_location_icon
            |   |   |__ label_location_stop
            |   |   |__ label_location_type
            |   |__ panel_information_departures
            |       |__ panel_departure_column
            |       |   |__ label_time
            |       |   |__ label_line
            |       |   |__ label_destination
            |       |   |__ label_pos
            |       |__ container_departures
            |__ tile_settings
                |__ label_heading_settings
                |__ label_subheading_settings
                |__ button_save_to_default
                |   |__ label_save_to_default
                |__ button_reset_to_default
                |   |__ label_reset_to_default
                |__ label_transport_type
                |__ label_stop
                |__ dropdown_type
                |   |__ dropdown_type_icon
                |__ dropdown_stop
                    |__ dropdown_stop_icon
        ```
        """
        # Initialization of UI elements
        # Hierarchy sorted by parents
        # Main screen_traffic_display
        UI.screen_traffic_display: lv.obj = lv.screen_active()

        # screen_traffic_display <-- ...
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

        # screen_traffic_display <-- container_paginator_tileview <-- ...
        UI.container_paginator_tileview, \
            UI.button_paginator_tileview_home, \
            UI.button_paginator_tileview_departures, \
            UI.button_paginator_tileview_settings = \
            UI.build_paginator_tileview_traffic_display(
                UI.screen_traffic_display
            )

        # screen_traffic_display <-- tileview_traffic_display <-- tile_home
        UI.tile_home: lv.obj = UI.tile(
            UI.tileview_traffic_display, 0, 0, lv.DIR.RIGHT
        )

        # tileview_traffic_display <-- tile_home <-- ...
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

        # tile_home <-- panel_information_home <-- ...
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

        # tile_home <-- panel_information_home <-- container_group_info <-- ...
        UI.container_group_info: lv.obj = UI.obj(
            UI.panel_information_home,
            Style.CONTAINER_GROUP_INFO
        )

        # container_group_info <-- circle_initials_first
        UI.circle_initials_first: lv.obj = UI.obj(
            UI.container_group_info,
            (
                Style.CIRCLE_INITIALS,
                Style.CIRCLE_INITIALS_FIRST,
                Style.INITIALS_RED
            )
        )

        # container_group_info <-- circle_initials_first <-- ...
        UI.label_initials_first: lv.label = UI.label(
            UI.circle_initials_first,
            "J",
            (
                Style.LABEL_INITIALS_LETTER,
                Style.INITIALS_RED
            )
        )

        # container_group_info <-- circle_initials_second
        UI.circle_initials_second: lv.obj = UI.obj(
            UI.container_group_info,
            (
                Style.CIRCLE_INITIALS,
                Style.CIRCLE_INITIALS_SECOND,
                Style.INITIALS_TURQUOISE
            )
        )
        # container_group_info <-- circle_initials_second <-- ...
        UI.label_initials_second: lv.label = UI.label(
            UI.circle_initials_second,
            "A",
            (
                Style.LABEL_INITIALS_LETTER,
                Style.INITIALS_TURQUOISE
            )
        )

        # container_group_info <-- circle_initials_third
        UI.circle_initials_third: lv.obj = UI.obj(
            UI.container_group_info,
            (
                Style.CIRCLE_INITIALS,
                Style.CIRCLE_INITIALS_THIRD,
                Style.INITIALS_BLUE
            )
        )
        # container_group_info <-- circle_initials_third <-- ...
        UI.label_initials_third: lv.label = UI.label(
            UI.circle_initials_third,
            "L",
            (
                Style.LABEL_INITIALS_LETTER,
                Style.INITIALS_BLUE
            )
        )

        # container_group_info <-- circle_initials_fourth
        UI.circle_initials_fourth: lv.obj = UI.obj(
            UI.container_group_info,
            (
                Style.CIRCLE_INITIALS,
                Style.CIRCLE_INITIALS_FOURTH,
                Style.INITIALS_ORANGE
            )
        )
        # container_group_info <-- circle_initials_fourth <-- ...
        UI.label_initials_fourth: lv.label = UI.label(
            UI.circle_initials_fourth,
            "L",
            (
                Style.LABEL_INITIALS_LETTER,
                Style.INITIALS_ORANGE
            )
        )

        # container_group_info <-- circle_initials_fifth
        UI.circle_initials_fifth: lv.obj = UI.obj(
            UI.container_group_info,
            (
                Style.CIRCLE_INITIALS,
                Style.CIRCLE_INITIALS_FIFTH,
                Style.INITIALS_PURPLE
            )
        )
        # container_group_info <-- circle_initials_fifth <-- ...
        UI.label_initials_fifth: lv.label = UI.label(
            UI.circle_initials_fifth,
            "A",
            (
                Style.LABEL_INITIALS_LETTER,
                Style.INITIALS_PURPLE
            )
        )

        # panel_information_home <-- container_group_info <-- label_group_num
        UI.label_group_num: lv.label = UI.label(
            UI.container_group_info,
            "Group 13",
            Style.LABEL_GROUP_NUM
        )

        # panel_information_home <-- label_version
        UI.label_version: lv.label = UI.label(
            UI.panel_information_home,
            "v1.0.12",
            Style.LABEL_VERSION
        )

        # tileview_traffic_display <-- tile_departures <-- ...
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

        # tile_departures <-- panel_location <-- ...
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

        # tileview_traffic_display <-- tile_departures <-- ...
        UI.panel_information_departures: lv.obj = UI.obj(
            UI.tile_departures,
            Style.PANEL_INFORMATION
        )

        # tile_departures <-- panel_information_departures <-- ...
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

        # panel_information_departures <-- panel_departure_column <-- ...
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

        # tileview_traffic_display <-- tile_settings <-- ...
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

        # tile_settings <-- button_save_to_default <-- ...
        UI.button_save_to_default, UI.label_save_to_default = \
        UI.build_button_save(
            UI.tile_settings
        )

        # tile_settings <-- button_reset_to_default <-- ...
        UI.button_reset_to_default, UI.label_reset_to_default = \
        UI.build_button_reset(
            UI.tile_settings
        )

        # tileview_traffic_display <-- tile_settings <-- ...
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

        # tileview_traffic_display <-- tile_settings <-- dropdown_type <-- ...
        UI.dropdown_type, UI.dropdown_type_icon = UI.build_dropdown_type(
            UI.tile_settings
        )

        # tileview_traffic_display <-- tile_settings <-- dropdown_stop <-- ...
        UI.dropdown_stop, UI.dropdown_stop_icon = UI.build_dropdown_stop(
            UI.tile_settings
        )

        # Initialize dropdown_stop_observer, so UI.dropdown_stop options can
        # change dynamically based on Bindings.dropdown_stop_options_text
        UI.dropdown_stop_observer_initialize()

        # return UI.screen_traffic_display to main.py
        return UI.screen_traffic_display

    @staticmethod
    def tileview(parent: lv.obj) -> lv.tileview:
        """tileview is a static method, which creates and returns a
        lv.tileview object within its parent, it adds
        Style.TILEVIEW_TRAFFIC_DISPLAY within lv.PART.MAIN and
        Style.SCROLLBAR_TRANSPARENT within lv.PART.SCROLLBAR, making the
        scrollbar invisible.

        Also adds event Event.tileview_value_changed, when
        lv.EVENT.VALUE_CHANGED occurs, making it possible to configure certain
        events when a current tile is changed to be viewed."""
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
        """tile is a static method which creates and returns a lvgl tile
        object within its lv.tileview parent, it acts the same as
        lv.tileview.add_tile() method.

        For direction one can use lv.DIR flags."""

        return parent.add_tile(column, row, direction)

    @staticmethod
    def label(
            parent: lv.obj,
            text_or_binding: str | lv.subject_t | None = None,
            styles: lv.style_t | tuple[lv.style_t, ...] | None = None,
            parts: lv.part_t | lv.style_selector_t |
            tuple[lv.part_t | lv.style_selector_t, ...] = lv.PART.MAIN
    ) -> lv.label:
        """label is a static method that creates and returns a lv.label
        object, which makes it possible to create a lv.label object with
        multiple styles and parts in one go, including text or bind text.

        Parameter info:
        * parent: parent for the UI.label object
        * text_or_binding: IF static text use string, ELSE if bind_text use
        lv.subject_t object, None skips the label.set_text process.
        * styles: takes one lv.style_t or a tuple with multiple lv.style_t
        * parts: takes lv.part_t | lv.style_selector_t or a tuple with
        multiple lv.part_t | lv.style_selector_t

        Important notice:
        ```
        In order to add multiple different styles to parts one has to follow
        the following format:
            styles = lv.style_t, parts = lv.part_t | lv.style_selector
            --> gives one style to one part

            styles = (lv_style_t), parts = lv.part_t | lv.style_selector
            --> gives one style to one part

            styles = (lv_style_t, ...), parts = lv.part_t | lv.style_selector
            --> gives multiple styles to one part

            styles = (lv_style_t, ...),
            parts = (lv.part_t | lv.style_selector, ...)
            --> gives style from element of index to part from element of index
            The length of both tuple have to be of the same lenght, in order to
            get corresponding style to part.

            One style to multiple parts is only possible if the tuple of styles
            has the same style within its elements to different part within
            the parts tuple. And both tuple are of the same lenght.
        ```
        """

        label = lv.label(parent)
        styles_is_tuple = isinstance(styles, tuple)
        parts_is_tuple = isinstance(parts, tuple)

        # Add styles element to parts element
        if styles_is_tuple and parts_is_tuple:
            for i in range(len(styles)):
                label.add_style(styles[i], parts[i])

        # Add styles element to same parts
        elif styles_is_tuple:
            for style in styles:
                label.add_style(style, parts)

        # Add one style to one part
        elif isinstance(styles, lv.style_t):
            label.add_style(styles, parts)

        # bind_text to label
        if isinstance(text_or_binding, lv.subject_t):
            label.bind_text(text_or_binding, None)

        # set_text to label
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
        """
        button is a static method that creates and returns a lv.button and
        a lv.label object (if text_or_binding is NOT set to None),
        that is within the lv.button object, which makes it
        possible to create a lv.button and a lv.label object with multiple
        styles, parts and added flags in one go, including text or bind text
        for the label.

        Parameter info:
        * parent: parent for the UI.button object
        * text_or_binding: IF static text use string, ELSE IF bind_text use
        lv.subject_t object, None skips the label.set_text process.
        * styles_button: takes one lv.style_t or a tuple with multiple
        lv.style_t
        * styles_label: takes one lv.style_t or a tuple with multiple
        lv.style_t
        * parts_button: takes lv.part_t | lv.style_selector_t or a tuple with
        multiple lv.part_t | lv.style_selector_t
        * parts_label: takes lv.part_t | lv.style_selector_t or a tuple with
        multiple lv.part_t | lv.style_selector_t
        * add_flags: add all the flags that you want to enable on the button
        as lv.obj_flag_t
        * remove_flags: add all the flags that you want to remove from the
        button as lv.obj_flag_t

        Important general notice:
        ```
        In order to add multiple different styles to parts one has to follow
        the following format:
            styles = lv.style_t, parts = lv.part_t | lv.style_selector
            --> gives one style to one part

            styles = (lv_style_t), parts = lv.part_t | lv.style_selector
            --> gives one style to one part

            styles = (lv_style_t, ...), parts = lv.part_t | lv.style_selector
            --> gives multiple styles to one part

            styles = (lv_style_t, ...),
            parts = (lv.part_t | lv.style_selector, ...)
            --> gives style from element of index to part from element of index
            The length of both tuple have to be of the same lenght, in order to
            get corresponding style to part.

            One style to multiple parts is only possible if the tuple of styles
            has the same style within its elements to different part within
            the parts tuple. And both tuple are of the same lenght.
        ```
        """
        lv_button = lv.button(parent)
        styles_is_tuple = isinstance(styles_button, tuple)
        parts_is_tuple = isinstance(parts_button, tuple)

        # add flags to the button
        if add_flags:
            lv_button.add_flag(add_flags)

        # remove flags from the button
        if remove_flags:
            lv_button.remove_flag(remove_flags)

        # add styles_button element to parts_button element
        if styles_is_tuple and parts_is_tuple:
            for i in range(len(styles_button)):
                lv_button.add_style(styles_button[i], parts_button[i])

        # add styles_button element to same parts_button
        elif styles_is_tuple:
            for style in styles_button:
                lv_button.add_style(style, parts_button)

        # add styles_button to one parts_button
        elif isinstance(styles_button, lv.style_t):
            lv_button.add_style(styles_button, parts_button)

        # IF text_or_binding exist create lv_label, with text_or_binding and
        # its styles and parts
        if text_or_binding:
            lv_label = UI.label(
                lv_button,
                text_or_binding,
                styles_label,
                parts_label
            )

            # return both lv_button and label
            return lv_button, lv_label

        # return only lv_button
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
        """
        obj is a static method that creates and returns a lv.obj object
        which makes it possible to create a lv.obj object with multiple
        styles, parts and added flags in one go.

        Parameter info:
        * parent: parent for the UI.obj object
        * styles: takes one lv.style_t or a tuple with multiple
        lv.style_t
        * parts: takes lv.part_t | lv.style_selector_t or a tuple with
        multiple lv.part_t | lv.style_selector_t
        * add_flags: add all the flags that you want to enable on the
        lv.obj as lv.obj_flag_t
        * remove_flags: add all the flags that you want to remove from the
        lv.obj as lv.obj_flag_t
        * scroll_direction: set scroll direction with lv.DIR,
        do not forget to remove lv.obj.FLAG.SCROLLABLE from remove_flags.

        Important general notice:
        ```
        In order to add multiple different styles to parts one has to follow
        the following format:
            styles = lv.style_t, parts = lv.part_t | lv.style_selector
            --> gives one style to one part

            styles = (lv_style_t), parts = lv.part_t | lv.style_selector
            --> gives one style to one part

            styles = (lv_style_t, ...), parts = lv.part_t | lv.style_selector
            --> gives multiple styles to one part

            styles = (lv_style_t, ...),
            parts = (lv.part_t | lv.style_selector, ...)
            --> gives style from element of index to part from element of index
            The length of both tuple have to be of the same lenght, in order to
            get corresponding style to part.

            One style to multiple parts is only possible if the tuple of styles
            has the same style within its elements to different part within
            the parts tuple. And both tuple are of the same lenght.
        ```
        """
        lv_object = lv.obj(parent)
        styles_is_tuple = isinstance(styles, tuple)
        parts_is_tuple = isinstance(parts, tuple)

        # add flags to the lv_object
        if add_flags:
            lv_object.add_flag(add_flags)

        # remove flags from the object
        if remove_flags:
            lv_object.remove_flag(remove_flags)

        # add styles element to parts element
        if styles_is_tuple and parts_is_tuple:
            for i in range(len(styles)):
                lv_object.add_style(styles[i], parts[i])

        # add styles element to same parts
        elif styles_is_tuple:
            for style in styles:
                lv_object.add_style(style, parts)

        # add styles to one parts
        elif isinstance(styles, lv.style_t):
            lv_object.add_style(styles, parts)

        # set objects scroll direction
        if scroll_direction:
            lv_object.set_scroll_dir(scroll_direction)

        return lv_object

    @staticmethod
    def message_box_save(
            message: str | None = None,
            button_text_agree: str | None = None,
            button_text_disagree: str | None = None,
        ):
        """
        message_box_save is a static method which temporary creates a lv.msgbox
        with an optional message, button_agree and button_disagree text until
        the user decides to close the message box. It is mainly used for when
        UI.button_save gets clicked on, initiating the save to default
        settings process when button_text_agree gets clicked on when the
        message box is visible to the user.

        It can also be used as an error message for the user if
        button_text_agree is left as None. The message box has a preset style
        and position.
        """

        # Save and create the message box to be available within the
        # Event class with a temporary layer placed on top of screen
        Event.message_box_save: lv.msgbox = lv.msgbox(None)
        Event.message_box_save.add_style(
            Style.PANEL_MESSAGE_BOX_SAVE,
            lv.PART.MAIN
        )

        # IF message, add message as message box text description
        if message:
            Event.message_box_save.add_text(message)

        # Get parent of the message box to enable transparent background
        message_box_save_parent = Event.message_box_save.get_parent()
        message_box_save_parent.set_style_bg_opa(
            lv.OPA.TRANSP,
            lv.PART.MAIN
        )
        # Add Event to the message_box_save_parent that closes the message box
        # IF clicked on
        message_box_save_parent.add_event_cb(
            Event.button_save_disagree_clicked,
            lv.EVENT.CLICKED,
            None
        )

        # IF button_text_agree add a message box button and set text and style
        if button_text_agree:
            message_box_save_button_agree = \
                Event.message_box_save.add_footer_button(
                    button_text_agree
                )
            message_box_save_button_agree.add_style(
                Style.BUTTON_MESSAGE_BOX,
                lv.PART.MAIN
            )
            # Add Event.button_save_agree_clicked to the
            # message_box_save_button_agree which starts the saving to default
            # process IF clicked on
            message_box_save_button_agree.add_event_cb(
                Event.button_save_agree_clicked,
                lv.EVENT.CLICKED,
                None
            )

        # IF button_text_agree, add a message box button and set text and style
        if button_text_disagree:
            message_box_save_button_disagree: lv.button = \
                Event.message_box_save.add_footer_button(
                button_text_disagree
            )
            message_box_save_button_disagree.add_style(
                Style.BUTTON_MESSAGE_BOX,
                lv.PART.MAIN
            )
            # Add Event to the message_box_save_button_disagree that closes
            # the message box IF clicked on
            message_box_save_button_disagree.add_event_cb(
                Event.button_save_disagree_clicked,
                lv.EVENT.CLICKED,
                None
            )

    @staticmethod
    def message_box_save_result_success(parent: lv.obj, message: str):
        """
        message_box_save_result_success is a static method which temporary
        creates a lv.msgbox with an optional message and closes after a
        certain time period. It is mainly used for when a succesful save to
        default process has finished, and is configured to be used with
        UI.tile_settings as parent.

        It can also be used as a temporary message for the user. The message
        box has a preset style and position.
        """
        # create a message box and enqueue it to
        # Event.message_box_save_result_success_queue: queue_array
        message_box: lv.msgbox = lv.msgbox(parent)
        Event.message_box_save_result_success_queue.enqueue(message_box)
        # remove the lv.obj.FLAG.CLICKABLE from the message box
        message_box.remove_flag(lv.obj.FLAG.CLICKABLE)
        # Also remove the lv.obj.FLAG.CLICKABLE from messagebox's content
        message_box.get_content().remove_flag(lv.obj.FLAG.CLICKABLE)
        # Add the style_t Style.PANEL_MESSAGE_BOX_SAVE_RESULT_SUCCESS to the 
        # message box
        message_box.add_style(
            Style.PANEL_MESSAGE_BOX_SAVE_RESULT_SUCCESS,
            lv.PART.MAIN
        )
        # Override lv.msgbox's preset local ALIGNMENT and coordinates of the
        # message box
        message_box.align(lv.ALIGN.TOP_MID, 0, 358)
        message_box.add_text(message)  # set text message
        message_box.fade_in(100, 0)  # fade_in to view for 1 sec

        # Create a lv.timer_t for when the timer should call
        # Event.button_save_result_success_close and close the message box
        # Duration is currently 2 secs
        timer: lv.timer_t = lv.timer_create(
            Event.button_save_result_success_close,
            2000,
            None
        )

        # Repeat the timer once and set_auto_delete to True so the timer
        # deletes itself after the repeat count has finished
        timer.set_repeat_count(1)
        timer.set_auto_delete(True)

    @staticmethod
    def build_paginator_tileview_traffic_display(
        parent: lv.obj
    ) -> tuple[lv.obj, lv.button, lv.button, lv.button]:
        """
        build_paginator_tileview_traffic_display is a static method that
        builds and initializes the paginator used by Traffic Display for
        indicating the current tile being viewed.

        it returns the container_paginator_tileview, with
        button_paginator_tileview_home, button_paginator_tileview_departures
        and button_paginator_tileview_settings.
        """

        # create the container_paginator_tileview and add its style
        container_paginator_tileview = UI.obj(
            parent,
            Style.CONTAINER_PAGINATOR_TILEVIEW,
        )

        # create the button_paginator_tileview_home with UI.button method
        # and set its styles and parts, also remove lv.obj.FLAG.CLICKABLE
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

        # create the button_paginator_tileview_departures with UI.button method
        # and set its styles and parts, also remove lv.obj.FLAG.CLICKABLE
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

        # create the button_paginator_tileview_settings with UI.button method
        # and set its styles and parts, also remove lv.obj.FLAG.CLICKABLE
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

        # set button_paginator_tileview_home to CHECKED state during startup
        button_paginator_tileview_home.add_state(lv.STATE.CHECKED)

        return (
            container_paginator_tileview,
            button_paginator_tileview_home,
            button_paginator_tileview_departures,
            button_paginator_tileview_settings
        )

    @staticmethod
    def build_button_save(parent: lv.obj) -> tuple[lv.button, lv.label]:
        """build_button_save is a static method that builds the
        UI.button_save_to_default and the UI.label_save_to default, that is
        used to initialize the save to default settings process when clicked
        on.

        It returns the button_save_to_default and the label_save_to_default."""

        # Create button_save_to_default and label_save_to_default with their
        # text, styles and parts
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

        # Add Event.button_save_clicked to the button that initializes the
        # save to default settings process, through UI.message_box_save method
        # in the class Events when clicked on
        lv_button.add_event_cb(
            Event.button_save_clicked,
            lv.EVENT.CLICKED,
            None
        )

        return lv_button, lv_label

    @staticmethod
    def build_button_reset(parent: lv.obj) -> tuple[lv.button, lv.label]:
        """
        build_button_reset is a static method that builds the
        UI.button_reset_to_default and the UI.label_reset_to default, that is
        used to initialize the reset to default settings process when clicked
        on.

        It returns the button_reset_to_default and the label_reset_to_default.
        """

        # Create button_reset_to_default and label_reset_to_default with their
        # text, styles and parts
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

        # Add Event.button_reset_clicked to the button that initializes the
        # reset to default settings process in the class Events when clicked on
        lv_button.add_event_cb(
            Event.button_reset_clicked,
            lv.EVENT.CLICKED,
            None
        )

        return lv_button, lv_label

    @staticmethod
    def build_dropdown_type(parent: lv.obj) -> tuple[lv.dropdown, lv.label]:
        """
        build_dropdown_type is a static method that builds the
        UI.dropdown_type: lv.dropdown and the UI.dropdown_type_icon: lv.label
        that is used for selecting Transport types by the user within Traffic
        Display. Selected dropdown_type's index is bound to
        Bindings.transport_type_selected_index.

        It returns the dropdown_type and the dropdown_type_label.

        Currently available Transport types:
        ```
        * Bus:
            index = 0
        * Train:
            index = 1
        * Ferry:
            index = 2
        * All:
            index = 3
        ```
        """

        # create dropdown_type and set its options to static with Transport
        # types and icons
        dropdown_type = lv.dropdown(parent)
        dropdown_type.set_options_static(
            "\uE901   Bus\n\uE903   Train\n\uE904   Ferry\n\uE900   All"
        )
        # bind selected dropdown_type's index to
        # Bindings.transport_type_selected_index
        dropdown_type.bind_value(Bindings.transport_type_selected_index)
        # set dropdown opening list direction towards bottom
        dropdown_type.set_dir(lv.DIR.BOTTOM)
        # TODO Place holder uneccessary code
        # TODO dropdown_type.set_selected(
        # TODO     Bindings.transport_type_selected_index.get_int()
        # TODO )
        # add styles from the class Style to dropdown_type and its parts
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

        # create dropdown_type_label with its style from the class Style
        dropdown_type_icon = UI.label(
            dropdown_type,
            styles=Style.DROPDOWN_ICON
        )

        # add Event.dropdown_arrow_rotation to dropdown_type so its indicator
        # rotates when dropdown is open or closed
        for event in (lv.EVENT.READY, lv.EVENT.CANCEL):
            dropdown_type.add_event_cb(
                Event.dropdown_arrow_rotation,
                event,
                None
            )

        # add Event.dropdown_selected to dropdown_type, when VALUE_CHANGED
        # to trigger theme, text and label changes.
        dropdown_type.add_event_cb(
            Event.dropdown_selected,
            lv.EVENT.VALUE_CHANGED,
            None
        )

        # get dropdown_type_list and add styles from the Class styles to its
        # parts
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

        # trigger Event.dropdown_selected to update theme, text and labels
        dropdown_type.send_event(lv.EVENT.VALUE_CHANGED, None)

        return dropdown_type, dropdown_type_icon

    @staticmethod
    def build_dropdown_stop(parent: lv.obj) -> tuple[lv.dropdown, lv.label]:
        """
        build_dropdown_stop is a static method that builds the
        UI.dropdown_stop: lv.dropdown and the UI.dropdown_stop_icon: lv.label
        that is used for selecting departure stops by the user within Traffic
        Display. Selected dropdown_stop's index is bound to
        Bindings.stop_selected_index.

        It returns the dropdown_stop and  the dropdown_stop_icon.
        """

        # create dropdown_type and bind its selected index to
        # Bindings.stop_selected_index
        dropdown_stop = lv.dropdown(parent)
        dropdown_stop.bind_value(Bindings.stop_selected_index)
        # add styles from the class Style to dropdown_stop and its parts
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

        # create dropdown_stop_label with its style from the class Style
        dropdown_stop_icon = UI.label(
            dropdown_stop,
            styles=Style.DROPDOWN_ICON
        )

        # add Event.dropdown_arrow_rotation to dropdown_stop so its indicator
        # rotates when dropdown is open or closed
        for event in (lv.EVENT.READY, lv.EVENT.CANCEL):
            dropdown_stop.add_event_cb(
                Event.dropdown_arrow_rotation,
                event,
                None
            )

        # add Event.dropdown_selected to dropdown_stop, when VALUE_CHANGED
        # to trigger departure, text and label changes.
        dropdown_stop.add_event_cb(
            Event.dropdown_selected,
            lv.EVENT.VALUE_CHANGED,
            None
        )

        # get dropdown_stop_list and add styles from the Class Styles to its
        # parts
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
        """dropdown_stop_observer_initialize is a static method that
        initializes an observer over Bindings.dropdown_stop_options_text,
        which gets triggered when the class TrafficManager updates the
        available dropdown_stop's options.

        When Bindings.dropdown_stop_options_text is changed, the observer
        calls the UI.dropdown_stop_options_changed method.
        """
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
        """
        dropdown_stop_options_changed is a static method that is used by
        Bindings.dropdown_stop_options_text's observer, which happens whenever
        Bindings.dropdown_stop_options_text is changed mainly by the class
        TrafficManager.

        It gets the current Bindings.dropdown_stop_options_text, and updates
        UI.dropdown_stop options to currently available stop_options, and sets
        selected to the Bindings.stop_selected_index_new int value, making it
        possible to keep the old selected stop if available within the new
        options text. At last UI.dropdown_stop.send_event is called for
        lv.EVENT.VALUE_CHANGED calling the Event.dropdown_selected method
        which triggers the process of departure, text and label updates.
        """
        # get Bindings.dropdown_stop_options text
        dropdown_stop_options = subject.get_string()

        # IF Bindings.dropdown_stop_options text is an empty string return
        # Mainly happens durings startup of Traffic Display when no
        # stop_options are available yet, right as the
        # UI.dropdown_stop_observer_initialize method is ran. Which triggeres
        # the Binding.dropdown_stop_options_text obsever to run
        # UI.dropdown_stop_options_changed when initialized.
        if not dropdown_stop_options:
            return

        # set UI.dropdown_stop options to Bindings.dropdown_stop_options text
        UI.dropdown_stop.set_options(
            dropdown_stop_options
        )
        # set UI.dropdown_stop selected to Bindings.stop_selected_index_new
        # int value
        UI.dropdown_stop.set_selected(
            Bindings.stop_selected_index_new.get_int()
        )
        # trigger UI.dropdown_stop Event.dropdown_selected with
        # lv.EVENT.VALUE_CHANGED, starting the process of departure, text and
        # label updates
        UI.dropdown_stop.send_event(
            lv.EVENT.VALUE_CHANGED,
            None
        )

    @staticmethod
    def image(parent: lv.obj, 
              image_dsc: str | lv.image_dsc_t,
              style: lv.style_t,
              part: lv.part_t | lv.style_selector_t = lv.PART.MAIN
              ) -> lv.image:
        """
        image is a static method, which creates a lv.image object within its
        parent, using the source filepath or a lv.image_dsc_t object to set
        the source for the image. It also takes one style: lv.style_t and part:
        lv.part_t | lv.style_selector_t as arguments. Antialiasing for the
        image is set to True.

        The method returns the image as a lv.image object.
        """
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
        """
        container_departures_add_row is a static method used by the class
        TrafficManager to add departures within the UI.container_departures,
        which happens whenever a new stop is selected within UI.dropdown_stop
        options or when the departures need to be updated. The method has
        preset styles and positions from the class Style for each newly added
        row (container) and its labels.

        Parameter information:
        ```
            transport_type: str | None <-- Determines the style format being
                used on the LINE item:
                    "bus" <-- gives Style.LABEL_LINE_ITEM with
                        Style.INITIALS_RED
                    "train" <-- gives Style.LABEL_LINE_ITEM_TRAIN with
                        Style.INITIALS_TURQUOISE and train_number with
                        Style.LABEL_LINE_ITEM_TRAIN_ID
                    "ferry" <-- gives Style.LABEL_LINE_ITEM with
                        Style.INITIALS_BLUE
                    ELSE <-- gives Style.LABEL_LINE_ITEM with
                        Style.INITIALS_PURPLE
            time: str | None <-- Determines original scheduled time within
                TIME item.
            delay_mins: int | None <-- Determines the TIME item format being
                used and its new estimated time for departure.
                IF NOT delay_mins or time == "-":
                    time is displayed as original scheduled time.
                ELSE:
                    time is displayed as strike_through, and new estimated
                    time for departure is displayed as Colors.TEXT_LATE
                    # ORANGE.
            line: str | None <-- Determines the text of the label within LINE
                item.
            destination: str | None <-- Determines text of the label within
                DESTINATION item.
            position: str | None <-- Determines the text of the label within
                POS item.
            train_number: str | None <-- Determines the text of the label for
                train_number within LINE item.
        ```

        General notice:
        * When time, line, destination, position or train_number is set to
        None or an empty string, they are respectively assigned to be "-".
        """
        # create row as panel_departures_item within UI.container_departures
        # with Style.PANEL_DEPARTURES_ITEM
        panel_departures_item = UI.obj(
            UI.container_departures,
            Style.PANEL_DEPARTURES_ITEM
        )
        # TODO unused variable transport_type_selected
        # TODO Traffic Manager determines transport type that is sent to method
        # TODO transport_type_selected = \
        # TODO Bindings.transport_type_selected_text_bare.get_string().lower()

        # Assign parameter to parameter IF parameter is None or "" assign "-".
        time = time or "-"
        line = line or "-"
        destination = destination or "-"
        position = position or "-"
        train_number = train_number or "-"

        # IF not delay_mins or time == "-"
        # Display time as original scheduled time
        # This happens if delay_mins == None or int value 0 or time was
        # assigned with "-" due to usually being None
        # Normal situation is when there is no time delay and scheduled
        # departure time is present
        if not delay_mins or time == "-":
            UI.label(
                panel_departures_item,
                time, Style.LABEL_TIME_ITEM
            )

        # ELSE
        # scheduled departure time is present with an estimated delay set
        else:
            # split time from ":" into hours and mins
            hours, mins = time.split(":")
            # summarize total hours in mins + mins + delay_mins as type int
            total_time_mins = int(hours) * 60 + int(mins) + delay_mins

            # calculate the estimated hour time by using integer division on
            # the residual of total_time_mins modulus 1440 (whole days)
            hours = (total_time_mins % 1440) // 60
            # calculate the estimated min time by using the residual of mins
            # modulus 60 (whole hours) from the residual of total_time_mins
            # modulus 1440 (whole days)
            mins = (total_time_mins % 1440) % 60

            # convert hours and mins into string
            hours = str(hours)
            mins = str(mins)

            # reimplement a "0" to the beginning of hours and mins IF needed
            if len(hours) == 1:
                hours = "0" + hours

            if len(mins) == 1:
                mins = "0" + mins

            # join hours and mins by a ":" and assign to time_estimated
            time_estimated = ":".join([hours, mins])

            # initialize a UI.label within panel_departures_item with
            # time_estimated as text and Style.LABEL_TIME_ITEM_DELAY under
            # UI.label_time column
            UI.label(
                panel_departures_item,
                time_estimated,
                Style.LABEL_TIME_ITEM_DELAY
            )

            # initialize a UI.label within panel_departures_item with time
            # text and Style.LABEL_TIME_ITEM_POST under UI.label_time column
            UI.label(
                panel_departures_item,
                time,
                Style.LABEL_TIME_ITEM_POST
            )

        # IF transport_type == "bus"
        # initialize a UI.label within panel_departures_item with line text
        # and (Style.LABEL_LINE_ITEM, Style.INITIALS_RED) under
        # UI.label_line column
        if transport_type == "bus":
            UI.label(
                panel_departures_item,
                line,
                (
                    Style.LABEL_LINE_ITEM,
                    Style.INITIALS_RED
                    )
            )

        # IF transport_type == "train"
        # initialize two UI.label within panel_departures_item one with line
        # text and (Style.LABEL_LINE_ITEM_TRAIN, Style.INITIALS_TURQUOISE) and
        # one with train_number text and Style.LABEL_LINE_ITEM_TRAIN_ID under
        # UI.label_line column
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

        # IF transport_type == "ferry"
        # initialize a UI.label within panel_departures_item with line text
        # and (Style.LABEL_LINE_ITEM, Style.INITIALS_BLUE) under
        # UI.label_line column
        elif transport_type == "ferry":
            UI.label(
                panel_departures_item,
                line,
                (
                    Style.LABEL_LINE_ITEM,
                    Style.INITIALS_BLUE
                )
            )

        # ELSE
        # initialize a UI.label within panel_departures_item with line text
        # and (Style.LABEL_LINE_ITEM, Style.INITIALS_PURPLE) under
        # UI.label_line column
        else:
            UI.label(
                panel_departures_item,
                line,
                (
                    Style.LABEL_LINE_ITEM,
                    Style.INITIALS_PURPLE
                )
            )

        # initialize a UI.label within panel_departures_item with destination
        # text and Style.LABEL_DESTINATION_ITEM under
        # UI.label_destination column
        UI.label(
            panel_departures_item,
            destination,
            Style.LABEL_DESTINATION_ITEM
        )

        # initialize a UI.label within panel_departures_item with position text
        # and Style.LABEL_POS_ITEM under UI.label_pos column
        UI.label(
            panel_departures_item,
            position,
            Style.LABEL_POS_ITEM
        )
