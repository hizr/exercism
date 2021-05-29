def convert(number):
    rain = ""
    for drop in (3, "Pling"), (5, "Plang"), (7, "Plong"):
        if number % drop[0] == 0:
            rain += drop[1]
    return rain if rain else str(number)