"""
NumPy Array Slicing Guide
-------------------------

This file demonstrates how slicing works in NumPy arrays.

Syntax:
    array[start:end:step]

Rules:
- start → inclusive
- end   → exclusive
- step  → jump interval
"""

import numpy as np


# --------------------------------------------------
# Create 2D Array
# --------------------------------------------------
array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Original Array:\n", array)


# --------------------------------------------------
# Row Slicing
# --------------------------------------------------

# Select rows from index 2 onwards
print("\nRows from index 2:")
print(array[2:])


# --------------------------------------------------
# Column Selection
# --------------------------------------------------

# First column
print("\nFirst column:")
print(array[:, 0])

# Last column
print("\nLast column:")
print(array[:, -1])


# --------------------------------------------------
# Step Slicing
# --------------------------------------------------

# Every 2nd row
print("\nEvery 2nd row:")
print(array[::2])

# Reverse rows
print("\nReversed array:")
print(array[::-1])


# --------------------------------------------------
# Sub-matrix Extraction
# --------------------------------------------------

# Bottom-left block
print("\nBottom-left submatrix:")
print(array[2:, 0:2])

# Bottom-right block
print("\nBottom-right submatrix:")
print(array[2:, 2:4])