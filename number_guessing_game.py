import random


from arts import logo_guess_the_number


def numbers():
    r = random.randint(1, 101)
    return r


def guessing(level):
    while True:
        print(f"You have {level} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        if level > 1:

            if guess == guessed_no:
                print(f"You got it! The answer was {guess}.")
                break
            elif guess >= guessed_no:
                print("Too high")
                print("Guess again")
            elif guess <= guessed_no:
                print("Too low")
                print("Guess again")
            else:
                print("Your guess average no")

            level -= 1
        else:
            print(f"You have run out of guesses, you lose.")
            break


print(logo_guess_the_number)
guessed_no = numbers()
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
choice = input("Choose a difficult. Type 'easy' or 'hard': ")
#print(f"your right guess: {guessed_no}")
if choice == 'easy':
    guessing(10)
else:
    guessing(5)

"""
or alternative way

import random

EASY_LEVEL = 10
HARD_LEVEL = 5

random_guess_no = random.randint(1,100)
def guess_again():
    return "Guess again!"

def check_win(user_guess, actual_guess, turns):
    if user_guess < actual_guess:
        print("Too low")
        print(guess_again())
        return turns - 1
    elif user_guess > actual_guess:
        print("Too high")
        print(guess_again())
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_guess}")

def set_difficulty():
    levels = input("Choose a difficulty level, Type 'easy' or 'hard': ")
    if levels == 'easy':
      return EASY_LEVEL
    else:
      return HARD_LEVEL

def guessing_game():

    guess = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    level = set_difficulty()

    while guess != random_guess_no:
        print(f"You have {level} attempts remaining to guess the game")
        guess = int(input("Make a guess: "))
        level = check_win(guess, random_guess_no, level)
        if level == 0:
            print("You have run out of guessing, you lose.")
            print(f"The correct guess was: {random_guess_no}")
            return

guessing_game()

"""