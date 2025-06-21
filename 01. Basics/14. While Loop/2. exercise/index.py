# **1. Guessing Game**

# - **Challenge:** Develop a program that lets a user guess a secret number.
# - **Functionality:**
#   - Define a secret number (or store it in a variable).
#   - Use a `while` loop to repeatedly prompt the user for guesses.
#   - Inside the loop:
#     - Check if the guess is too high, too low, or correct.
#     - Provide feedback to the user based on their guess.
#   - When the guess is correct, print a congratulatory message.
import random

secret_number = random.randint(1, 10)
guess = None

while guess != secret_number:
    guess = int(input("Guess the secret number: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif abs(guess - secret_number) == 1:
        print("So close! You are just 1 number away. Try again!")
    elif guess > secret_number:
        print("Too high! Try again.")


print("🎉 Congratulations! You guessed the correct number.")

# **2. Menu-Driven Program (While Loop Version)**

# - **Challenge:** Rewrite the menu-driven program using a `while` loop.
# - **Functionality:**
#   - Create a loop that continues until the user chooses to exit.
#   - Inside the loop:
#     - Display a menu with options (e.g., add, subtract, exit).
#     - Use `if` statements to handle different menu options and perform the corresponding actions (add, subtract, etc.).
while True:
    print("\n--- Simple Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")
    choice.lower()

    if choice == "1":
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print("Result: ", num1 + num2)

    elif choice == "2":
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print("Result: ", num1 + num2)

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


# **3. Countdown Timer**

# - **Challenge:** Create a program that simulates a countdown timer.
# - **Functionality:**
#   - Prompt the user to enter a starting time in seconds.
#   - Use a `while` loop with a counter variable.
#   - Inside the loop:
#     - Decrement the counter variable by 1 (simulating one second passing).
#     - Print the remaining time.
#   - Once the counter reaches 0, print a message like "Time's up!"

# **Note:** Functionality like `time.sleep(1)` might not be available in all environments.
import time

seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    print("Time left: ", seconds, "seconds")
    time.sleep(1)
    seconds -= 1
print("⏰ Time's up!")
