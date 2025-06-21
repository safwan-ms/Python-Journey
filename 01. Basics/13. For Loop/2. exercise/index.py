# Challenge 1: Printing Numbers (1 to 10)
# Write a program that uses a for loop and range() to print the numbers from 1 to 10 (inclusive).

for i in range(1, 11):
    print(i)

# ------------------------------------

# Challenge 2: Counting Down (10 to 1)
# Write a program that uses a for loop and range() to print the numbers from 10 down to 1 (in descending order).

for i in range(10, 0, -1):
    print(i)

# ------------------------------------


# Challenge 3: Even Numbers Only (1 to 10)
# Write a program that uses a for loop and range() to print only the even numbers between 1 and 10 (inclusive). (Hint: use the modulo operator % to check for evenness).

for i in range(0, 11, 2):
    print(i)

# ------------------------------------

# Challenge 4: Sum of Numbers (1 to 100)
# Write a program that uses a for loop and range() to calculate the sum of all numbers from 1 to 100 (inclusive).
total = 0

for i in range(1, 101):
    total += i
    print(total)

# ------------------------------------
