import lvgl as lv

from .theme import Theme
from .bindings import Bindings
from .queue_array import QueueArray


class Event:
    message_box_save: lv.msgbox = None
    message_box_save_result_success_queue: QueueArray = QueueArray()

    @staticmethod
    def tileview_value_changed(event: lv.event_t):
        from .ui import UI
        tile_view: lv.tileview = event.get_target_obj()
        tile: lv.obj = tile_view.get_tile_active()

        if tile.get_index() == 0:
            UI.button_paginator_tileview_home.add_state(
                lv.STATE.CHECKED
            )

            UI.button_paginator_tileview_departures.remove_state(
                lv.STATE.CHECKED
            )

        elif tile.get_index() == 1:
            UI.button_paginator_tileview_departures.add_state(
                lv.STATE.CHECKED
            )

            UI.button_paginator_tileview_home.remove_state(
                lv.STATE.CHECKED
            )

            UI.button_paginator_tileview_settings.remove_state(
                lv.STATE.CHECKED
            )

            Bindings.dropdown_stop_signal.set_int(
                1 - Bindings.dropdown_stop_signal.get_int()
            )

        elif tile.get_index() == 2:
            UI.button_paginator_tileview_settings.add_state(
                lv.STATE.CHECKED
            )

            UI.button_paginator_tileview_departures.remove_state(
                lv.STATE.CHECKED
            )

    @staticmethod
    def button_save_clicked(event: lv.event_t):
        from .ui import UI

        UI.message_box_save(
            "Are you sure you want to Save to Default Settings?",
            "Yes",
            "No"
        )

    @staticmethod
    def _save_current_settings_as_default():
        from .ui import UI

        exception = Bindings.save_to_default_settings()

        if not exception:
            UI.message_box_save_result_success(
                UI.screen_traffic_display,
                "Default Settings Saved!"
            )

        else:
            UI.message_box_save(str(exception), None, "Ok")

    @staticmethod
    def button_save_agree_clicked(event: lv.event_t):
        Event.message_box_save.close_async()
        Event._save_current_settings_as_default()

    @staticmethod
    def button_save_disagree_clicked(event: lv.event_t):
        Event.message_box_save.close_async()

    @staticmethod
    def button_save_result_success_close(timer: lv.timer_t):
        message_box: lv.msgbox = \
            Event.message_box_save_result_success_queue.dequeue()

        message_box.close_async()

    @staticmethod
    def button_reset_clicked(event: lv.event_t):
        from .ui import UI

        Bindings.reset_to_default_settings()

        UI.dropdown_type.send_event(lv.EVENT.VALUE_CHANGED, None)
        UI.dropdown_stop.send_event(lv.EVENT.VALUE_CHANGED, None)

    @staticmethod
    def dropdown_arrow_rotation(event: lv.event_t):
        dropdown: lv.dropdown = event.get_target_obj()

        if event.get_code() == lv.EVENT.READY:
            dropdown.set_symbol(lv.SYMBOL.UP)

        else:
            dropdown.set_symbol(lv.SYMBOL.DOWN)

    @staticmethod
    def dropdown_selected(event: lv.event_t):
        dropdown: lv.dropdown = event.get_target_obj()
        index: int = dropdown.get_selected()
        icon: lv.label = dropdown.get_child(0)
        dropdown_text = dropdown.get_options().split("\n")[index]
        icon_text = dropdown_text[0:1].strip()
        icon.set_text(icon_text)
        dropdown_text_bare = dropdown_text.replace(icon_text, "").strip()

        if dropdown_text_bare != "":
            dropdown.set_text(" " * 7 + dropdown_text_bare)

        if icon_text != "\uE902" and icon_text != "":

            if index == 0:
                Theme.select(0)
            elif index == 1:
                Theme.select(1)
            elif index == 2:
                Theme.select(2)
            elif index == 3:
                Theme.select(3)

            Bindings.transport_type_selected_text.copy_string(dropdown_text)
            Bindings.transport_type_selected_text_bare.copy_string(
                dropdown_text_bare
            )
            Bindings.transport_type_selected_index.set_int(index)

            Bindings.transport_type_and_stop_selected_text.copy_string(
                dropdown_text_bare +
                " · " +
                Bindings.stop_selected_text_bare.get_string()
            )
            Event._update_label_line_and_pos()

        else:
            from .ui import UI
            Bindings.stop_selected_text.copy_string(dropdown_text)
            Bindings.stop_selected_text_bare.copy_string(dropdown_text_bare)
            Bindings.stop_selected_index.set_int(index)

            Bindings.transport_type_and_stop_selected_text.copy_string(
                Bindings.transport_type_selected_text_bare.get_string() +
                    " · " + dropdown_text_bare
            )

            UI.container_departures.scroll_to_y(0, 0)

            Bindings.dropdown_stop_signal.set_int(
                1 - Bindings.dropdown_stop_signal.get_int()
            )

    @staticmethod
    def _update_label_line_and_pos():
        from .ui import UI

        transport_type_selected: str = \
            Bindings.transport_type_selected_text_bare.get_string().upper()
        label_line_text: str = UI.label_line.get_text()

        if transport_type_selected == "TRAIN" \
            and label_line_text != "TRAIN":
            UI.label_line.set_text("TRAIN")
            UI.label_pos.set_text("TRACK")

        elif transport_type_selected in ["BUS", "FERRY", "ALL"] \
            and label_line_text != "LINE":
            UI.label_line.set_text("LINE")
            UI.label_pos.set_text("POS.")

        if transport_type_selected == "FERRY" \
        and not UI.label_pos.has_flag(lv.obj.FLAG.HIDDEN):
            UI.label_pos.add_flag(lv.obj.FLAG.HIDDEN)

        elif transport_type_selected in ["BUS", "TRAIN", "ALL"] \
        and UI.label_pos.has_flag(lv.obj.FLAG.HIDDEN):
            UI.label_pos.remove_flag(lv.obj.FLAG.HIDDEN)
