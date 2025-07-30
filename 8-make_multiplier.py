#!/usr/bin/env python3
from typing import Callable  # Importing Callable from typing

# The 'make_multiplier' function takes a multiplier (float) and returns a function
# that multiplies a float by the multiplier.
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    # Inner function that performs the multiplication
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func  # Returns the inner multiplier_func function
