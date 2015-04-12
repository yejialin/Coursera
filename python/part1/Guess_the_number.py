# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

correct_number = 100
time = 0

# helper function to start and restart the game
def new_game():
    range100()

# define event handlers for control panel
def range100():
    global correct_number
    global time
    time = 7
    correct_number = random.randrange(0, 100)
    print ""
    print "New game.Range is from 0 to 100"
    print "Number of remaining guesses is", time
       
def range1000():
    global correct_number
    global time
    time = 10
    correct_number = random.randrange(0, 1000)
    print ""
    print "New game.Range is from 0 to 1000"
    print "Number of remaining guesses is", time

def input_guess(guess):
    global time
    guess_number = int(guess)
    print ""
    print "Guess was", guess_number
    if guess_number < correct_number:
        print "Higher"
    elif guess_number == correct_number:
        print "Corret"        
    else:
        print "Lower"
    time -= 1

    print "Number of remaining guesses is", time
    if time == 0:
        print "You lose"
        print "The number is",correct_number
        print ""
        new_game()


# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000 ,200)
f.add_button("New game",new_game,200)
f.add_input("Enter a guess", input_guess, 200)
# call new_game 

f.start()
