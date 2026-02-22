"""
=====================================================
NUMPY REFERENCE — ARRAY DIMENSIONS & INDEXING
=====================================================

This file demonstrates:

1. Array dimensions (0D → 3D+)
2. Shape property
3. Indexing methods
4. Multi-dimensional access
5. Example word construction from indexing

-----------------------------------------------------
"""

import numpy as np


# =====================================================
# SECTION 1 — ARRAY DIMENSIONS
# =====================================================

# ---------- 0D ARRAY (Scalar) ----------
array_0d = np.array('A')
print("0D array ndim:", array_0d.ndim)


# ---------- 1D ARRAY ----------
array_1d = np.array(['A', 'B', 'C'])
print("1D array ndim:", array_1d.ndim)


# ---------- 2D ARRAY ----------
array_2d = np.array([
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'F']
])
print("2D array ndim:", array_2d.ndim)


# ---------- 3D ARRAY ----------
array_3d = np.array([[
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'F']
]])
print("3D array ndim:", array_3d.ndim)



# =====================================================
# SECTION 2 — HIGHER DIMENSION ARRAY
# =====================================================

array_4d = np.array([[

    [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ],

    [
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R']
    ],

    [
        ['S', 'T', 'U'],
        ['V', 'W', 'X'],
        ['Y', 'Z', ' ']
    ]

]])

print("\nShape of array:", array_4d.shape)



# =====================================================
# SECTION 3 — INDEXING METHODS
# =====================================================

# Traditional indexing
print("\nTraditional indexing:", array_4d[0][0][0][0])

# Comma-separated indexing (Recommended)
print("Comma indexing:", array_4d[0, 0, 0, 2])



# =====================================================
# SECTION 4 — INDEXING EXAMPLE (WORD BUILDING)
# =====================================================

word = (
    array_4d[0,2,0,0] +
    array_4d[0,0,0,0] +
    array_4d[0,0,1,2] +
    array_4d[0,2,1,1] +
    array_4d[0,0,0,0] +
    array_4d[0,1,1,1]
)

print("\nConstructed word:", word)