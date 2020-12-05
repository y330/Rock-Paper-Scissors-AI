# author: Yonah Aviv
# created: 11/09/2020
# modified: 12/05/2020

# training/simulations/test for rock paper scissors(rps)
""" Using a mathematical explanation of Rock, Paper, Scissors from datagenetics.com

Rock, Paper, Scissors. Datagenetics.com (2013), (available at http://datagenetics.com/blog/march52013/index.html).
"""


import random
import collections


"""tables of outcomes for each hand:
210
021
102
"""
shifted = [1,2]
matrix = [2,1,0]
matrix = collections.deque(matrix)
wins = []

choices = {
    "rock": ["rock", "r", 0],
    "paper": ["paper", "p", 1],
    "scissors": ["scissors", "s", 2],
}


opponents = [AI(2) for i in range(10)]

def AI(index):
    return random.choice(list(choices.values()))[index]

def GetKey(val):
   for key, value in choice.items():
      if val == value:
         return key
      return "key doesn't exist"

def sample(size):
    global selection 
    selection = random.choices(population=opponents, k=size)
    return selection
def win(data, res):
    global wins, shifted
    for i in range(3):
        if res == shifted:
            print("3")
            wins = (list(
                        choices.keys()
                    )
                    [list
                     (
                         choices.values()
                     ).index(
                         [i][res[1]]
                     )
                    ]
                   )
            pass
        matrix.rotate(-1)
        shifted = list(matrix)[::2]
        
win(opponents, sample(2))
    

# def select(opponents):
#     C=["rock","paper","scissors"]
#     c,c1,p=random.choice(C),input(),{C[n]:C[(n+1)%3] for n in range(3)}
#     if c1 in p:print("You chose {}\nI chose {}".format(c1,c));
# CHOICES = ("rock", "paper", "scissors")
# while True:
#     human = raw_input("Your move [%s]: " % ",".join(CHOICES)).lower()
#     if human not in CHOICES: continue
#     cpu = random.choice(CHOICES)
#     print("CPU plays: %s" % cpu)
#     if human != cpu: break
#     print("Tie, play again..\n")

# print("You %s!" % ("Win" if CHOICES[CHOICES.index(human)-1] == cpu else "Lose"))

# players = {}
# players["opponents"] = enemys = [random.randint()] for i in range(10)]
# for i in range(10):
#   players["i"] = 4]
