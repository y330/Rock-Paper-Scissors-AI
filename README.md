# Rock Paper Scissors model

***Yonah Aviv***



  


**This is a work in progress, but you can play rock paper scissors against a computer that is random in [rockPaperScic.py](rockPaperScic.py).**

[Go to Training folder](Training) to see how my model works(unfinished). It will use machine learning.

  

## Background and methods

I took a great walkthrough on a statistical analysis of rock paper scissors from [DataGentics](http://datagenetics.com/blog/march52013/index.html), [written by Nick Barry](http://datagenetics.com/about.html)(I think) and used it as a reference for my code. 

### Mixtures

> The probability of being the winning tribe depends of the concentrations (relative ratios) of the starting players. The starting conditions effect the chances of surviving to the end. Obviously, if the ratios of Rock, Paper and Scissors at the start of the game are the same, the probabilities of being the last tribe standing are the same (This should be obvious from symmetry, and from the fact the intransitive property that each class is the same with exactly one strength and one weakness each). To work out what happens with non-equal starting conditions, we need to model the system. (DataGenetics) <sup>1</sup>

### Monte Carlo Method

![](http://datagenetics.com/blog/march52013/gm.png)
> To model this system, I wrote code to perform this contrived Rock, Paper, Scissors game using a random number generator to select two opponents for each round. Each game was played to completion. To get smooth results, I repeated this exercise 10,000 times for all combitions of starting players from 1-50 of each symbol. I counted the number of times the Rock team won, the number of times the Paper team won, and the number of times the Scissor team won. I also recorded the average number of rounds that were required to produce a winner. (DataGenetics) <sup>1</sup>




----

Rock paper scissors game with AI that predicts the future.

## Works Cited

1. Barry, Nick. “Rock, Paper, Scissors.” Datagenetics.com, 2013, datagenetics.com/blog/march52013/index.html. Accessed 6 Dec. 2020.



