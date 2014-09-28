__author__ = 'Jonas'
#Guess the Number
#Mini project 3

import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

secret_number = None
player_guess = None
max_range = 100
min_range = 0
num_guesses = None
guesses_remaining = None

def new_game():
    """
    This function starts a new game, computes a secret number, and computes
    the maximum allowed number of guesses for the player
    """
    print "New Game!\n"
    global secret_number
    global guesses_remaining
    global num_guesses
    secret_number = random.randrange(min_range, max_range)
    num_guesses = int(math.ceil(math.log(max_range, 2)))
    guesses_remaining = num_guesses

def range100():
    """
    This function sets the secret number range to [0 - 100) and starts
    a new game
    """
    global max_range
    global min_range
    max_range = 100
    min_range = 0
    print "\nSetting range to [0 - 100)\n"
    new_game()

def range1000():
    """
    This function sets the secret number range to [0 - 1000) and starts
    a new game
    """
    global max_range
    global min_range
    max_range = 1000
    min_range = 0
    print "\nSetting range to [0 - 1000)\n"
    new_game()

def input_guess(guess):
    """
    This function is the input handler which accepts a guess from the user as a string
    and converts it to an integer. The function then returns an appropriate message based
    on the guess and subtracts 1 from the guesses remaining.
    """
    global num_guesses
    global guesses_remaining
    guess = int(guess)
    guesses_remaining -= 1

    if guesses_remaining == 0:
        print "You ran out of guesses. You lose!"
        new_game()

    print "Your guess:", guess
    print "Guesses remaining:", guesses_remaining

    if guess == secret_number:
        print "Correct!\n"
        new_game()
    elif guess > secret_number:
        print "Lower\n"
    else:
        print "Higher\n"

frame = simplegui.create_frame("Guess the Number", 100, 200)

frame.add_input("Your guess:", input_guess, 50)
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)

new_game()
frame.start()