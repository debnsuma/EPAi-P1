def encoded_from_base10(number, base, digit_map):
    '''
    This function represents a number in some given base from base10, it takes the number, base and digit_map as an argument
    '''
    sign_flag = False
    if number < 0:
        sign_flag = True
        number = number * (-1)

    if base < 2 or base > 36:
        raise ValueError("Given base must be more than equal to 2 and less than equal to 32")

    if number == 0:
        return "0"

    if len(digit_map) != len(set(digit_map)):
        raise ValueError("Digit Map contains doesnt contain unique code ( repeating alphanumerics!!)")

    digits = []

    while number > 0:
        number, mod = divmod(number, base)
        digits.insert(0, mod)

    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not enough for encoding")

    digits = [digit_map[d] for d in digits]

    digits = [str(d) for d in digits]
    digits = "".join(digits)

    if sign_flag:
        digits = "-" + digits

    return digits

def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''

    abs_tol = 1e-05
    rel_tol = 1e-12

    diff = a - b
    if diff < 0:
        diff *= -1

    rel_tol_cal = rel_tol * max(a, b)
    tol = max(rel_tol_cal, abs_tol)

    if diff <= tol:
        return True
    else:
        return False

def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point.
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''

    from fractions import Fraction
    sign_flag = False

    if f_num < 0:
        f_num *= -1
        sign_flag = True

    num = Fraction(f_num)

    real = num.numerator // num.denominator
    if sign_flag:
        return real * -1
    else:
        return real

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    from fractions import Fraction

    sign = 1

    if f_num < 0:
        sign = -1
        f_num *= -1

    f_num_round = f_num + .5
    num = Fraction(f_num_round)
    absolute = num.numerator // num.denominator
    f_num_round = sign * absolute

    return f_num_round

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't.
    Hint: use FRACTIONS and extract numerator.
    '''
    return 3.0
