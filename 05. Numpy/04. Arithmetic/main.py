"""
NumPy Arithmetic & Vectorized Operations
----------------------------------------

This module demonstrates:

1. Scalar arithmetic
2. Vectorized math functions
3. Element-wise operations
4. Comparison & boolean masking

Key Idea:
NumPy performs operations element-wise without loops.
"""

import numpy as np


# --------------------------------------------------
# Scalar Arithmetic (Broadcasting)
# --------------------------------------------------
array = np.array([1, 2, 3])

print("Scalar Arithmetic:")
print("Add 1:", array + 1)
print("Multiply by 3:", array * 3)
print("Power:", array ** 2)


# --------------------------------------------------
# Vectorized Math Functions
# --------------------------------------------------
decimal_array = np.array([1.01, 2.5, 3.99])

print("\nVectorized Math Functions:")
print("Square root:", np.sqrt(decimal_array))
print("Round:", np.round(decimal_array))
print("Floor:", np.floor(decimal_array))


# Example: Area of circles
radii = np.array([1, 2, 3])
areas = np.pi * radii**2

print("\nCircle Areas:", areas)


# --------------------------------------------------
# Element-wise Arithmetic
# --------------------------------------------------
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("\nElement-wise Operations:")
print("Addition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)


# --------------------------------------------------
# Comparison Operators & Boolean Masking
# --------------------------------------------------
scores = np.array([91, 55, 100, 73, 82, 64])

print("\nStudents Passed (>=60):")
print(scores >= 60)

# Replace failing scores with 0
scores[scores < 60] = 0

print("\nUpdated Scores:")
print(scores)