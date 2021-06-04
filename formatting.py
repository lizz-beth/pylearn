def prettier(data):
    pairs = data.items()
    return "\n".join(
        ["{}:\t{}\n".format(*pair) for pair in pairs]
    )


