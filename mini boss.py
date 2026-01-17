"""
miniboss final project
"""




import random

# Define a list of healing items
healing_items = ["Potion", "Potion", "Potion"]

# Define the player's and boss's initial health
player_health = 100
boss_health = 150

# Function to display the player's and boss's current health
def display_health(player, boss):
    print(f"Your health: {max(player, 0)}")
    print(f"Boss's health: {max(boss, 0)}")

# Main game loop
while player_health > 0 and boss_health > 0:
    print("\n1. Attack")
    print("2. Heal")
    print("3. Run")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        # Player attacks the boss with a 70% hit chance
        if random.random() < 0.7:  # 70% chance to hit
            boss_health -= 20
            print("You attacked the boss!")
        else:
            print("You missed the boss!")
    elif choice == "2":
        # Player heals themselves
        if not healing_items:  # Check if the list is empty
            print("You have no healing items left.")
            continue
        
        print("Available healing items (all heal 20 HP. can increase max HP.): ")
        for i, item in enumerate(healing_items):
            print(f"{i+1}. {item}")
        item_choice = input("Enter the number of the item to use: ")
        if item_choice.isdigit() and 1 <= int(item_choice) <= len(healing_items):
            player_health += 20  # Simple healing logic
            print(f"You used {healing_items[int(item_choice) - 1]}, You felt all your wounds disappear!")
            # Remove the used item from the list
            del healing_items[int(item_choice) - 1]
        else:
            print("Invalid choice, Try again.")
    elif choice == "3":
        print("You ran away but why? you were supposed to save the kingdom!")
        break
    else:
        print("Invalid choice, Try again.")

    # Boss attacks the player with a 60% hit chance
    if boss_health > 0:
        if random.random() < 0.6:  # 60% chance to hit
            player_health -= 15
            print("The boss attacked you!")
        else:
            print("The boss missed you!")

    # Display the current health
    display_health(player_health, boss_health)

# Game over logic
if player_health <= 0:
    player_health = 0
    print("You failed the kingdom, Try again!")
elif boss_health <= 0:
    boss_health = 0
    print("You beat the foul beast and saved the kingdom, congratulations!")
display_health(player_health, boss_health)
