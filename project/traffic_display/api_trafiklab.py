import requests
from secrets import TRAFIKLAB_API_KEY


def get_departures(stop_id):
    url = "https://realtime-api.trafiklab.se/v1/departures/" + str(stop_id)

    response = requests.get(url + "?key=" + TRAFIKLAB_API_KEY)
    data = response.json()
    response.close()

    return data["departures"]


def format_departures(departures):
    result = []

    for bus in departures:
        route = bus["route"]

        result.append({
            "kind": route["transport_mode"].lower(),
            "time": bus["scheduled"][11:16],
            "line": route["designation"],
            "destination": route["direction"],
            "delayMins": bus["delay"] // 60
        })

    return result


def get_bus_departures(stop_id):
    departures = get_departures(stop_id)
    formatted = format_departures(departures)

    buses = []

    for bus in formatted:
        if bus["kind"] == "bus":
            buses.append(bus)

    return buses


def get_campus_departures():
    buses = get_bus_departures("740032188")

    result = []

    for bus in buses:
        if bus["line"] == "1":
            result.append(bus)

    result.sort(key=lambda bus: bus["time"])

    return result


def get_stops(transport):
    return [
        {
            "id": "740032188",
            "name": "Campus Gräsvik"
        }
    ]


def get_departures_for_ui(kind, stop_id):
    departures = get_departures(stop_id)
    formatted = format_departures(departures)

    result = []

    for bus in formatted:
        if kind == "all" or bus["kind"] == kind:
            result.append(bus)

    result.sort(key=lambda bus: bus["time"])

    return result
