import lvgl as lv

from .settings import Settings
from .bindings import Bindings
from .ui import UI
from .trafiklab_api import TrafiklabAPI


class TrafficManager:
    container_departures: lv.obj = None
    container_journey: lv.obj = None
    dropdown_type_selected_observer: lv.observer_t = None
    dropdown_stop_signal_observer: lv.observer_t = None
    dropdown_stop_signal_timer: lv.timer_t = None

    dropdown_stop_options: "list[dict[str, list[str]]]" = []

    @staticmethod
    def init(container_departures: lv.obj, container_journey: lv.obj = None):
        TrafficManager.container_departures = container_departures
        TrafficManager.container_journey = container_journey

        TrafficManager.dropdown_type_selected_observer = \
            Bindings.transport_type_selected_text_bare.add_observer(
                TrafficManager.initialize_dropdown_stop_items,
                None
            )
        TrafficManager.dropdown_stop_signal_observer = \
            Bindings.dropdown_stop_signal.add_observer(
                TrafficManager.update_container_departures,
                None
            )

        TrafficManager.dropdown_stop_signal_timer = \
        lv.timer_create(
            TrafficManager.incite_dropdown_stop_signal,
            60000,
            None
        )

    @staticmethod
    def initialize_dropdown_stop_items(
        observer: lv.observer_t,
        subject: lv.subject_t
    ):
        options_text = ""
        options_list: list[str] = []
        transport_type = subject.get_string().upper()
        if transport_type == "FERRY":
            transport_type = "BOAT"

        traffic_stops = Settings.traffic_stops_dict
        TrafficManager.dropdown_stop_options = []

        stop_text_bare = Bindings.stop_selected_text_bare.get_string().lower()
        found_stop_index = 0

        for id_combined in sorted(
            traffic_stops,
            key=lambda id_combined: traffic_stops[id_combined]["stop"].lower()
        ):
            if transport_type == "ALL" or \
            transport_type in traffic_stops[id_combined]["transport_modes"]:
                options_list.append(
                    f"\uE902   {traffic_stops[id_combined]["stop"]}"
                )
                TrafficManager.dropdown_stop_options.append(
                    {id_combined: traffic_stops[id_combined]}
                )

                if stop_text_bare == (
                    traffic_stops[id_combined]["stop"].lower()):
                    found_stop_index = len(options_list) - 1

        options_text = ("\n").join(options_list)

        Bindings.stop_selected_index_new.set_int(found_stop_index)
        Bindings.dropdown_stop_options_text.copy_string(options_text)

    @staticmethod
    def update_container_departures(
        observer: lv.observer_t,
        subject: lv.subject_t
    ):
        index = Bindings.stop_selected_index.get_int()
        transport_type_selected: str = \
            Bindings.transport_type_selected_text_bare.get_string().lower()

        scroll_y_position = TrafficManager.container_departures.get_scroll_y()
        TrafficManager.container_departures.clean()

        if transport_type_selected.strip() == "":
            return

        stop_selected_dict = TrafficManager.dropdown_stop_options[index]
        combined_id = next(iter(stop_selected_dict.keys()))
        parent_id, child_id = combined_id.split(":")

        departures_data: list[dict] = TrafiklabAPI.get_data(parent_id)
        departures = TrafiklabAPI.format_all_departures(departures_data)

        for departure in departures:
            transport_type: str | None = departure.get("kind")
            time: str | None = departure.get("time")
            delay_mins: int | None = departure.get("delayMins")
            line: str | None = departure.get("line")
            destination: str | None = departure.get("destination")
            platform: str | None = departure.get("platform")
            train_number: str | None = departure.get("train_number")

            if transport_type_selected == "all" or \
                transport_type_selected == transport_type:
                UI.container_departures_add_row(
                    transport_type,
                    time,
                    delay_mins,
                    line,
                    destination,
                    platform,
                    train_number
                )

        TrafficManager.container_departures.scroll_to_y(scroll_y_position, 0)

    @staticmethod
    def incite_dropdown_stop_signal(timer: lv.timer_t):
        Bindings.dropdown_stop_signal.set_int(
            1 - Bindings.dropdown_stop_signal.get_int()
    )
