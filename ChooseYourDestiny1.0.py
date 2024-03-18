#Programmer: Julian G
# date: 3/15/24
#Program: Choose Your Destiny
import time
import random

def intro():
    print("Welcome to the Fairy Fantasy Adventure!")
    print("You find yourself in the enchanted forest of Eldoria.")
    print("Your quest is to retrieve the lost Crystal of Power.")
    print("Your journey begins here...\n")
    time.sleep(1)

def forest_path():
    print("You start walking along the forest path.")
    time.sleep(1)
    print("As you venture deeper into the forest, you encounter various options:")
    time.sleep(1)
    print("1. Follow the sparkling stream.")
    print("2. Investigate the mysterious glow in the distance.")
    print("3. Enter the hidden cave behind the waterfall.")
    print("4. Feel the magical presence in the air.")
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    if choice == "1":
        follow_stream()
    elif choice == "2":
        investigate_glow()
    elif choice == "3":
        enter_cave()
    elif choice == "4":
        feel_magical_presence()
    else:
        print("\nInvalid choice. Please enter 1, 2, 3, or 4.\n")
        forest_path()

def follow_stream():
    print("\nYou follow the sparkling stream, mesmerized by its beauty.")
    time.sleep(1)
    print("The stream leads you to a tranquil clearing with a magical fountain.")
    time.sleep(1)
    print("You take a moment to rest and refresh yourself.")
    time.sleep(1)
    print("Feeling rejuvenated, you continue on your quest.\n")
    time.sleep(1)
    forest_path()

def investigate_glow():
    print("\nYou decide to investigate the mysterious glow in the distance.")
    time.sleep(1)
    print("As you approach, you discover a field of glowing fireflies.")
    time.sleep(1)
    print("Their soft light guides your path through the forest.")
    time.sleep(1)
    print("You feel a sense of peace and wonder as you follow the fireflies.")
    time.sleep(1)
    print("You emerge from the forest feeling inspired and ready to continue your journey.\n")
    time.sleep(1)
    forest_path()

def enter_cave():
    print("\nYou bravely enter the hidden cave behind the waterfall.")
    time.sleep(1)
    print("Inside, you find a treasure chest filled with sparkling gems.")
    time.sleep(1)
    print("You also discover ancient cave paintings depicting mythical creatures.")
    time.sleep(1)
    print("Although tempted to stay, you know your true quest lies elsewhere.")
    time.sleep(1)
    print("You leave the cave, carrying the memory of its wonders with you.\n")
    time.sleep(1)
    forest_path()

def feel_magical_presence():
    print("\nYou close your eyes and focus on the magical presence in the air.")
    time.sleep(1)
    print("You sense a connection to the ancient spirits of the forest.")
    time.sleep(1)
    print("They offer you guidance and protection on your journey.")
    time.sleep(1)
    print("Filled with newfound strength, you forge ahead with confidence.\n")
    time.sleep(1)
    forest_path()

def main():
    intro()
    forest_path()

if __name__ == "__main__":
    main()
