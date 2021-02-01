import time
from math import tan, pi


def _print(repetitons, *args, **kwargs):
    if "sep" not in kwargs:
        kwargs["sep"] = " "
    if "end" not in kwargs:
        kwargs["end"] = "\n"

    for i in range(repetitons):
        print(*args, sep=kwargs["sep"], end=kwargs["end"])


def _squared_power_list(repetitons, num, **kwargs):
    if "start" not in kwargs:
        kwargs["start"] = 0
    if "end" not in kwargs:
        kwargs["end"] = 0

    for i in range(repetitons):
        result = [num ** i for i in range(kwargs["start"], kwargs["end"] + 1)]
        print(result)


def _polygon_area(repetitons, side_length, **kwargs):
    if "sides" not in kwargs:
        kwargs["sides"] = 3

    if kwargs["sides"] > 6:
        print("This polygon supports area calculations of upto a hexagon(3 <= 'side' <= 6)")
    elif kwargs["sides"] < 3:
        print("Mathematics Guru says, min. no of sides a polygon can have is 3 :)")
    else:
        for i in range(repetitons):
            area = kwargs["sides"] * (side_length ** 2) / (4 * tan(pi / kwargs["sides"]))
            print(round(area, 3))


def _temp_converter(repetitons, input_temp, **kwargs):
    if "temp_given_in" not in kwargs:
        kwargs["temp_given_in"] = "f"

    if kwargs["temp_given_in"] == "c":
        for i in range(repetitons):
            out_temp = (input_temp * 9 / 5) + 32
            print(round(out_temp, 3))

    elif kwargs["temp_given_in"] == "f":
        for i in range(repetitons):
            out_temp = (input_temp - 32) * 5 / 9
            print(round(out_temp, 3))

    else:
        print("The parameter, 'temp_given_in' can be either 'f' or 'c'")


def _speed_converter(repetitons, distance, **kwargs):
    if "dist" not in kwargs:
        kwargs["dist"] = "km"
    if "time" not in kwargs:
        kwargs["time"] = "min"

    for i in range(repetitons):
        if kwargs["dist"] == "m":
            distance_in_km = distance * 0.001
        elif kwargs["dist"] == "ft":
            distance_in_km = distance * 0.0003048
        elif kwargs["dist"] == "yrd":
            distance_in_km = distance * 0.0009144
        else:
            distance_in_km = distance

        if kwargs["time"] == "ms":
            time_in_hr = 2.7778e-7
        elif kwargs["time"] == "s":
            time_in_hr = 0.00027778
        elif kwargs["time"] == "day":
            time_in_hr = 24
        else:
            time_in_hr = 1

        speed = round(distance_in_km / time_in_hr, 3)
        print(f"Speed : {speed}")


def time_it(fn, *args, repetitons=1, **kwargs):
    start = time.perf_counter()

    if fn == None:
        pass
    if fn == "print":
        _print(repetitons, *args, **kwargs)

    if fn == "squared_power_list":
        if len(args) < 1 or len(args) > 1:
            print("Need at least 2 position argument, to define the base number")
        else:
            _squared_power_list(repetitons, args[0], **kwargs)

    if fn == "polygon_area":
        if len(args) < 1 or len(args) > 1:
            print("Need at least 2 position argument, to define the side length of the polygon")
        else:
            _polygon_area(repetitons, args[0], **kwargs)

    if fn == "temp_converter":
        if len(args) < 1 or len(args) > 1:
            print("Need at least 2 position argument, to define the base temperature")
        else:
            _temp_converter(repetitons, args[0], **kwargs)

    if fn == "speed_converter":
        if len(args) < 1 or len(args) > 1:
            print("Need at least 2 position argument, to define distance travelled(in km/m/ft/yrd)")
        else:
            _speed_converter(repetitons, args[0], **kwargs)

    end = time.perf_counter()
    return round(end - start, 4)


