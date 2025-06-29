def outer_function(x):
    """Outer function with a nested function."""

    def inner_function(y):
        return x + y

    result = inner_function(5)
    return result


# Calling the outer function
result_value = outer_function(10)
print(result_value)
