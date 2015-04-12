# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

# helper functions
def name_to_number(name):
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
        print "What's this"
    
def number_to_name(number):
    if number == 0:
        return "rock"
    if number == 1:
        return "Spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard"
    if number == 4:
        return "scissors"
    
def rpsls(player_choice): 
    temp1 = name_to_number(player_choice)
    temp2 = random.randrange(0,5)
    print "Player chooses", player_choice
    print "Computer choose", number_to_name(temp2)
    if (temp1 - temp2) % 5 < 3:
        print "Player wins!"
    else:
        print "Computer wins!"
    print ""
    
	
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

