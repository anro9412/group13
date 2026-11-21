import lvgl as lv

from .theme import Theme
from .bindings import Bindings
from .queue_array import QueueArray


class Event:
    """Event is a static class that holds responsibility through methods of
    what happens next when a certain interaction between the user and the UI
    elements take place.

    Right now Event has access to:
    * LVGL
    * Theme class
    * Bindings class
    * QueueArray"""
    message_box_save: lv.msgbox = None
    message_box_save_result_success_queue: QueueArray = QueueArray()

    @staticmethod
    def tileview_value_changed(event: lv.event_t):
        """tileview_value_changed is an event method that is triggered when
        the user changes the current tile being viewed throughout
        Traffic Display.

        E.g. you can define here what should happen when tile_home,
        tile_departures, tile_settings is being viewed. Currently
        Traffic Display's paginators active state is being switched on and off
        here."""
        # This import was made local due to potential of conflicting imports
        # with the UI class during initialization of the classes.
        from .ui import UI 
        tile_view: lv.tileview = event.get_target_obj() # Fetches the Tileview
        tile: lv.obj = tile_view.get_tile_active() # Fetches the tile

        if tile.get_index() == 0:  # IF tile_home is being viewed.
            UI.button_paginator_tileview_home.add_state(
                lv.STATE.CHECKED
            )

            UI.button_paginator_tileview_departures.remove_state(
                lv.STATE.CHECKED
            )

        elif tile.get_index() == 1:  # IF tile_departures is being viewed
            UI.button_paginator_tileview_departures.add_state(
                lv.STATE.CHECKED
            )

            UI.button_paginator_tileview_home.remove_state(
                lv.STATE.CHECKED
            )

            UI.button_paginator_tileview_settings.remove_state(
                lv.STATE.CHECKED
            )

            # Signal to TrafficManager to update departures.
            # Bindings.dropdown_stop_signal.set_int(
            #     1 - Bindings.dropdown_stop_signal.get_int()
            # )

        elif tile.get_index() == 2:  # IF tile_settings is being viewed
            UI.button_paginator_tileview_settings.add_state(
                lv.STATE.CHECKED
            )

            UI.button_paginator_tileview_departures.remove_state(
                lv.STATE.CHECKED
            )

    @staticmethod
    def button_save_clicked(event: lv.event_t):
        """button_save_clicked is an event method that tells the UI class to
        create a messagebox, asking the user if they are sure that they want to
        save current settings to default settings."""
        from .ui import UI

        UI.message_box_save(
            "Are you sure you want to Save to Default Settings?",
            "Yes",
            "No"
        )

    @staticmethod
    def _save_current_settings_as_default():
        """_save_current_settings_as_default is a method that belongs to the
        class Event. It starts the process of contacting the Bindings class
        to save_to_default_settings.

        It tells the user through as message box if the save process was
        successful or not.

        Exceptions should be handled here!"""
        from .ui import UI

        exception = Bindings.save_to_default_settings()

        if not exception:  # Tell the user the saving process was successful.
            UI.message_box_save_result_success(
                UI.screen_traffic_display,
                "Default Settings Saved!"
            )

        else:  # Display the error message through an message box.
            UI.message_box_save(str(exception), None, "Ok")

    @staticmethod
    def button_save_agree_clicked(event: lv.event_t):
        """button_save_agree_clicked is an Event method, which gets triggered
        IF the UI.message_box_save()'s child button
        message_box_save_button_agree gets clicked.

        It tells Event to close the Event.message_box_save, and calls the
        Event._save_current_settings_as_default() method to start the
        save_to_default_settings process."""
        Event.message_box_save.close_async()
        Event._save_current_settings_as_default()

    @staticmethod
    def button_save_disagree_clicked(event: lv.event_t):
        """button_save_disagree_clicked is an Event method, which gets
        triggered IF the UI.message_box_save()'s child button
        message_box_save_button_disagree gets clicked, or the outside area of
        the message box, hence its parent.

        It tells Event to close the Event.message_box_save."""
        Event.message_box_save.close_async()

    @staticmethod
    def button_save_result_success_close(timer: lv.timer_t):
        """button_save_result_success_close is an Event timer method, which
        gets triggered IF Event._save_current_settings_as_default() method
        save_to_default_settings process was successful.

        It dequeues the success message_box from the
        Event.message_box_save_result_success_queue and closes it."""
        message_box: lv.msgbox = \
            Event.message_box_save_result_success_queue.dequeue()

        message_box.close_async()

    @staticmethod
    def button_reset_clicked(event: lv.event_t):
        """button_reset_clicked is an Event method which get triggered IF the
        UI.button_reset gets clicked, which calls Bindings to start the
        reset_to_default_settings() process.

        It also calls UI.dropdown_type and UI.dropdown_stop to tell them to
        send an event that their values have been changed. In order to trigger
        them to update their options and UI changes."""
        from .ui import UI

        Bindings.reset_to_default_settings()

        UI.dropdown_type.send_event(lv.EVENT.VALUE_CHANGED, None)
        UI.dropdown_stop.send_event(lv.EVENT.VALUE_CHANGED, None)

    @staticmethod
    def dropdown_arrow_rotation(event: lv.event_t):
        """dropdown_arrow_rotation is an Event method, which gets triggered
        when the dropdown gets opened up or closed down by the user.

        It changes the dropdown's indicator from the arrow down symbol to
        arrow up symbol when opened, and back to arrow down symbol when
        closed."""
        dropdown: lv.dropdown = event.get_target_obj()

        if event.get_code() == lv.EVENT.READY:
            dropdown.set_symbol(lv.SYMBOL.UP)

        else:
            dropdown.set_symbol(lv.SYMBOL.DOWN)

    @staticmethod
    def dropdown_selected(event: lv.event_t):
        """dropdown_selected is an Event method that is used by
        UI.dropdown_type and UI.dropdown_stop, and gets triggered during
        lv.EVENT.VALUE_CHANGED.

        It handles:
        * Configuration of dropdown elements and panel_departure_column's
        appearance, through Theme.select() and
        Event._update_label_line_and_pos method calls.
        * Updates currently selected options Bindings.
        * Triggers Bindings.dropdown_stop_signal process, which tells
        TrafficManager's observers to contact TrafficManager methods to start
        updating dropdown_stop options, and container_departure_items."""
        dropdown: lv.dropdown = event.get_target_obj()
        index: int = dropdown.get_selected()  # currently selected option index
        icon: lv.label = dropdown.get_child(0) # currently selected option icon
        # currently selected option text with icon text
        dropdown_text = dropdown.get_options().split("\n")[index]
        icon_text = dropdown_text[0:1].strip()  # currently selected icon text
        icon.set_text(icon_text)  # Change currently selected label_icon text
        # currently selected option text bare without icon text
        dropdown_text_bare = dropdown_text.replace(icon_text, "").strip()

        # IF NOT empty bare text, dropdown has options
        if dropdown_text_bare != "":
            # set dropdown text non READY, with added space for label_icon
            dropdown.set_text(" " * 7 + dropdown_text_bare)

        # IF icon_text NOT EQUAL to LOCATION symbol text
        # AND icon_text is NOT empty string
        # MEANS Event instance is of UI.dropdown_type
        if icon_text != "\uE902" and icon_text != "":

            if index == 0:  # IF BUS is selected
                Theme.select(0)  # Trigger theme change for BUS
            elif index == 1:  # ELSE IF TRAIN is selected
                Theme.select(1)  # Trigger theme change for TRAIN
            elif index == 2:  # ELSE IF FERRY is selected
                Theme.select(2)  # Trigger Theme change for FERRY
            elif index == 3:  # ELSE IF ALL is selected
                Theme.select(3)  # Trigger Theme change for ALL

            # UPDATE Bindings for currently selected transport_type
            Bindings.transport_type_selected_text.copy_string(dropdown_text)
            Bindings.transport_type_selected_text_bare.copy_string(
                dropdown_text_bare
            )
            Bindings.transport_type_selected_index.set_int(index)

            # TRIGGER UPDATE UI.label_subheading_departures through bindings
            Bindings.transport_type_and_stop_selected_text.copy_string(
                dropdown_text_bare +
                " · " +
                Bindings.stop_selected_text_bare.get_string()
            )
            # Method call to update UI.panel_departure_column's labels
            Event._update_label_line_and_pos()

        else:  # EVENT instance is of dropdown_stop
            from .ui import UI
            # UPDATE BINDINGS for currently selected stop
            Bindings.stop_selected_text.copy_string(dropdown_text)
            Bindings.stop_selected_text_bare.copy_string(dropdown_text_bare)
            Bindings.stop_selected_index.set_int(index)

            # TRIGGER UPDATE UI.label_subheading_departures through bindings
            Bindings.transport_type_and_stop_selected_text.copy_string(
                Bindings.transport_type_selected_text_bare.get_string() +
                    " · " + dropdown_text_bare
            )

            # scroll to top of container_departures
            UI.container_departures.scroll_to_y(0, 0)

            # Triggers Bindings.dropdown_stop_signal process
            Bindings.dropdown_stop_signal.set_int(
                1 - Bindings.dropdown_stop_signal.get_int()
            )

    @staticmethod
    def _update_label_line_and_pos():
        """_update_label_line_and_pos is a method that is used by
        Event.dropdown_selected(), to update the text of
        UI.panel_departure_column's containing labels UI.label_line and
        UI.label_pos according to which transport_type that is currently
        selected within UI.dropdown_type."""
        from .ui import UI

        # The bare text of currently selected transport_type
        transport_type_selected: str = \
            Bindings.transport_type_selected_text_bare.get_string().upper()
        # The currently used UI.label_line text
        label_line_text: str = UI.label_line.get_text()

        # IF transport_type_selected equals to "TRAIN" and
        # the currently used UI.label_line text is not the same
        if transport_type_selected == "TRAIN" \
            and label_line_text != "TRAIN":
            UI.label_line.set_text("TRAIN")  # UPDATE UI.label_line text
            UI.label_pos.set_text("TRACK")  # UPDATE UI.label_post text

        # ELSE IF transport_type_selected exist as string in
        # ["BUS", "FERRY", "ALL"] and the currently used UI.label_line text is
        # not the same.
        elif transport_type_selected in ["BUS", "FERRY", "ALL"] \
            and label_line_text != "LINE":
            UI.label_line.set_text("LINE")  # UPDATE UI.label_line text
            UI.label_pos.set_text("POS.")  # UPDATE UI.label_pos text

        # TODO Place holder for future decision if selected transport_type
        # TODO FERRY label_pos should be visible or not.
        # if transport_type_selected == "FERRY" \
        # and not UI.label_pos.has_flag(lv.obj.FLAG.HIDDEN):
        #     UI.label_pos.add_flag(lv.obj.FLAG.HIDDEN)

        # elif transport_type_selected in ["BUS", "TRAIN", "ALL"] \
        # and UI.label_pos.has_flag(lv.obj.FLAG.HIDDEN):
        #     UI.label_pos.remove_flag(lv.obj.FLAG.HIDDEN)
