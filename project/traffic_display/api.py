STATUS = 'UI prototype - example departures'

# ----- PROTOTYPE EXAMPLES: ersätt med api senare -----
STOP_EXAMPLES = {'bus': ['Karlskrona C', 'Campus Gräsvik', 'Lyckeby', 'Saltö', 'Nättraby', 'Ronneby Bus Station', 'Bergåsa'], 'train': ['Karlskrona C', 'Ronneby C', 'Karlshamn C', 'Sölvesborg C', 'Kristianstad C', 'Hässleholm C', 'Malmö C'], 'ferry': ['Karlskrona (Stena Terminal)']}
DEPARTURE_EXAMPLES = (
    {'time': '06:10', 'line': '1', 'platform': 'A', 'destination': 'Saltö', 'kind': 'bus'},
    {'time': '06:45', 'line': '2', 'platform': 'B', 'destination': 'Lyckeby', 'kind': 'bus'},
    {'time': '07:20', 'line': '3', 'platform': 'C', 'destination': 'Bergåsa', 'delayMins': 3, 'kind': 'bus'},
    {'time': '07:55', 'line': '1', 'platform': 'A', 'destination': 'Saltö', 'kind': 'bus'},
    {'time': '08:30', 'line': '2', 'platform': 'B', 'destination': 'Lyckeby', 'kind': 'bus'},
    {'time': '06:10', 'line': 'Öst', 'platform': '1', 'destination': 'Malmö C', 'kind': 'train', 'train_number': '1072'},
    {'time': '06:45', 'line': 'Krös', 'platform': '2', 'destination': 'Kalmar C', 'kind': 'train', 'train_number': '1073'},
    {'time': '07:20', 'line': 'SJ', 'platform': '1', 'destination': 'Stockholm C', 'delayMins': 8, 'kind': 'train', 'train_number': '1074'},
    {'time': '07:55', 'line': 'Öst', 'platform': '2', 'destination': 'Malmö C', 'kind': 'train', 'train_number': '1075'},
    {'time': '08:30', 'line': 'Krös', 'platform': '1', 'destination': 'Kalmar C', 'kind': 'train', 'train_number': '1076'},
    {'time': '18:00', 'line': 'Stena', 'destination': 'Gdynia, Poland', 'kind': 'ferry'},
)

# ----- STOP DATA: API integration point -----
def get_stops(transport):
    names = []
    for kind, stops in STOP_EXAMPLES.items():
        if transport in ('all', kind):
            for name in stops:
                if name not in names:
                    names.append(name)
    return [{'id': name, 'name': name} for name in names]

# ----- DEPARTURE DATA: your API integration point -----
def get_departures(transport, stop_id):
    return [dict(row) for row in DEPARTURE_EXAMPLES
            if transport in ('all', row['kind'])]
