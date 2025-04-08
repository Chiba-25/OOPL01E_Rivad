import time

def adventure_game():
    # Introduction
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a dark forest with two paths ahead.")
    time.sleep(1)
    print("Will you take the left path or the right path?")
    time.sleep(1)

    # First decision
    choice1 = input("Type 'left' or 'right': ").lower()
    if choice1 == "left":
        print("\nYou walk down the left path and encounter a friendly fox.")
        time.sleep(1)
        print("The fox offers you two items: a glowing sword or a magical potion.")
        time.sleep(1)
        item = input("Type 'sword' or 'potion': ").lower()
        if item == "sword":
            print("\nYou take the sword and continue your journey. The forest grows darker...")
            time.sleep(1)
            print("Suddenly, a wild troll appears! You bravely fight and defeat it with your sword.")
            time.sleep(1)
            print("Victory is yours! You find a treasure chest filled with gold.")
        elif item == "potion":
            print("\nYou drink the potion and feel your strength increase.")
            time.sleep(1)
            print("The potion reveals a hidden path leading to a secret garden with rare jewels!")
        else:
            print("\nConfused by your indecision, you wander aimlessly and return to the forest entrance.")
    elif choice1 == "right":
        print("\nYou take the right path and stumble upon a mysterious cave.")
        time.sleep(1)
        print("Inside the cave, you find two ancient artifacts: a magic lamp and a crystal orb.")
        time.sleep(1)
        artifact = input("Type 'lamp' or 'orb': ").lower()
        if artifact == "lamp":
            print("\nYou rub the magic lamp and a genie appears! You are granted three wishes.")
            time.sleep(1)
            print("Choose wisely, and your destiny changes forever!")
        elif artifact == "orb":
            print("\nThe crystal orb shows you visions of the future.")
            time.sleep(1)
            print("You learn valuable secrets that help you on your journey to find hidden treasure!")
        else:
            print("\nYou hesitate and the cave collapses, forcing you to retreat.")
    else:
        print("\nYou decide not to take either path and remain stuck in the forest forever. Game over!")

# Start the game
adventure_game()
