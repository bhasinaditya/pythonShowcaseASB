################################################################################################
# This is guess the number game

import random
secretNumber = random.randint(1, 20)
print('I am thinking of a random number between 1 and 20.')

# Ask the player to take a guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess...')
    # user enters the number
    guess = int(input())
    if guess < secretNumber:
        print('your guess is too LOW')
    elif guess > secretNumber:
        print('your guess is too HIGH')
    else:
        break  # This is the correct guess

if guess == secretNumber:
    print('Good Job!  You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

################################################################################################