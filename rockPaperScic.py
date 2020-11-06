# File name: rockPaperScic.py
# Author: Yonah Aviv
# Date created: October 6, 2020

# Game is playable but computer decisions are random. No AI yet

def compchoice():
    """if win_q == human: 
        if us == 3:
            cs = 1
        else:
            cs = us + 1
     elif win_q == "computer":
        if us == 3:
            cs = 3
        else:
            cs = us
      return cs
    """
    cs = random.randint(1,3)
    return cs
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

name = input("Type a name to be able to save game: ")
datafile = open("gameData.txt", "r")
prevdata = datafile.read()
datafile.close()
# backfile = open("gameDataBackup.txt", "w")
# print(prevdata, file=backfile)
# backfile.close()
datafile = open("gameData.txt", "w")

while True:
    if run:
        x = input("[1] to continue, or [2] to Quit: ")
    if x == "1":
        error = True
        print("R = rock.  P = paper.  S = scissors.")
        us = input("Enter your choice: ")
        # cs = computerChoice()
        cs = compchoice() 
        if us == "R" or us == "r" or us == "Rock" or us == "rock":
            us = 1
            error = False
        if us == "P" or us == "p" or us == "Paper" or us == "paper":
            us = 2
            error = False
        if us == "S" or us == "s" or us == "Scissors" or us == "scissors":
            us = 3
            error = False

        if not error:
            computerHistory.append(cs)
            humanHistory.append(us)

            count = count + 1
            cs = choices[cs - 1]
            us = choices[us - 1]
            print("You chose", us, "and the computer chose", cs, ":")
            win = getwinner(cs, us)

            winHistory.append(win)
            if win == "tie":
                print("The game is a tie.")
            if win == "human":
                humanScore = humanScore + 1
                print("You win!")
            if win == "computer":
                computerScore = computerScore + 1
                print("The computer wins.")
            print("Your score is", humanScore, "of", count, ".")
            print("The computer's score is", computerScore, "of", count, ".")
        if error:
            print("That is an invalid command!")

        run = True
    if x == "2":
        break
    if x != ("1" or "2"):
        print("That is an invalid command!")
        run = True

filecleanup() #log history in gameData.txt
