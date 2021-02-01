# Session 3 assignment of EPAi2.0

This is the README for the EPAi2.0 Assignment. 

Name: Suman Debnath 

In this assignment we had lots of tests around "Numeric Types", which covers Integers, Constructors, Bases, Rational Numbers, Floats, rounding, Coercing to Integers and equality

The pytest contains total 16 tests:

- `test_readme_exists()` - This test checks if the readme file exists or not
- `test_readme_contents()` - This tests if this README file contains min of 500 words or not :)
- `test_readme_proper_description()`- This tests certian specific things present or not in the README file
- `test_readme_file_for_formatting()` - This checks the minimum no. of times "#" is used in the doc
- `test_indentations()` - Returns pass if used four spaces for each level of syntactically significant indenting
- `test_function_name_had_cap_letter()` - Checks if any function name contains an capital letter or not
- `test_invalid_base_valueerror()` - Checks with some invalide base value to test the function `encoded_from_base10()`
- `test_invalid_base_valueerror_provides_relevant_message()` - Checks for the right ValueError exception when giving an invalid base
- `test_innacurate_digit_map_length()` - Checks for the right ValueError exception when giving an invalid digit_map
- `test_hexadecimal_conversions()` - Check for the function `encoded_from_base10()` to represent an 10 base positive number to a 16 base number
- `test_negative_hexadecimal_conversions()` - Check for the function `encoded_from_base10()` to represent an 10 base negative number to a 16 base number
- `test_repeating_digits_in_digit_map()` - Check for the function `encoded_from_base10()` to make sure the digit_map is correct and doesnt contain repitative alphanumerics
- `test_repeating_digits_valueerror_provides_relevant_message()` - Checks for the right ValueError exception when giving an invalid digit_maps
- `test_float_equality_testing()` - Checks for the floating point quality betweek 2 numbers. This is basically an implementation of `math.isclose()` method
- `test_things_not_allowed()` - Checks any non-allowed package/class usage in the code
- `test_fraction_used_or_not()` - Checks if the Fraction() class is used or not
- `test_manual_truncation_function()` - Check the truncation functionality 
- `test_manual_rounding_function()` - Check the found functionality 
- `test_functions_for_zero()` - Test with some corner case

Few of the functions/classes used in the solution are: 

## encoded_from_base10(number, base, digit_map)

This function represents a number in some given base from base10, it takes the number, base and digit_map as an argument
Some condition checks:
- ValueError("Given base must be more than equal to 2 and less than equal to 32")
- ValueError("Digit Map contains doesnt contain unique code ( repeating alphanumerics!!)")
- ValueError("digit_map is not enough for encoding")

No where in the code we used `math` modules or even the buildin functions like, `int()`, `bin()`, `hex()`, `round()`, and `truncation()` module. 

## float_equality_testing(a, b)

This function emulates the `isclose` method from the MATH module, but you can't use this function
We are going to assume:
- rel_tol = 1e-12 (relative tolerance)
- abs_tol = 1e-05 (absolute tolerance)

## manual_truncation_function(f_num)

This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point.
It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc. 

But we have not used the absolute build in functionality, in place of that we used Fraction() and the // operator to get the absolute value of a fraction/float

## manual_rounding_function(f_num)

This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but expected to write your one manually.

## rounding_away_from_zero(f_num)

This function implements rounding away from zero.
Desperately need to use INT constructor? Well you can't.
Hint: use FRACTIONS and extract numerator.

This function is not yet implemented. 