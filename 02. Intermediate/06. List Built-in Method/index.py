# append
my_list = [1, 2, 3]
my_list.append(6)
print(my_list)


# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)

# insert
my_list = [1, 2, 3]
my_list.insert(1, 3)
print(my_list)

# remove(element) this is based on nth item
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)

# pop(index) this is based on index
my_list = [1, 2, 3]
my_list.pop(2)
print(my_list)

# copy
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)
