import time
import random

score = 0

# function that declares print and pause


def print_Pause(para):
    print(para)
    time.sleep(2)


# game code
def start_game():
    colors = ["red", "blue", "green", "white", "black"]
    Specific_Color = random.choice(colors)

    # Define the player's name
    player_name = input("What is your name, adventurer? ")
    # Initialize the player's score
    score = 0
    # Define the starting point of the story
    print_Pause(
        f"Welcome,{player_name}!"
    )
    print_Pause(
        f"Nice {Specific_Color} outfit You find yourself in a dark forest")
    print_Pause(
        f"searching for alost treasure. As you make your way through the trees"
    )
    print_Pause(f"you come across afork in the path.Your score is {score}")

    # Define the first choice

    while True:
        choice1 = input("\nWhich path do you choose? (left / right) ")
        if choice1 in ["left", "right"]:
            break
        else:
            print_Pause("Please enter either 'left' or 'right'.")

    # Consequences based on the left choice
    if choice1 == "left":
        score += 10
        print_Pause(
            f"\nYou choose to take the left path, "
        )
        print_Pause("you come across a clearing with a small pond.")
        print_Pause(
            f"There isa small boat tied up on the shore.Your score is {score}")

        while True:
            choice2 = input(
                "Do you want to get in boat and row across the pond?(yes/no)"
            )
            if choice2.lower() in ["yes", "no"]:
                break
            else:
                print_Pause("Please enter either 'yes' or 'no'.")

        if choice2 == "yes":
            score += 10
            print_Pause(f"\nYou get into the boat and row across the pond.")
            print_Pause(
                f"As you approach the other side"
            )
            print_Pause("you see a glint of gold in the distance")
            print_Pause(
                f"You row closer"
            )
            print_Pause("and find atreasure chest filled with gold and jewels")
            print_Pause(
                f"You have earned 10 points.Your score is {score}"
            )

            End_Game(player_name, score)
        else:
            score -= 10
            print_Pause(
                f"\nYou decide not to risk getting in the boat"
            )
            print_Pause(f"hoping to find the treasure another way.")
            print_Pause(f"Your score is {score}")
            End_Game(player_name, score)
    # Consequences based on the right choice
    else:
        score += 10
        print_Pause(f"\nYou choose to take the right path")
        print_Pause(
            f"you come across a dark and spooky cave"
        )
        print_Pause(f".A faint light can be seen in the distance.")
        print_Pause(f"Your score is {score}")
        while True:
            choice2 = input(
                "Do you want to enter and investigate the light?(yes/no)"
            )
            if choice2 in ["yes", "no"]:
                break
            else:
                print_Pause("Please enter either 'yes' or 'no'")

        # Award points based on the second choice
        if choice2 == "yes":
            score += 10
            print_Pause(
                f"You entered and make your way through the twisting passages"
            )
            print_Pause(
                f"Eventually,you come across aroom"
            )
            print_Pause("with asmall fire burning in the center")
            print_Pause(
                f"Next to the fire is a treasure chest filled with gold!"
            )
            print_Pause(f"You have earned 10 points.Your score is {score}.")
            End_Game(player_name, score)

        else:
            score -= 10
            print_Pause(
                f"You decide not to risk entering the cave"
            )
            print_Pause(f"hoping to find the treasure another way")
            print_Pause(f"Your score is {score}")
            End_Game(player_name, score)
            # End Game


def End_Game(player_name, score):
    if score == 20:
        print_Pause(
            f"Congratulations,{player_name}"
        )
        print_Pause("You have completed the game with score of 40")
        print_Pause(f"/nThanks for playing!")
        Repeating_Game()
    else:
        print_Pause(
            f"/nGood luck for another timeYour current score is {score}")
        Repeating_Game()


# Repeating_Game##
def Repeating_Game():
    while True:
        repeating_option = input("Do you want to play again???  YES/NO")
        if repeating_option == "yes":
            score = 0
            start_game()
        elif repeating_option == "no":
            print_Pause("thanks for playing. goodbye!!!!")
            break
        else:
            print_Pause("please enter either yes or no")


start_game()
