import lvgl as lv

from .settings import Settings


class Bindings:
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
