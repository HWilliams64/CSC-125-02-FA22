sys.path.insert(0, '..')
from sept_22 import default_value
from python_file import function as py_function
from typing import Union
import sys

from py_module.default_value import sub_mod_function

default_value.default_value(2)


def add_stuff(x: Union[int, str], y: Union[int, str]) -> int:
    """
    Add x and y together and returns the sum.

    if x or y is a string then this will attempt to convert the string to a
    number then use the number form in the math operation.

    Args:
        x (int, str): This is a integer or the string form of an integer
        y (int, str): This is a integer or the string form of an integer

    Returns:
        int: The summation of x and y as numbers
    """

    # this will check if x is a string and if its a string with a number in it
    if isinstance(x, str) and x.isdigit():
        # This will convert the string to a integer
        x = int(x)

    if isinstance(y, str) and y.isdigit():
        y = int(y)

    return x + y


#print(add_stuff("1", "2"))
#print(add_stuff(1, 2))
