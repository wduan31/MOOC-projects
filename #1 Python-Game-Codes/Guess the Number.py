# http://www.codeskulptor.org/#user31_Lfb3XoW0eK_22.py
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# initialize global variables used in your code
answer = 0
# answer is the number randomly generated by computer
low = 0
# low sets the lower limit of answer
high = 100
# high sets the higher limit of answer
remain_chances = 0
# remain_chances records the chances remained before failure

# helper function to start and restart the game
def new_game():
    global answer
    global remain_chances
    answer = random.randrange (low, high)
    # randomly generates a number bewteen limits
    remain_chances = int(math.ceil(math.log(high - low + 1, 2)))
    # remained chances is the smallest integer n that satisfies
    # 2 ** n >= high - low + 1
    print "A new game starts with range between", low,  "and" , high
    print "Chances Remaining", remain_chances, "\n"
    pass


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global low
    global high
    low = 0
    high = 100
    new_game()
    pass

def range1000():
    # button that changes range to range [0,1000) and restarts
    global low
    global high
    low = 0
    high = 1000
    new_game()
    pass
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    global remain_chances
    print "Your guess was:", guess
    if (guess > answer ):
        print "Lower!"
        # if the guessed number is too high, ask player to lower the guess
        remain_chances = remain_chances -1
        print "Chances Remaining", remain_chances, "\n"    
    elif (guess < answer ):
        print "Higher"
        # if the guessed number is too low, ask player to increase the guess
        remain_chances = remain_chances -1
        print "Chances Remaining", remain_chances, "\n"
    else:
        print "You Win! Answer is ", answer, "\n" 
        new_game()
        # Start a new game if the player is correct and wins
    if (remain_chances == 0):
        print "Sorry,You Lose! Answer is", answer, "\n"
        new_game()
        # Start a new game if the player runs out of trial
    pass

    
# create frame
frame = simplegui.create_frame ("Guess the number", 200, 200)


# register event handlers for control elements
frame.add_button ("Range is [0,100)", range100, 200)
frame.add_button ("Range is [0,1000)", range1000, 200)
frame.add_input ("Enter an input", input_guess, 200)
# call new_game and start frame
frame.start()


# always remember to check your completed program against the grading rubric
