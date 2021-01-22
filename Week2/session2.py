# KINDLY GO THROUGH TEST FILE TO UNDERSTAND
from typing import List
import time
import gc 
import sys

# Here in this code we will be leaking memory because we are creating cyclic reference.
# Find that we are indeed making cyclic references.
# Eventually memory will be released, but that is currently not happening immediately.
# We have added a function called "clear_memory" but it is not able to do it's job. Fix it.
# Refer to test_clear_memory Test in test_session2.py to see how we're crudely finding that
# this code is sub-optimal.
class Something(object):

    def __init__(self):
        super().__init__()
        self.something_new = None

    def __repr__(self):
        return f"object located at: {hex(id(self))}"


class SomethingNew(object):

    def __init__(self, i: int = 0, something: Something = None):
        super().__init__()
        self.i = i
        self.something = something

    def __repr__(self):
        return f"object located at : {hex(id(self))}"

def add_something(collection: List[Something], i: int):
    '''
    This create an instance of class Something() and it initiates 
    "something_new" attribute of Something() instance to an instance of SomethingNew()
    '''
    something = Something()
    something.something_new = SomethingNew(i, something)
    collection.append(something)

def reserved_function():
    # to be used in future if required
    pass

def clear_memory(collection: List[Something]):
    '''
    This function, simply removes all the elements in the collection, like list 
    '''
    collection.clear()


def critical_function():
    '''
    This is the function which creates cyclic reference between the instances 
    It also runs for 1024*128 times in loop and after creating the cyclic references,
    it removes all the elements from the collection 
    and later it runs GC collect to clear the memory to avoid memory leak 
    '''
    collection = list()
    for i in range(1, 1024 * 128):
        add_something(collection, i) 
    clear_memory(collection)
    # Added these following two lines 
    collection = None 
    gc.collect()


# Here we are suboptimally testing whether two strings are exactly same or not
# After that we are trying to see if we have a particular character in that string or not
# Currently the code is suboptimal. Write it in such a way that it takes 1/10 the current time

# DO NOT CHANGE THIS PROGRAM
def compare_strings_old(n):
    '''
    A simple function which compares a long string with another string(both are same) 
    It compairs using `equality` logic, and hence its very slow 
    It also check the membership of a character in the string as well
    '''
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a == b:
            pass
    char_list = list(a)
    for i in range(n):
        if 'd' in char_list:
            pass

# YOU NEED TO CHANGE THIS PROGRAM
def compare_strings_new(n):
    '''
    This function is a better and more optimized version of the function `compare_strings_old`
    Here the comparision is done via `is` operater which uses id() of the object 
    Also for membership test it uses `set()` in place of `list()` which is more efficient and fast
    '''
    a = sys.intern('a long string that is not intered' * 200)
    b = sys.intern('a long string that is not intered' * 200)

    char_set = set(a)

    for i in range(n):
        if a is b:
            pass
        if 'd' in char_set:
            pass