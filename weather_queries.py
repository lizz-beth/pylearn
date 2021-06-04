def base_query(place, lat, lon):
    return {
        "q": place,
        "lat": lat,
        "lon": lon,
        "callback": "test",
        "id": "2172797",
        "lang": "ru",
        "units": "metric",
        "mode": "html"
    }


def place_query(place):
    return base_query(place, 0, 0)


def coord_query(lat, lon):
    return base_query("", lat, lon)


def current_place_query():
    import coords
    return coord_query(*coords.current())
