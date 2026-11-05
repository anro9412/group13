
from traffic_display import api_trafiklab


STOPS = {
    "bus": [
        {"id": "740098084", "name": "Karlskrona C"},
        {"id": "740032188", "name": "Campus Gräsvik"},
        {"id": "740000930", "name": "Lyckeby"},
        {"id": "740031870", "name": "Saltö"},
        {"id": "740024966", "name": "Nättraby"},
        {"id": "740000069", "name": "Ronneby Resecentrum"},
        {"id": "740021468", "name": "Bergåsa"}
    ],
    "train": [
        {"id": "740098084", "name": "Karlskrona C"},
        {"id": "740000069", "name": "Ronneby Resecentrum"},
        {"id": "740001537", "name": "Bergåsa station"}
    ],
    "ferry": [
        {"id": "740098084", "name": "Karlskrona C"}
    ]
}


def get_stops(transport):
    result = []

    if transport == "all":
        for stops in STOPS.values():
            for stop in stops:
                if stop not in result:
                    result.append(stop)
    else:
        result = STOPS.get(transport, [])

    return result


def get_departures(transport, stop_id):
    data = api_trafiklab.get_data(stop_id)
    departures = api_trafiklab.format_all_departures(data)

    return [row for row in departures
            if transport in ("all", row["kind"])]
