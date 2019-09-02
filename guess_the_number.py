## Secret number establishment
import random
secretNum = random.randint(1,10)

## prompt for guessing number and track the gugess attempts
guess = int(input("Guess a number from 1 - 10: "))
guessCount = 0
## While loop giving hints for gguessing number
while guessCount < 4:    
    if secretNum > guess:
        guess = int(input("Higher! Guess again: "))
        guessCount = guessCount + 1
    if secretNum < guess:
        guess = int(input("Lower! Guess again: "))
        guessCount = guessCount + 1
    if secretNum == guess:
        print("You got it!")
        break
else: 
    print("You are out of guesses! Bye!")
