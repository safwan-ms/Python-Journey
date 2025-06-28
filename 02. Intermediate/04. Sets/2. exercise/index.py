# Challenge 1: Creating Sets

# Using curly braces {}: Create a set of your favorite hobbies.
# Using the set() function: Create a set from a list containing duplicate elements (e.g., set([1, 1, 2, 3]) will remove duplicates).

hobbies = {"eat", "sleep", "code", "code", "code", "repeat"}
print("My hobbies set:", hobbies)

# Challenge 2: Set Membership and Checking for Uniqueness

# Create a set of numbers.
# Check if a specific number is present in the set using the in operator.
# Try adding a duplicate element to the set and observe that it's not included (sets cannot have duplicates).

fruits = {"apple", "banana", "mango", "orange"}

print("banana" in fruits)
print("grape" in fruits)
# Challenge 3: Set Operations: Union, Intersection, Difference

# Create two sets: one representing movies you've watched and another representing your friend's watched movies.
# Use the following set operations to find:
# Union: The movies watched by either you or your friend.
# Intersection: The movies you both have watched.
# Difference: The movies you've watched that your friend hasn't and vice versa (use appropriate methods like union(), intersection(), and difference()).
my_movies = {"Inception", "Interstellar", "The Dark Knight", "Avatar", "Titanic"}
friends_movies = {"The Dark Knight", "Avengers", "Titanic", "Joker", "Spider-Man"}
union = my_movies.union(friends_movies)
print("Union =", union)

intersection = my_movies.intersection(friends_movies)
print("Intersection =", intersection)

difference = my_movies.difference(friends_movies)
print("Difference =", difference)

# Challenge 4: Adding and Removing Elements from Sets

# Create a set of fruits.
# Add a new fruit to the set using the add() method.
# Remove a specific fruit from the set using the remove() method.
# (Optional) Try removing an element that's not in the set using discard() (which won't cause an error).

fruits = {"apple", "banana", "mango", "orange"}
fruits.add("grape")
fruits.remove("apple")
fruits.discard("apple")
print(fruits)
