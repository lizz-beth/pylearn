from datetime import datetime


def current_time_formatted(fmt="%H:%M:%S"):
    return datetime.now().strftime(fmt)
