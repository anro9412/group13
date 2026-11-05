
import requests
from secrets import TRAFIKLAB_API_KEY


def get_data(stop_id):
    url = "https://realtime-api.trafiklab.se/v1/departures/" + str(stop_id)
    response = requests.get(url + "?key=" + TRAFIKLAB_API_KEY)

    try:
        data = response.json()
        return data["departures"]

    finally:
        response.close()


def get_kind(bus):
    kind = bus["route"]["transport_mode"].lower()

    if kind == "boat":
        kind = "ferry"
    return kind


def get_line(bus):
    route = bus["route"]
    line = route.get("designation") or " "

    if get_kind(bus) == "train":
        name = route.get("name") or " "
        if "Krösatåg" in name:
            line = "Krös"
        elif "Karlskrona - Kristianstad - Malmö" in name:
            line = "Öst"
        else:
            line = name or line
    return str(line)


def get_platform(bus):
    platform = bus.get("realtime_platform")

    if not platform:
        platform = bus.get("scheduled_platform")

    if platform:
        return platform.get("designation")

    return None


def format_departure(bus):
    route = bus["route"]

    departure = {
        "time": bus["scheduled"][11:16],
        "line": get_line(bus)
    }

    platform = get_platform(bus)
    if platform:
        departure["platform"] = platform

    departure["destination"] = route.get("direction") or ""

    delay = bus.get("delay") or 0
    if delay >= 60:
        departure["delayMins"] = delay // 60

    departure["kind"] = get_kind(bus)

    if get_kind(bus) == "train":
        trip = bus.get("trip") or {}
        number = trip.get("technical_number")

        if not number:
            number = route.get("designation") or ""

        departure["train_number"] = str(number)

    return departure


def format_all_departures(departures):
    result = []
    for bus in departures:
        if not bus.get("canceled"):
            kind = get_kind(bus)

            if kind == "bus" or kind == "train" or kind == "ferry":
                departure = format_departure(bus)
                result.append(departure)
    return result
