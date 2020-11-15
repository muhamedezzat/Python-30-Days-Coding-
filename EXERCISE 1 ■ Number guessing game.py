from prettytable import prettyTable
import random


def guessing_number():
    number = random.randint(0, 100)

    for i in range(3):
        # while True:
        user_input = int(input(f"Please Guess a number: "))
        print(number)
        if user_input == number:
            print(f"Right! the answer if {user_input}\n")
            print("Thanks for Guessing the correct number ")
            break
        elif user_input > number:
            print(f"Your guess {user_input} is Too Hight \n")
        else:
            print(f"Your guess {user_input} is Too Low \n")

        print("Sorry! You Guess wrong three Times.\nThanks for your Time")


print(f"\nWelcome to my funny guessing game I hope to enjoy with it.\n")
guessing_number()
