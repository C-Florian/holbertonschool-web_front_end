#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple  # Importing necessary types

# The 'element_length' function takes an iterable of sequences (e.g., strings or lists),
# and returns a list of tuples containing each sequence and its length.
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]  # Returns a list of tuples with each element and its length
