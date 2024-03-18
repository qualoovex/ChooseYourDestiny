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

def forest_path(options):
    print("You start walking along the forest path.")
    time.sleep(1)
    print("As you venture deeper into the forest, you encounter various options:")
    time.sleep(1)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input(f"Enter your choice (1-{len(options)}): ")
    choice_index = int(choice) - 1
    if 0 <= choice_index < len(options):
        chosen_option = options.pop(choice_index)
        print(f"\nYou choose to {chosen_option}.")
        time.sleep(1)
        if chosen_option == "follow the sparkling stream":
            follow_stream()
        elif chosen_option == "investigate the mysterious glow in the distance":
            investigate_glow()
        elif chosen_option == "enter the hidden cave behind the waterfall":
            enter_cave()
        elif chosen_option == "feel the magical presence in the air":
            feel_magical_presence()
    else:
        print("\nInvalid choice. Please enter a valid option.\n")
        forest_path(options)

def follow_stream():
    print("\nYou follow the sparkling stream, mesmerized by its beauty.")
    time.sleep(1)
    print("As you walk, you notice colorful flowers and playful butterflies.")
    time.sleep(1)
    print("The stream leads you to a tranquil clearing with a magical fountain.")
    time.sleep(1)
    print("You take a moment to rest and refresh yourself, drinking from the fountain.")
    time.sleep(1)
    print("Feeling rejuvenated, you continue on your quest.\n")
    time.sleep(1)

def investigate_glow():
    print("\nYou decide to investigate the mysterious glow in the distance.")
    time.sleep(1)
    print("As you approach, you realize the glow is coming from a cluster of enchanted fireflies.")
    time.sleep(1)
    print("The fireflies lead you to a hidden grove filled with mystical flowers.")
    time.sleep(1)
    print("You feel a sense of tranquility and wonder in the grove.")
    time.sleep(1)
    print("You spend some time exploring before continuing your journey.\n")
    time.sleep(1)

def enter_cave():
    print("\nYou bravely enter the hidden cave behind the waterfall.")
    time.sleep(1)
    print("Inside, you find yourself in a chamber filled with shimmering crystals.")
    time.sleep(1)
    print("The crystals emit a soft, soothing light that illuminates the cave.")
    time.sleep(1)
    print("You feel a sense of calm and wonder as you explore the cave.")
    time.sleep(1)
    print("After some time, you emerge from the cave, feeling refreshed and invigorated.\n")
    time.sleep(1)

def feel_magical_presence():
    print("\nYou close your eyes and focus on the magical presence in the air.")
    time.sleep(1)
    print("You feel a connection to the ancient spirits of the forest.")
    time.sleep(1)
    print("They guide you through the forest, leading you to hidden wonders.")
    time.sleep(1)
    print("You spend hours wandering through the forest, filled with a sense of peace and wonder.")
    time.sleep(1)
    print("As the sun begins to set, you emerge from the forest, grateful for the magical experience.\n")
    time.sleep(1)

def main():
    intro()
    options = [
        "follow the sparkling stream",
        "investigate the mysterious glow in the distance",
        "enter the hidden cave behind the waterfall",
        "feel the magical presence in the air"
    ]
    while options:
        forest_path(options)

if __name__ == "__main__":
    main()
