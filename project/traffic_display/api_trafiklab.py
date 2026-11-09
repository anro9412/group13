
import requests
from secrets import TRAFIKLAB_API_KEY


def get_data(stop_id: str) -> list:
    """Fetch raw departure records for a stop and always close the response."""
    url = "https://realtime-api.trafiklab.se/v1/departures/" + str(stop_id)
    response = requests.get(url + "?key=" + TRAFIKLAB_API_KEY)

    try:
        # Let JSON and schema errors propagate so callers do not treat invalid
        # provider responses as successful empty departure lists.
        data = response.json()
        return data["departures"]

    finally:
        response.close()


def get_kind(transport_type: dict) -> str:
    """Return a normalized lowercase transport kind for a provider record."""
    kind = transport_type["route"]["transport_mode"].lower()

    # The API calls water transport "boat", while the UI says ferry.
    if kind == "boat":
        kind = "ferry"
    return kind

def get_line(transport_type: dict) -> str:
    """Choose the display line or operator label for a departure record."""
    route = transport_type["route"]
    line = route.get("designation") or " "

    if get_kind(transport_type) == "train":
        # Use short recognizable names for the regional routes; other trains
        # show their provider route name, falling back to the designation.
        name = route.get("name") or " "
        if "Krösatåg" in name:
            line = "Krös"
        elif "Karlskrona - Kristianstad - Malmö" in name:
            line = "Öst"
        else:
            line = name or line
    return str(line)


def get_platform(transport_type: dict) -> "str | None":
    """Return the realtime platform designation, falling back to the schedule."""
    platform = transport_type.get("realtime_platform")

    # A missing realtime platform is common, so retain useful scheduled data.
    if not platform:
        platform = transport_type.get("scheduled_platform")

    if platform:
        return platform.get("designation")

    return None


def clean_destination(value: "str | None") -> str:
    """Trim a destination and remove a duplicated phrase joined by a separator."""
    destination = (value or "").strip()
    # Test the recognized joiners and split only when both sides are identical.
    # This avoids altering legitimate destination names that contain punctuation.
    for separator in ("", " ", ", ", " - "):
        repeated_length = len(destination) - len(separator)
        if repeated_length > 0 and repeated_length % 2 == 0:
            half = repeated_length // 2
            first = destination[:half]
            middle = destination[half:half + len(separator)]
            second = destination[half + len(separator):]
            if middle == separator and first.strip() == second.strip():
                return first.strip()
    return destination


def format_departure(transport_type: dict) -> dict:
    """Convert one provider record into the UI's compact departure structure."""
    route = transport_type["route"]

    # Slice the provider's ISO timestamp to its local-looking HH:MM segment,
    # matching the format expected by the departure table.
    departure = {
        "time": transport_type["scheduled"][11:16],
        "line": get_line(transport_type)
    }

    platform = get_platform(transport_type)
    if platform:
        departure["platform"] = platform

    departure["destination"] = clean_destination(route.get("direction"))

    delay = transport_type.get("delay") or 0
    # Provider delay is measured in seconds; omit sub-minute delay values.
    if delay >= 60:
        departure["delayMins"] = delay // 60

    departure["kind"] = get_kind(transport_type)

    if get_kind(transport_type) == "train":
        # Prefer the trip-specific technical number, using route designation
        # only when the trip object has no number.
        trip = transport_type.get("trip") or {}
        number = trip.get("technical_number")

        if not number:
            number = route.get("designation") or ""

        departure["train_number"] = str(number)

    return departure


def format_all_departures(departures: list) -> list:
    """Normalize supported active departures and skip canceled modes."""

    result = []

    for transport_type in departures:
        if not transport_type.get("canceled"):
            kind = get_kind(transport_type)

            if kind == "bus" or kind == "train" or kind == "ferry":
                departure = format_departure(transport_type)
                result.append(departure)

    return result
