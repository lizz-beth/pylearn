from geocoder import ip


def current():
    return ip('me').latlng
