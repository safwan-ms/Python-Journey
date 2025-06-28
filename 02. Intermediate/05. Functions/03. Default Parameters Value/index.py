# ----------------------
# Example 1
def greet_person(name, greeting="Hello"):
    """This function greets a person with a specified greeting (default is Hello)."""
    print(f"{greeting}, {name}!")


greet_person("Safwax")
greet_person("Irfax", "Hi there")
# ----------------------


# ----------------------
# Example 2
def print_message(message, num_exclamatory_mark=3):
    print(message + "!" * num_exclamatory_mark)


# Calling the function with different arguments
print_message("Hello")  # Prints "Hello!!!"
print_message("Hi there", 5)  # Prints "Hi there!!!!!"
print_message("Greetings", 10)
# --------------------------------------
