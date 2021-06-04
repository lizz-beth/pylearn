import time


def write_and_sleep(dir, text, secs=5):
    do_and_sleep(
        lambda: __write_to_file(dir, text),
        secs
    )


def periodically(action, period_secs):
    while True:
        do_and_sleep(action, period_secs)


def do_and_sleep(action, secs):
    action()
    __sleep(secs)


def __write_to_file(dir, text):
    file = open(dir, "w")
    file.write(str(text))
    file.close()


def __sleep(secs):
    time.sleep(secs)
