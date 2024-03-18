import time
import random

class Adventure:
    def __init__(self):
        self.choices = []

    def add_choice(self, choice):
        self.choices.append(choice)

    def intro(self):
        print("Welcome to the Choose Your Own Adventure Game!")
        print("You find yourself standing at the edge of a mystical forest.")
        print("Your quest is to retrieve the ancient Crystal of Power.")
        print("Your adventure begins here...\n")
        time.sleep(1)

    def forest_path(self):
        available_options = [
            "Follow the sparkling stream.",
            "Investigate the mysterious glow in the distance.",
            "Enter the hidden cave behind the waterfall.",
            "Feel the magical presence in the air.",
            "End your adventure."
        ]

        while True:
            print("\nAs you venture deeper into the forest, you encounter various options:")
            time.sleep(1)
            for i, option in enumerate(available_options, 1):
                print(f"{i}. {option}")
            choice = input(f"Enter your choice (1-{len(available_options)}): ")
            try:
                choice_index = int(choice) - 1
                chosen_option = available_options[choice_index]
                if 0 <= choice_index < len(available_options):
                    self.add_choice(chosen_option)
                    available_options.pop(choice_index)
                    if chosen_option == "End your adventure.":
                        print("\nYour adventure in the enchanted forest ends here.")
                        break
                    else:
                        print(f"\nYou choose to {chosen_option}.")
                        time.sleep(1)
                        if chosen_option == "Follow the sparkling stream.":
                            self.follow_stream()
                        elif chosen_option == "Investigate the mysterious glow in the distance.":
                            self.investigate_glow()
                        elif chosen_option == "Enter the hidden cave behind the waterfall.":
                            self.enter_cave()
                        elif chosen_option == "Feel the magical presence in the air.":
                            self.feel_magical_presence()
                else:
                    print("\nInvalid choice. Please enter a valid option.\n")
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")

    def follow_stream(self):
        print("\nYou follow the sparkling stream, mesmerized by its beauty.")
        time.sleep(1)
        print("As you walk, you notice colorful flowers and playful butterflies.")
        time.sleep(1)
        print("Suddenly, you hear a soft melody coming from the trees.")
        time.sleep(1)
        print("You follow the sound and discover a group of friendly forest creatures dancing.")
        time.sleep(1)
        print("They invite you to join them, and you spend a joyful afternoon dancing and laughing.")
        time.sleep(1)
        print("As the sun sets, the creatures bid you farewell, and you continue on your quest.")

    def investigate_glow(self):
        print("\nYou decide to investigate the mysterious glow in the distance.")
        time.sleep(1)
        print("As you approach, you realize the glow is coming from a magical portal.")
        time.sleep(1)
        print("You hesitate for a moment, unsure of what lies beyond.")
        time.sleep(1)
        print("Curiosity gets the better of you, and you step through the portal.")
        time.sleep(1)
        print("You find yourself in a realm of wonder and enchantment.")
        time.sleep(1)
        print("You have many adventures in this new realm, but eventually, you find a way back to Eldoria.")
        time.sleep(1)
        print("You return to the forest, forever changed by your journey through the portal.")

    def enter_cave(self):
        print("\nYou bravely enter the hidden cave behind the waterfall.")
        time.sleep(1)
        print("Inside, you find yourself in a labyrinth of twisting passages.")
        time.sleep(1)
        print("You explore deeper into the cave, guided by the soft glow of crystals.")
        time.sleep(1)
        print("Suddenly, you hear a low growl echoing through the cavern.")
        time.sleep(1)
        print("You turn a corner and come face to face with a fearsome dragon!")
        time.sleep(1)
        print("You try to reason with the dragon, but it attacks, breathing fire.")
        time.sleep(1)
        print("You barely escape with your life, fleeing back to the safety of the forest.")

    def feel_magical_presence(self):
        print("\nYou close your eyes and focus on the magical presence in the air.")
        time.sleep(1)
        print("You feel a deep connection to the forest and its ancient guardians.")
        time.sleep(1)
        print("They whisper words of wisdom and guidance to you.")
        time.sleep(1)
        print("You spend hours communing with the spirits, learning their secrets.")
        time.sleep(1)
        print("When you finally open your eyes, you feel renewed and ready to face any challenge.")


def main():
    adventure = Adventure()
    adventure.intro()
    adventure.forest_path()
    print("\nYour adventure choices:")
    for i, choice in enumerate(adventure.choices, 1):
        print(f"{i}. {choice}")


if __name__ == "__main__":
    main()
