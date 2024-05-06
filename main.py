# Alex Wong
# wongal2
# CS 361 project

import random
import sys


def main():
    print("Welcome to the mini-game collection!")
    print("Use this program to play some fun games using text input!")
    print()
    user_choice = get_main_choice()
    while True:
        if user_choice == "1":
            high_card_low_card()
        elif user_choice == "H":
            print_help_main()
        elif user_choice == "N":
            print_features_main()
        elif user_choice == "Q" or user_choice == "ESC":
            exit()
        else:
            print("Invalid input, please try again")
        user_choice = get_main_choice()
    return


def get_main_choice():
    print()
    return input("Please select from the following options:\n\
        1:    High Card Low Card\n\
        H:    Help menu\n\
        N:    Read about latest update features\n\
        Q:    Quit\n").upper()


def print_help_main():
    print()
    print("You have the selected the help menu option:")
    print("""
        The mini-game collection features different text based minigames
        for you to enjoy. Follow the menu prompts to navigate to a game
        you would like to play. Enter “ESC” to exit to program at anytime.
        """)
    return


def print_features_main():
    print()
    print("You have selected to read about the latest update features:")
    print("""
        Version 1.0 features the implementation of the user interface and
        High Card Low Card game. More games will be added in future updates!
          """)
    return


def exit():
    print()
    print("Are you sure you want to quit? Your progress will not be saved")
    choice = input("Enter Y for Yes, anything else for No\n").upper()
    if choice == "Y":
        print("Thanks for playing! Goodbye!")
        sys.exit()
    return


def high_card_low_card():
    print()
    print("Welcome to High Card Low Card!")
    print("This game will take less than a minute.")
    user_choice = get_hclc_choice()
    while user_choice != "Q":
        if user_choice == "1":
            play_hclc()
        elif user_choice == "2":
            hclc_rules()
        elif user_choice == "ESC":
            exit()
        else:
            print("Invalid input, please try again")
        user_choice = get_hclc_choice()
    return


def get_hclc_choice():
    print()
    return input("Please select from the following options:\n\
        1.    Start game\n\
        2.    Read the game rules\n\
        Q.    Return to main menu\n").upper()


def hclc_rules():
    print()
    print("You have selected to read the game rules for High Card Low Card:")
    print("""
        In High Card Low Card, two cards with numbers [1, 9] will be picked.
        You will then be shown the first card. You will then guess if the
        second card is higher or lower than the first card. If you guess
        correctly you win a point!
          """)
    return


def play_hclc():
    points = 0
    play = "Y"
    while play == "Y":
        card1 = random.randint(1, 9)
        card2 = random.randint(1, 9)
        while card1 == card2:
            card2 = random.randint(1, 9)
        print()
        print("The first card is : ", card1)
        print("Will the second card be higher or lower?")
        choice = input("Enter H for higher, L for lower\n").upper()
        while choice != "H" and choice != "L":
            if choice == "ESC":
                exit()
            else:
                print("Invalid input, please try again")
            choice = input("Enter H for higher, L for lower\n").upper()
        print()
        print("The second card is : ", card2)
        if (choice == "H" and card2 > card1) or (choice == "L" and card2 < card1):
            print("Congratulations, you win!")
            points += 1
        else:
            print("Sorry, your guess was incorrect")
        print("You have ", points, " points")
        print("Would you like to play again?")
        play = input("Enter Y for yes, anything else to return to the main menu\n").upper()
        if play == "ESC":
            exit()
            play = "Y"
        elif play != "Y":
            print("Are you sure you want to quit? Your progress will not be saved.")
            play = input("Enter Y to continue playing, anything else to return to the main menu\n").upper()
    return


main()
