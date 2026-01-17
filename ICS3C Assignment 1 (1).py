"""
===============================================
Assignment 1 – Python Programming
Student Name: Ethan Knelsen
Date: 10/31/2025

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

# =======================================================
# Question 1: Say Hello
# Write a program that asks the user for their name
# and prints: Hello, <name>!
# =======================================================

# --- Put your code here ---
name = (input("your name: "))
print (f"hello,{name}")
# =======================================================
# Question 2: Adding Numbers
# Ask the user to enter two numbers. Add them together
# and print the result.
# =======================================================

# --- Put your code here ---
num_1 = int(input("number 1: "))
num_2 = int(input("number 2: "))
print(num_1 + num_2)
# =======================================================
# Question 3: Average of Three Numbers
# Ask the user to enter three numbers. Calculate the
# average and print it.
# =======================================================

# --- Put your code here ---
num_3 = int(input("number 1: "))
num_4 = int(input("number 2: "))
num_5 = int(input("number 3: "))
av = (num_3 + num_4 + num_5) / 3
print("The average is:", av) 
# =======================================================
# Question 4: Pizza Shop – Calculate Tax
# Ask the user to enter the total cost of their order.
# Calculate 13% tax and print the total amount including tax.
# ===============

# --- Put your code here ---
price = int(input("total price: $"))
tax = 0.13
total = price + (price * tax )
print("Total with tax: ${:.2f}".format(total))
# =======================================================
# Question 6: Tip Calculator
# Ask the user to enter the total bill amount at a restaurant.
# Ask the user to enter a tip percentage (e.g., 15 for 15%).
# Calculate the tip amount and the total bill including tip.
# Print both values clearly.
# =======================================================

# --- Put your code here ---
price_2 = int(input("price "))
tip = float(input("add tip use decimals like 0.13: "))
total_2 = price_2 + (price_2 * tip)
print (total_2)
