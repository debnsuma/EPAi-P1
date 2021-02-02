import time
from math import pi, tan

# 1. Generate power of a number function
def squared_power_list(num, *, start=0, end):

    if start >= 0 and end >= start:
        result = [num ** i for i in range(start, end + 1)]
    else:
        print("The parameter 'start' should be 0 or more and can not be negative and 'end' should be equal to or more than 'start'")
        result = []
    return result

# 2. Polygon Area Calculator Function
def polygon_area(side_length, *, sides=3):
    if side_length > 0 and sides >= 3 and sides <= 6:
        area = sides * (side_length ** 2) / (4 * tan(pi / sides))
    else:
        print("Side Length can not be negative and Sides can be only 3, 4, 5, 6")
        area = None
    return area

# 3. Temperature Conversion Function
def temp_converter(temperature, *, temp_given_in='c'):
    if temp_given_in == 'c' and temperature >= -273.15:
        temp_in_f = temperature * 9 / 5 + 32
        temp_in_k = temperature + 273.15
        print(
            f'For given temperature in {temperature:.3f} C is equivelent to  {temp_in_f:.3f} F or {temp_in_k:.3f} K ')
        temp1 = temp_in_f
        temp1_b = "F"
        temp2 = temp_in_k
        temp2_b = "K"
    elif temp_given_in == 'f' and temperature > -459.67:
        temp_in_c = (temperature - 32) / 1.8
        temp_in_k = (temperature - 32) / 1.8 + 273.15
        print(
            f'For given temperature in {temperature:.3f} F is equivelent to  {temp_in_c:.3f} C or {temp_in_k:.3f} K ')
        temp1 = temp_in_c
        temp1_b = "C"
        temp2 = temp_in_k
        temp2_b = "K"
    elif temp_given_in == 'k' and temperature >= 0:
        temp_in_c = temperature - 273.15
        temp_in_f = (temperature - 273.15) * 9 / 5 + 32
        print(
            f'For given temperature in {temperature:.3f} K is equivelent to  {temp_in_c:.3f} C or {temp_in_f:.3f} F ')
        temp1 = temp_in_c
        temp1_b = "C"
        temp2 = temp_in_f
        temp2_b = "F"
    else:
        lis = ['c', 'f', 'k']
        if temp_given_in not in lis:
            print("Check input temperature base")
            temp1 = temp1_b = temp2 = temp2_b = None
        elif temp_given_in == 'c' and temperature < -273.15:
            print("For Celius Temperature cannot be less than -273.15")
            temp1 = temp1_b = temp2 = temp2_b = None
        elif temp_given_in == 'f' and temperature > -459.67:
            print("For fahrenheit Temperature cannot be less than -459.67")
            temp1 = temp1_b = temp2 = temp2_b = None
        else:
            print("For Kelvin Temperature cannot be less than 0")
            temp1 = temp1_b = temp2 = temp2_b = None
    return temp1, temp1_b, temp2, temp2_b


# 4. Speed Converter Function
def speed_converter(speed, *, dist='km',time='min'):
    table_dist = {"km": 1, 'm': 1000, "ft": 3280.84, "yrd": 1093.61, "mile": 0.621371}
    time_dist = {"ms": 1 / (3.6 * 10 ** 6), "s": 1 / 3600, "min": 1 / 60, "hr": 1, "day": 24}
    if speed >= 0 and dist in table_dist and time in time_dist:
        d_value = table_dist.get(dist)
        t_value = time_dist.get(time)
        speed_converted = speed * d_value * t_value
        print(f'Speed in {speed:.3e} in kmph is equal to {speed_converted:.3e} in {dist}/{time}')
    elif dist not in table_dist and time not in time_dist:
        speed_converted = None
        print('Provide time(ms,s,min,hr,day) and distnace(km,m,mile,yrd or ft) in proper units  ')
    elif dist not in table_dist:
        speed_converted = None
        print('Provide proper distance  units')
    elif time not in time_dist:
        speed_converted = None
        print('Provide proper  time  units ')
    else:
        speed_converted = None
        print('speed cannot be negative')
    return speed_converted

# The Main time_it function
def time_it(fn, *args, repetitions=1, **kwargs):

    # Starting the timer
    start = time.perf_counter()
    if not callable(fn):
        print('The given function is undefined')

    elif repetitions > 0:
        # Starting the loop
        for i in range(repetitions):
            fn(*args, **kwargs)
    else:
        print("Repetitions should be greter than 0")
        repetitions = 1

    # Ending the timer
    end = time.perf_counter()

    # Calculating the average run time per call for the function
    avg_run_time = (end - start) / repetitions

    return avg_run_time
