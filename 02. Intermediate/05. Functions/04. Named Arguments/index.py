# ----------------------------
# Example 1
def display_info(name, age, city):
    """Display information about a person."""
    print("Name: ", name)
    print("Age: ", age)
    print("City: ", city)


# Using keyword arguments to call the function
display_info(name="Safwax", age=20, city="Japan")

# ----------------------------


# ----------------------------
# Example 2
def calculate_rectangle(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area


area_result = calculate_rectangle(length=2, width=4)
print("Rectangle Area: ", area_result)
# ----------------------------
