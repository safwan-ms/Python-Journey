# -----------------------------
my_list = [1, 2, 3]

# Unpacking the list into variables a,b,c
a, b, c = my_list

print(a)
print(b)
print(c)

# -----------------------------

# -----------------------------
my_list = [1, 2, 3, 4, 5]
first, second, *rest = my_list
print(first)
print(second)
print(rest)
