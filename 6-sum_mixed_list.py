#!/usr/bin/env python3
from typing import List, Union  # Importing List and Union from typing

# The 'sum_mixed_list' function takes a list containing both integers and floats,
# and returns their sum as a float.
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)  # Adds up all elements in the list, whether they are integers or floats
