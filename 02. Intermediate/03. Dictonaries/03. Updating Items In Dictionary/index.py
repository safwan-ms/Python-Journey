# Adding a New-Value Pair
my_dict = {"name": "John", "age": 25}
my_dict["city"] = "New York"
print(my_dict)

# Modifying Existing Value
my_dict = {"name": "John", "age": 25}
my_dict["age"] = 28
print(my_dict)

# Updating with Another Dictionary
my_dict = {"name": "John", "age": 25}
update_dict = {"age": 26, "city": "New York"}
my_dict.update(update_dict)
print(my_dict)

# Updating with Keyword Arguments
my_dict = {"name": "John", "age": 25}
my_dict.update(age=20, city="New York")
print(my_dict)


# Using setdefault() to Add Default Values
my_dict = {"name": "John", "age": 25}
my_dict.setdefault("city", "New York")
print(my_dict)
