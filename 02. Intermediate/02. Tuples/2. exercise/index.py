# Challenge 1: Creating Tuples

# Using parentheses (): Create a tuple containing your favorite foods.
# Using the tuple() function: Create a tuple from a list (e.g., tuple(["apple", "banana", "cherry"])).
favorite_foods = ["apple", "banana", "cherry"]
fruits_tuple = tuple(favorite_foods)
print("Fruits tuple: ", fruits_tuple)

# Challenge 2: Accessing Tuple Elements

# Create a tuple containing different data types (string, number, boolean).
# Access elements using their index (just like with lists).
student_tuple = ("Safwax", 20, False)
print(student_tuple[0])


# Challenge 3: Immutability of Tuples

# Try to modify an element in a tuple using indexing and assignment (e.g., my_tuple[0] = "new value").
# Observe the error message that you'll get since tuples are immutable (unchangeable).
my_tuple = ("apple", "banana", "cherry")
my_tuple[0] = "grape"  # Try changing the first item


# Challenge 4: Unpacking Tuples

# Create a tuple with student information (name, age, grade).
# Use tuple unpacking to assign these values to separate variables.

student_report = ("Safwax", 20, "A++")
name, age, grade = student_report
print(name)
print(age)
print(grade)
