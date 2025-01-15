# Text-based adventure game: Haunted Mansion Adventure

# Welcome message
print("\nWelcome to the Haunted Mansion Adventure!")
print("You find yourself standing in front of a creepy old mansion. What will you do?")
print("Choices: ENTER, RUN AWAY, or LOOK AROUND\n")

# Get the first choice from the user
choice1 = input("Your choice: ").strip().upper()

# First level of choices
if choice1 == "ENTER":
    print("\nYou step inside the mansion, and the door slams shut behind you.")
    print("In the dimly lit hallway, you see a staircase leading up and a door to the basement.")
    print("Choices: UPSTAIRS or BASEMENT\n")
    
    # Get the second choice
    choice2 = input("Your choice: ").strip().upper()
    
    # Second level of choices
    if choice2 == "UPSTAIRS":
        print("\nYou climb the creaky stairs and find a dusty old library.")
        print("There’s a strange book on a pedestal and a glowing orb on a table.")
        print("Choices: READ the book, TOUCH the orb, or LEAVE the room\n")  # Exceeds: More than two choices
        
        # Get the third choice
        choice3 = input("Your choice: ").strip().upper()
        
        # Third level of choices
        if choice3 == "READ":
            print("\nThe book contains a spell that teleports you safely out of the mansion. You win!")  # Winning outcome
        elif choice3 == "TOUCH":
            print("\nThe orb absorbs your energy. You faint and wake up outside the mansion. Game over!")
        elif choice3 == "LEAVE":
            print("nYou leave the library and find another way out. You survived!")  # Neutral outcome
        else:
            print("\nInvalid choice. The library collapses, and you are trapped. Game over!")
    
    elif choice2 == "BASEMENT":
        print("\nYou descend into the dark basement and see two chests: one gold and one silver.")
        print("Choices: OPEN GOLD, OPEN SILVER, or RETURN upstairs\n")  # Exceeds: More than two choices
        
        # Get the third choice
        choice3 = input("Your choice: ").strip().upper()
        
        # Third level of choices
        if choice3 == "OPEN GOLD":
            print("\nThe chest contains treasure! You are rich and escape the mansion!")  # Winning outcome
        elif choice3 == "OPEN SILVER":
            print("\nThe chest is cursed! You are trapped forever. Game over!")
        elif choice3 == "RETURN":
            print("\nYou go back upstairs and find a secret exit. You escape safely!")  # Neutral outcome
        else:
            print("\nInvalid choice. The basement floods, and you drown. Game over!")
    
    else:
        print("\nInvalid choice. The mansion collapses, and you are trapped. Game over!")

elif choice1 == "RUN AWAY":
    print("\nYou run away safely but never know what secrets the mansion holds. Game over!")

elif choice1 == "LOOK AROUND":
    print("\nYou discover a hidden key under the doormat.")  # Exceeds: Hidden choice
    print("Do you want to ENTER the mansion using the key or LEAVE?\n")
    
    # Get the second choice
    choice2 = input("Your choice: ").strip().upper()
    
    # Second level of choices
    if choice2 == "ENTER":
        print("\nUsing the key, you find a hidden treasure room. You win!")  # Hidden reward
    elif choice2 == "LEAVE":
        print("\nYou leave safely but miss out on the treasure. Game over!")
    else:
        print("\nInvalid choice. The mansion vanishes into thin air. Game over!")

else:
    print("\nInvalid choice. A ghost appears and scares you away. Game over!")

# Features that exceed requirements:
# 1. Hidden choice in "LOOK AROUND" leads to discovering a key.
# 2. More than two choices in some scenarios (e.g., library and basement).
# 3. Multiple endings (winning, neutral, losing) provide diverse outcomes.
# 4. Input flexibility with case-insensitive handling using strip() and upper().
