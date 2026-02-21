"""
=====================================================
NUMPY REFERENCE — LIST vs NUMPY ARRAY OPERATIONS
=====================================================

Concepts covered:

1. Python list multiplication behaviour
2. NumPy array element-wise operations
3. Type checking
"""

import numpy as np


# =====================================================
# SECTION 1 — PYTHON LIST BEHAVIOUR
# =====================================================

# Python list
my_list = [1, 2, 3, 4]

# Multiplying list duplicates elements (NOT math)
list_result = my_list * 2

print("Python List Result:", list_result)



# =====================================================
# SECTION 2 — NUMPY ARRAY BEHAVIOUR
# =====================================================

# NumPy array
array = np.array([1, 2, 3, 4])

# Element-wise multiplication
array_result = array * 2

print("NumPy Array Result:", array_result)



# =====================================================
# SECTION 3 — TYPE CHECKING
# =====================================================

print("Type of array:", type(array))