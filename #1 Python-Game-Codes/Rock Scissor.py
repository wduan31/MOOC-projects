#http://www.codeskulptor.org/#user29_e6xclxlnqEdEBze_12.py

import random
def name_to_number (name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "wrong input"
def number_to_name (number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "input number out of range"
def RPSLS (player_choice):

    print "Player chooses " + player_choice
    computer_choice = random.randrange(0,5)
    print "Player chooses " + number_to_name (computer_choice)
    num = (name_to_number (player_choice) -  computer_choice) % 5
    if num == 1 or num == 2:
        print "Player wins!"
    elif num == 3 or num == 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    print
    return ()
RPSLS ("rock")
RPSLS ("Spock")
RPSLS ("paper")
RPSLS ("lizard")
RPSLS ("scissors")
