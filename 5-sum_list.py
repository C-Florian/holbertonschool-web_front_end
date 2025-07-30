#!/usr/bin/env python3
from typing import List  # Importing List from typing to annotate lists

# The 'sum_list' function takes a list of floats and returns their sum as a float.
def sum_list(input_list: List[float]) -> float:
    return sum(input_list)  # Uses the sum function to add up all elements in the list
