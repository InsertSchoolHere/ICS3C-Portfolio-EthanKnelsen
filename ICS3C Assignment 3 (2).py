"""
===============================================
Assignment – 3
Student Name: 
Date: 

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

# =======================================================
# Task 1: Blast Off!
# 
# Write a program that asks the user for a number to count up to,
# and also asks how much to count by each time (the step size).
# The program should use a for loop to display the count on
# separate lines and end by printing "Blast off!".
#
# Program Requirements:
#   1. Ask the user for a number to count up to.
#   2. Ask the user for a step amount.
#   3. Use a for loop to count up by that step amount
#      until you reach that number or above.
#   4. Display each number on a new line.
#   5. When the count is finished, print "Blast off!".
#
# Example Output:
#   Enter a number to count up to: 20
#   Enter a step amount: 5
#   0
#   5
#   10
#   15
#   20
#   Blast off!
# =======================================================

# --- Put your code here ---
try:
    num = int(input("choose a number: "))
    step_num = int(input("choose a step number: "))
    for i in range(0, num, step_num):
        print(i)
except ValueError: 
    print("Invalid input. Please enter a valid number when you try again.")



# =======================================================
# Task 2: Number Guessing Game
#
# Write a program that asks the user to guess a secret number
# between 1 and 10. You can hardcode the secret number
# (e.g., secret_number = 7).
#
# Program Requirements:
#   1. Use a while loop to let the user keep guessing until
#      they get it right.
#   2. If the guess is too low, display "Too low! Try again."
#      If the guess is too high, display "Too high! Try again."
#   3. When they guess correctly, display a congratulations message.
#
# Example Output:
#   I'm thinking of a number between 1 and 10.
#   Enter your guess: 5
#   Too low! Try again.
#   Enter your guess: 9
#   Too high! Try again.
#   Enter your guess: 7
#   You got it! The secret number was 7.
# =======================================================

# --- Put your code here ---
try:
    secret_number = 7

    guess = 0          
    guess_count = 0   


    while guess != secret_number:
    
        guess = int(input("Guess a number between 1 and 10: "))   
        guess_count += 1  


        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {guess_count} tries!")
except ValueError: 
    print("Invalid input. Please enter a valid number when you try again.")
