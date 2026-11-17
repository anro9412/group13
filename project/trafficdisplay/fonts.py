import lvgl as lv


class Fonts:
    figtree_semibold_48: lv.font_t = None
    figtree_semibold_28: lv.font_t = None
    figtree_semibold_22: lv.font_t = None
    figtree_semibold_16: lv.font_t = None
    figtree_semibold_12: lv.font_t = None
    inter_light_14: lv.font_t = None
    inter_light_12: lv.font_t = None
    icons_21: lv.font_t = None

    @staticmethod
    def init():
        filepath = "S:/trafficdisplay/fontsandimages/"
        Fonts.figtree_semibold_48 = lv.binfont_create(
            filepath + "ui_font_my_figtree_semibold_48.bin"
        )
        Fonts.figtree_semibold_28 = lv.binfont_create(
            filepath + "ui_font_my_figtree_semibold_28.bin"
        )
        Fonts.figtree_semibold_22 = lv.binfont_create(
            filepath + "ui_font_my_figtree_semibold_22.bin"
        )
        Fonts.figtree_semibold_16 = lv.binfont_create(
            filepath + "ui_font_my_figtree_semibold_16.bin"
        )
        Fonts.figtree_semibold_12 = lv.binfont_create(
            filepath + "ui_font_my_figtree_semibold_12.bin"
        )
        Fonts.inter_light_14 = lv.binfont_create(
            filepath + "ui_font_my_inter_28pt_light_14.bin"
        )
        Fonts.inter_light_12 = lv.binfont_create(
            filepath + "ui_font_my_inter_28pt_light_12.bin"
        )
        Fonts.icons_21 = lv.binfont_create(
            filepath + "ui_font_icons_21.bin"
        )
