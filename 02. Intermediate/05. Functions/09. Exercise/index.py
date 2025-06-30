# **1. Basic Function with Parameters**

# - **Challenge:** Write a function that takes two numbers (`a` and `b`) as parameters and returns their sum. Call the function with different numeric arguments to test it.


def add(a, b):
    return a + b


result = add(3, 5)
print(result)

# **2. Default Parameter Values**


# - **Challenge:** Modify the function from Challenge 1 to have a default value for the second parameter (`b`) in case it's not provided during the function call. Set the default value to 10. Call the function with one and two arguments to see how the default value works.
def add(a, b=10):
    return a + b


result = add(3)
print(result)

# **3. Named Arguments**


# - **Challenge:** Write a function that calculates the area of a rectangle. It should take two parameters for width and height. Call the function with the arguments named appropriately (e.g., `area(width=5, height=10)`) to demonstrate named arguments.
def area(width, height):
    return width * height


result = area(width=5, height=10)

print("Area of the rectangle:", result)


# **4. Docstrings and Return Statements**


# - **Challenge:** Add a docstring to the function explaining its purpose and parameters. Ensure the function returns the calculated value using a return statement.
def area(width, height):
    return width * height

    """
    Calculate the area of a rectangle.

    Parameters:
    width (int or float): The width of the rectangle.
    height (int or float): The height of the rectangle.

    Returns:
    int or float: The area of the rectangle.
    """


result = area(width=5, height=10)
print("Area of the rectangle:", result)

# **5. Nested Functions**

# - **Challenge:** Write a function that calculates the factorial of a number (factorial of a number is the product of all positive integers less than or equal to that number). Define another function within the first function (nested function) to perform the factorial calculation recursively. The outer function can call the nested function and return the result.


# ** (Implementation for nested functions requires additional coding) **
def calculate_factorial(n):
    """
    Calculate the factorial of a number using a nested recursive function.

    Parameters:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of the number.
    """

    def factorial_recursive(x):
        # Base case
        if x == 0 or x == 1:
            return 1
        return x * factorial_recursive(x - 1)

    return factorial_recursive(n)


result = calculate_factorial(5)
print("Factorial of 5 is:", result)

# **6. Lambda Functions (Bonus Challenge)**

# - **Challenge:** Explore lambda functions as a concise way to write anonymous functions for simple operations. Write a program that uses a lambda function to calculate the square of a number.
square = lambda x: x**2

result = square(6)
print("Square of 6 is:", result)
