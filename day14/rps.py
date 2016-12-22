# import random module
import random

# run function while count is less than/equal to 3
while count >= 3:
    # set count to zero at start
    count = 0 
    # set number of computer wins to 0
    computer = 0
    # set number of human wins to 0
    human = 0
    # allow user to choose rock, paper, or scissors
    a = input("rock, paper, or scissors? ")
    # allow computer to randomly chose rock, paper or scissors
    options = ["rock", "paper", "scissors"]
    b = random.choice(options)

    # print what the computer and you chose
    print("you chose", a, "and computer choses", b)

    # define function
    def rockpaperscissors():
    
        # if user = rock and computer = rock
        if a == "rock":
            if b == "rock":
                # print "tie"
                print("tie!")
                # reduce count bc a tie should not count as a round
                count -= 1
            # if user = rock and computer = paper
            elif b == "paper":
                # print "computer wins"
                print("computer wins")
                # add to computer victories
                computer +=1
            # if user = rock and computer = scissors
            elif b == "scissors":
                # print "you win"
                print("you win!")
                # add to human victories
                human += 1
        # if user = paper and computer = paper
        if a == "paper":
            if b == "paper":
                # print tie
                print("tie!")
                # reduce count bc a tie should not count as a round
                count -= 1
            # if user = paper and computer = scissors
            elif b == "scissors":
                # print "computer wins"
                print("computer wins")
                 # add to computer victories
                computer +=1
            # if user = paper and computer = rock
            elif b == "rock":
                # print "you win"
                print("you win!")
                # add to human victories
                human += 1
                
        # if user = scissors and computer = scissors
        if a == "scissors":
            if b == "scissors":
                # print tie
                print("tie!")
                # reduce count bc a tie should not count as a round
                count -= 1
            # if user = scissors and computer = rock
            elif b == "rock":
                # print "computer wins"
                print("computer wins")
                # add to computer victories
                computer +=1
            # if user = scissors and computer = paper
            elif b == "paper":
                # print "you win"
                print("you win!")
                # add to human victories
                human += 1
                
    # call function
    rockpaperscissors()
# increase count for each time run through function
    count += 1
    
# if human has won twice
if human == 2:
    print("you win!" )
# print "you win game"

# if computer has won twice
if computer == 2:
    # print "computer wins game"
    print("computer wins game" )