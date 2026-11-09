from traffic_display import api_trafiklab


STATUS: str = 'Live data from Trafiklab'

STOPS: dict[str, list[dict[str, str]]] = {
    'bus': [
        {'id': '740098084', 'name': 'Karlskrona C'},
        {'id': '740032188', 'name': 'Campus Gräsvik'},
        {'id': '740000663', 'name': 'Lyckeby'},
        {'id': '740031870', 'name': 'Saltö'},
        {'id': '740024966', 'name': 'Nättraby'},
        {'id': '740000069', 'name': 'Ronneby Resecentrum'},
        {'id': '740021468', 'name': 'Bergåsa'},
    ],
    'train': [
        {'id': '740098084', 'name': 'Karlskrona C'},
        {'id': '740000069', 'name': 'Ronneby Resecentrum'},
        {'id': '740001537', 'name': 'Bergåsa station'},
    ],
    'ferry': [
        {'id': '740098084', 'name': 'Karlskrona C'},
    ],
}


def get_stops(transport: str) -> list[dict[str, str]]:
    """Return unique supported stops for one transport or for all transports. """

    if transport != 'all':
        return STOPS.get(transport, [])
    result = []
    # Compare complete stop records so shared IDs and names appear only once.
    for stops in STOPS.values():
        for stop in stops:
            if stop not in result:
                result.append(stop)
    return result


def get_departures(transport: str, stop_id: str) -> list:
    """Fetch and normalize a stop's departures, then filter by transport."""
    data: list = api_trafiklab.get_data(stop_id)
    departures: list = api_trafiklab.format_all_departures(data)

    filtered_departures: list = []

    for departure in departures:
        if transport == 'all' or transport == departure['kind']:
            filtered_departures.append(departure)

    return filtered_departures
