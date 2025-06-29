# --------------------------
add = lambda x, y: x + y
result = add(3, 5)
print(result)
# --------------------------


# --------------------------
# Function that takes another function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)


# Example of using a lambda function as an argument
result_addition = apply_operation(2, 5, lambda a, b: a + b)


result_subtract = apply_operation(2, 3, lambda a, b: a - b)
print(result_subtract)
# --------------------------
