class Colors:
    """Colors is a static class that holds standard a color hex palette that is
    frequently used within Traffic Display UI elements.

    Color palette:
    * BACKGROUND: Is used for tile Backgrounds. #BLACK
    * BACKGROUND_PANEL: Is used for panels. #DARK GREY
    * BORDER: Is used for borders on panels. #GREY
    * TYPE: Is a dynamic color that changes between BUS, TRAIN, FERRY and
    ALL during theme changes.
    * BACKGROUND_HIGHLIGHT: Is used during active press on elements in
    dropdown list menus. #BRIGHT GREY
    * TEXT_WHITE: Is used for standard white text. #WHITE
    * ARROW: Is mainly used for grey text. #MIX_BETWEEN_DARK_GREY_AND_GREY
    * TEXT_RED: Is used for red text, is the same as BUS color #RED
    * TEXT_MUTED: Was intended for muted text, but is currently the same as
    ARROW color, currently a placeholder for future potential updates. #
    MIX_BETWEEN_DARK_GREY_AND_GREY
    * TEXT_LATE: Is used for delayed time text within departure within
    departures timetable. #ORANGE
    * BUS: Is used for text, icons and borders that belongs to the bus type,
    theme uses this color to assign TYPE color during theme changes. #RED
    * TRAIN: Is used for text, icons and borders that belongs to the train
    type, theme uses this color to assign TYPE color during theme changes. #
    TURQUOISE
    * FERRY: Is used for text, icons and borders that belongs to the ferry
    type, theme uses this color to assign TYPE color during theme changes. #
    BLUE
    * ONLINE: Is intended to be used for wifi connected indicator. # Green
    * OFFLINE: Is intended to be used for wifi disconnected indicator. #RED
    * ALL:  Is used for text, icons and borders that belongs to the all types,
    theme uses this color to assign TYPE color during theme changes. #PURPLE
    """
    BACKGROUND = 0x0C0C0C
    BACKGROUND_PANEL = 0x18181B
    BORDER = 0x27272a
    TYPE = 0xE0213B
    BACKGROUND_HIGHLIGHT = 0x27272a
    TEXT_WHITE = 0xe4e6e5
    ARROW = 0x52525C
    TEXT_RED = 0xE0213B
    TEXT_MUTED = 0x52525C
    TEXT_LATE = 0xFF9500
    BUS = 0xE0213B
    TRAIN = 0x00C9A7
    FERRY = 0x4DA6FF
    ONLINE = 0x30fe06
    OFFLINE = 0xf32020
    ALL = 0xA855F7
