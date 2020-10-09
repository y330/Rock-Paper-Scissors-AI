# File name:ockPaperScic.py
# Author: Yonah Aviv
# Date created: October 6, 2020

import random


def getwinner(cs, us):
    # winCombo = [0,1], [1,2], [2,0] # winning combinations relative to first comp: rockpaper, paperscissors,
    # scissorsrock ref1, ref2 = us + cs, cs + us  # user input <=> concatenated with computer inp  ut

    # if ref1 in winCombo:  # relative to user input, computer wins
    # 	result = "You lost!", cPoint + 1
    # elif ref2 in winCombo:  # relative to computers input, you win
    # 	result, uPoint = "You won!", uPoint + 1
    # elif us == cs:  # draw
    # 	win = "tie"

    if us == cs:
        win_q = "tie"
    elif us == "rock" and cs == "paper":
        win_q = "computer"
    elif us == "rock" and cs == "scissors":
        win_q = "human"
    elif us == "paper" and cs == "rock":
        win_q = "human"
    elif us == "paper" and cs == "scissors":
        win_q = "computer"
    elif us == "scissors" and cs == "rock":
        win_q = "computer"
    elif us == "scissors" and cs == "paper":
        win_q = "human"

    return win_q


def checkfile(filename):
    try:
        status = open(filename, "x")
    except FileExistsError:
        status = open(filename, "r")
    return status


def filecleanup():
    print(prevdata, file=datafile)
    if name != "test":
        print(name + ":", file=datafile)
        print("Wins:", winHistory, file=datafile)
        print("Computer Choices:", computerHistory, file=datafile)
        print("Human Choices:", humanHistory, file=datafile)
    datafile.close()


run = True
count = 0
humanScore = 0
computerScore = 0
choices = ["rock", "paper", "scissors"]
winHistory = []
computerHistory = []
humanHistory = []
print
name = input("Name: ")
datafile = checkfile("gameData.txt")  # check if gameData.txt exists
prevdata = datafile.read()
datafile.close()
# backfile = open("gameDataBackup.txt", "w")
# print(prevdata, file=backfile)
# backfile.close()
datafile = open("gameData.txt", "w")

while True:
    if run:
        print("""
        ██     ██ ███████ ██      ██████  ██████  ███    ███ ███████ 
██     ██ ██      ██     ██      ██    ██ ████  ████ ██      
██  █  ██ █████   ██     ██      ██    ██ ██ ████ ██ █████ 
██ ███ ██ ██      ██     ██      ██    ██ ██  ██  ██ ██    
 ███ ███  ███████ ███████ ██████  ██████  ██      ██ ███████ 
                                                             

        """)
        x = input("\n\n[1]Continue \n[2]Quit\nThe choice is yours: ")
    if x == "1":
        error = True
        print("""██████      ██ ██████    ██ ███████ 
██   ██    ██  ██   ██  ██  ██      
██████    ██   ██████  ██   ███████ 
██   ██  ██    ██     ██         ██ 
██   ██ ██     ██    ██     ███████ 
                                    
                                    """)
        us = input("Enter your choice: ")
        # cs = computerChoice()
        cs = random.randint(1, 3)
        if us in ["R", "r", "Rock", "rock"]:
            us = 1
            error = False
        if us in ["P", "p", "Paper", "paper"]:
            us = 2
            error = False
        if us in ["S", "s", "Scissors", "scissors"]:
            us = 3
            error = False

        if not error:
            computerHistory.append(cs)
            humanHistory.append(us)

            count += 1
            cs = choices[cs - 1]
            us = choices[us - 1]
            print("You chose", us, "and the computer chose", cs, ":")
            win = getwinner(cs, us)

            winHistory.append(win)
            if win == "tie":
                print("The game is a tie.")
            if win == "human":
                humanScore += 1
                print("You win!")
            if win == "computer":
                computerScore += 1
                print("The computer wins.")
            print("Your score is", humanScore, "of", count, ".")
            print("The computer's score is", computerScore, "of", count, ".")
        if error:
            print("Invalid input. Please follow instructions.")

        run = True
    elif x == "2":
        break
    if x != ("1" or "2"):
        print("Invalid input. Please follow instructions.")
        run = True

filecleanup()
5
