# Session 2 assignment of EPAi2.0

This is the README for the EPAi2.0 Assignment. 

Name: Suman Debnath 

In this assignment we had lots of tests around "Object Mutability & Interning"

The pytest contains total 9 tests:

- `test_clear_memory()` - Which tests for the memory leak 
- `test_memory_actually_increased()` - This test will check whether we are actually increase the memory during running the function f
- `test_performance()` - This test compares the performance between two different functions "compare_strings_old()" and "compare_strings_new()" to compare 2 long string if they are identically or not, along with a membership test of a character in the whole string 
- `test_readme_exists()` - This tests if README file exists or not 
- `test_readme_contents()` - This tests if this README file contains min of 500 words or not :) 
- `test_readme_proper_description()` - This tests certian specific things present or not in the README file
- `test_readme_file_for_formatting()` - This checks the minimum no. of times "#" is used in the doc 
- `test_class_repr()` - This checks for `__rep__()` implementation in the class definition of the classes `Something` and `SomethingNew` 
- `test_indentations()` - Checks for four spaces at each level of syntactically significant indenting
- `test_function_name_had_cap_letter()` - Checks if any function name contains an capital letter or not

Few of the functions/classes mentioned are: 

##Something

This `class` was just an dummy class, which had one parameter `something_new` under `__init__`, which is the constructor method inside the class definition.

##SomethingNew

This is also a `class` which holds two attributes, one as an integer and nother an object under `__init__`, which is the constructor method inside the class definition. 

##add_something()

This is a `function`, it create an instance of class Something() and it initiates "something_new" attribute of Something() instance to an instance of SomethingNew()

- collection : Its an empty list() object

##clear_memory()

This is a `function`, which simply removes all the elements in the collection, like list, 

##critical_function()

This is the function which creates cyclic reference between the instances 
It also runs for 1024*128 times in loop and after creating the cyclic references, it removes all the elements from the collection  and later it runs GC collect to clear the memory to avoid memory leak. 


##compare_strings_old()

A simple function which compares a long string with another string(both are same) 
It compairs using `equality` logic, and hence its very slow 
It also check the membership of a character in the string as well

##compare_strings_new()

This function is a better and more optimized version of the function `compare_strings_old`
Here the comparision is done via `is` operater which uses id() of the object 
Also for membership test it uses `set()` in place of `list()` which is more efficient and fast

- sleep : It was a dummy call to mimic slowness
- char_list : It just converts a string to a list of character

## Changes made in the solution in the file `session2.py`

- Added the ``__repr__`` function in both the class, Something and SomethingNew
- In the function `critical_function()` added these two lines  : 
    - collection = None 
    - gc.collect()
- Edited the function `compare_strings_new()`, 
    - Used set() in place of list() for storing the characters in the string
    - Used only 1 `for` loop 
    - Used `is` operator in place of `==` 
