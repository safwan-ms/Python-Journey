#  Empty Dictionaries
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

# Dictionary with Key-Value Pairs
student_info = {"name": "Alice", "age": 20, "grade": "A"}
print(student_info)  # {'name': 'Alice', 'age': 20, 'grade': 'A'}
print(type(student_info))  # <class 'dict'>
print(len(student_info))  # 3

# Using the dict() Constructor
person = dict(name="Safwax", age=20, city="Japan")
print(person)  # {'name': 'Safwax', 'age': 20, 'city': 'Japan'}

# Dictionary with different data types
mixed_dict = {"name": "Charlie", "age": 30, "grades": [85, 69, 89], "is_student": True}
print(mixed_dict)
# {'name': 'Charlie', 'age': 30, 'grades': [85, 69, 89], 'is_student': True}


# Nested Dictionary
nested_dict = {
    "person": {"name": "David", "age": 22},
    "location": {"city": "Paris", "country": "France"},
}
print(nested_dict)
# {'person': {'name': 'David', 'age': 22}, 'location': {'city': 'Paris', 'country': 'France'}}


#  Using a List of Tuples
tuple_list = [("name", "Eva"), ("age", 28), ("city", "Berlin")]
from_tuples_dict = dict(tuple_list)
print(from_tuples_dict)
# {'name': 'Eva', 'age': 28, 'city': 'Berlin'}
