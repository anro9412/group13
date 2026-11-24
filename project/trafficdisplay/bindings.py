import lvgl as lv

from .settings import Settings


class Bindings:
    """
    Bindings is a static class that holds the responsibility for lv.subject_t
    used within Traffic Display. It has communication with LVGL and the class
    Settings. It holds the attributes of Traffic Display that can be bound.

    Most of the attributes' values within Bindings are derived from the class
    Settings's saved_default_settings_dict and Bindings has communication with
    Settings to load these default settings into the UI environment within
    Bindings, and use the currently used settings within Bindings to send a
    new_default_settings dict to the Settings class to override its
    Settings.saved_default_settings dict, that is used to save
    default_settings to a json file.

    It also holds lv.subject attributes that are only available when the
    application is running on the device, hence subjects which are not meant
    to be saved to default settings within the device's memory.

    Bindings lv.subject_t subjects that are meant to be saved to default
    settings:
    ```
        Bindings.transport_type_selected_text <-- E.g "\\uE901   Bus"
        Bindings.transport_type_selected_text_bare <-- E.g "Bus"
        Bindings.transport_type_selected_index <-- E.g 0
        Bindings.stop_selected_text <-- "\\uE902   Karlskrona Centralstation"
        Bindings.stop_selected_text_bare <-- "Karlskrona Centralstation"
        Bindings.stop_selected_index <-- E.g index value int from
            UI.dropdown_stop.get_selected method
        Bindings.transport_type_and_stop_selected_text <-- E.g
            "Bus · Karlskrona Centralstation"
    ```

    Bindings lv.subject_t subjects that are not meant to be saved to default
    settings:
    ```
        Bindings.dropdown_stop_options_text <-- The class TrafficManager
            stores its dropdown_stop_options here.
        Bindings.dropdown_stop_signal <-- Signals the class TrafficManager to
            trigger its observer to call
            TrafficManager.update_container_departures method.
    ```
    """
    transport_type_selected_text: lv.subject_t = None
    _transport_type_selected_text_buffer = bytearray(16)

    transport_type_selected_text_bare: lv.subject_t = None
    _transport_type_selected_text_bare_buffer = bytearray(16)

    transport_type_selected_index: lv.subject_t = None

    stop_selected_text: lv.subject_t = None
    _stop_selected_text_buffer = bytearray(128)

    stop_selected_text_bare: lv.subject_t = None
    _stop_selected_text_bare_buffer = bytearray(128)

    stop_selected_index: lv.subject_t = None
    stop_selected_index_new: lv.subject_t = None

    transport_type_and_stop_selected_text: lv.subject_t = None
    _transport_type_and_stop_selected_text_buffer = bytearray(128)

    dropdown_stop_options_text: lv.subject_t = None
    _dropdown_stop_options_text_buffer = bytearray(3840)

    dropdown_stop_signal: lv.subject_t = None

    @staticmethod
    def init():
        """
        init is a static method that initializes all the Bindings subject
        attributes as lv.subject_t subjects, and calls
        Bindings.load_saved_settings() to initialize all the subjects with
        configured setup as int or string subjects, with values for subjects
        that are meant to be saved with their respective values from
        Settings.saved_default_settings dict,
        Bindings.dropdown_stop_options_text with value as empty string and
        Bindings.dropdown_stop_signal with value as 0.
        """
        Bindings.transport_type_selected_text = lv.subject_t()
        Bindings.transport_type_selected_text_bare = lv.subject_t()
        Bindings.transport_type_selected_index = lv.subject_t()
        Bindings.stop_selected_text = lv.subject_t()
        Bindings.stop_selected_text_bare = lv.subject_t()
        Bindings.stop_selected_index = lv.subject_t()
        Bindings.stop_selected_index_new = lv.subject_t()
        Bindings.transport_type_and_stop_selected_text = lv.subject_t()
        Bindings.dropdown_stop_options_text = lv.subject_t()
        Bindings.dropdown_stop_signal = lv.subject_t()

        Bindings.load_saved_settings()

    @staticmethod
    def load_saved_settings():
        settings = Settings.get_saved_default_settings()

        Bindings.transport_type_selected_text.init_string(
            Bindings._transport_type_selected_text_buffer,
            None,
            len(Bindings._transport_type_selected_text_buffer),
            settings["transport_type_selected_text"]
        )

        Bindings.transport_type_selected_index.init_int(
            settings["transport_type_selected_index"]
        )
        Bindings.transport_type_selected_text_bare.init_string(
            Bindings._transport_type_selected_text_bare_buffer,
            None,
            len(Bindings._transport_type_selected_text_bare_buffer),
            settings["transport_type_selected_text_bare"]
        )

        Bindings.stop_selected_text.init_string(
            Bindings._stop_selected_text_buffer,
            None,
            len(Bindings._stop_selected_text_buffer),
            settings["stop_selected_text"]
        )

        Bindings.stop_selected_text_bare.init_string(
            Bindings._stop_selected_text_bare_buffer,
            None,
            len(Bindings._stop_selected_text_bare_buffer),
            settings["stop_selected_text_bare"]
        )

        Bindings.stop_selected_index.init_int(
            settings["stop_selected_index"]
        )

        Bindings.stop_selected_index_new.init_int(
            settings["stop_selected_index"]
        )

        Bindings.transport_type_and_stop_selected_text.init_string(
            Bindings._transport_type_and_stop_selected_text_buffer,
            None,
            len(Bindings._transport_type_and_stop_selected_text_buffer),
            settings["transport_type_and_stop_selected_text"]
        )

        Bindings.dropdown_stop_options_text.init_string(
            Bindings._dropdown_stop_options_text_buffer,
            None,
            len(Bindings._dropdown_stop_options_text_buffer),
            ""
        )

        Bindings.dropdown_stop_signal.init_int(0)

    @staticmethod
    def save_to_default_settings() -> None | Exception:
        new_default_settings = {
            "transport_type_selected_text":
                Bindings.transport_type_selected_text.get_string(),

            "transport_type_selected_text_bare":
                Bindings.transport_type_selected_text_bare.get_string(),

            "transport_type_selected_index":
                Bindings.transport_type_selected_index.get_int(),

            "stop_selected_text":
                Bindings.stop_selected_text.get_string(),

            "stop_selected_text_bare":
                Bindings.stop_selected_text_bare.get_string(),

            "stop_selected_index":
                Bindings.stop_selected_index.get_int(),

            "transport_type_and_stop_selected_text":
                Bindings.transport_type_and_stop_selected_text.get_string()
        }

        exception = Settings.save_to_default_settings(new_default_settings)

        return exception

    @staticmethod
    def reset_to_default_settings():
        default_settings = Settings.get_saved_default_settings()

        Bindings.transport_type_selected_text.copy_string(
            default_settings["transport_type_selected_text"]
        )

        Bindings.transport_type_selected_text_bare.copy_string(
            default_settings["transport_type_selected_text_bare"]
        )

        Bindings.transport_type_selected_index.set_int(
            default_settings["transport_type_selected_index"]
        )

        Bindings.stop_selected_text.copy_string(
            default_settings["stop_selected_text"]
        )

        Bindings.stop_selected_text_bare.copy_string(
            default_settings["stop_selected_text_bare"]
        )

        Bindings.stop_selected_index.set_int(
            default_settings["stop_selected_index"]
        )

        Bindings.transport_type_and_stop_selected_text.copy_string(
            default_settings["transport_type_and_stop_selected_text"]
        )
