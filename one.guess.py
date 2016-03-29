import random

def float(minimum,maximum):
	return strength * random.random(minimum,maximum)

def PlayerResult(result, guess):
    if result > guess:
        sub = abs(guess - result)
        return "That is under by {}".format(sub)
    else:
        add = abs(guess - result)
        return "That is over by {}".format(add)

def PlayerResult(result, PlayersGuess):
    if result > PlayersGuess:
        sub = abs(PlayersGuess - result)
        return "That is under by {}".format(sub)
    else:
        add = abs(PlayersGuess - result)
        return "That is over by {}".format(add)

def main(number):
	raw_input("What is the minimum number?: ")
	raw_input("What is the maximum number?: ")
	raw_input("I'm thinking of a number from " "to " )
	raw_input("What do you think it is?: ")

main()

