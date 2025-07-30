#!/usr/bin/env python3
from typing import Union, Tuple  # Importing Union and Tuple from typing

# The 'to_kv' function takes a string and an int or float, and returns a tuple.
# The first element is the string, and the second is the square of the number as a float.
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v ** 2)  # Returns a tuple with k and the square of v
