# CONSOLE_GUESSING_GAME
import random


def test_number():
    # Computer 3_digit random number
    sample_space = list(range(0, 10))
    random.shuffle(sample_space)  # shuffle the list of numbers to avoid repitition

    target = sample_space[:3]

    '''
    Checks whether user- input 3-digit number is exactly the same as
     the chosen random 3-digit number(case 1), or if at least one of the digits are equal(case 2'
     or none of the are equal(case 3).
    :return: match for case 1, close for case 2, nope for case 3
    '''
    while True:
        # User prompted 3_digit number
        guessed_number = input("Enter 3 numbers and separate each with a comma:\n")

        guessed_list = guessed_number.split(",")

        if len(guessed_list) != 3:
            print("ENTER ONLY 3 DIGITS")
            continue
        # for i in range(0, 3):
        #     if guessed_list[i] == target[i]:
        #         print("Match")
        #     elif guessed_list != target[i]:
        #         print("Nope")
        #     else:
        #         print("Close")

        if (guessed_list[0] == target[0]) and (guessed_list[1] == target[1]) and (guessed_list[2] == target[2]):
            print("Match")
        elif (guessed_list[0] != target[0]) and (guessed_list[1] != target[1]) and (guessed_list[2] != target[2]):
            print("Nope")
        else:
            print("Close")
            print("You almost guessed the number")
            pass

        a = input("Would you love to play again?? type 'y' to continue and 'n to stop'.\n")

        if a is "y":
            test_number()
        else:
            print(target)
            print("Thank You!! for playing the game.")
            break


test_number()
