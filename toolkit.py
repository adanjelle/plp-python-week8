
# PLP Python Week 8
# Python Toolkit

import random

# Welcome message
print("=================================")
print("       WELCOME TO PYTHON TOOLKIT")
print("=================================")


# Tool 1: Simple Calculator
# Performs addition, subtraction, multiplication and division.

def simple_calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"The result is: {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"The result is: {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"The result is: {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"The result is: {result}")
            else:
                print("Error: Division by zero is not allowed.")

        else:
            print("Invalid operation. Please choose between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


# Tool 2: To-Do List Manager
# Allows users to add, view and remove tasks.

def todo_manager():
    tasks = []

    while True:
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Back to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your task: ")

            if task.strip():
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Please enter a valid task.")

        elif choice == "2":
            if tasks:
                print("\nYour tasks:")

                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("Your to-do list is empty.")

        elif choice == "3":
            task = input("Enter the task to remove: ")

            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' removed successfully!")
            else:
                print("That task is not on your list.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print(f"Sorry, '{choice}' is not a valid option.")


# Tool 3: Number Guessing Game
# Generates a random number and lets the user guess it.

def number_guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")
    print("I have selected a number between 1 and 10.")

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")

            elif guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You guessed the number {secret_number}.")
                print(f"You got it in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Main menu loop
while True:
    print("\n=================================")
    print("          PYTHON TOOLKIT")
    print("=================================")
    print("1. Simple Calculator")
    print("2. To-Do List Manager")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        simple_calculator()

    elif choice == "2":
        todo_manager()

    elif choice == "3":
        number_guessing_game()

    elif choice == "4":
        print("\nThank you for using Python Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
