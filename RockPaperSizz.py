# Rock Paper Sizz

import random, sys

print ('ROCK, PAPER. SIZZ')

# These variables keep track of wins, losses and draw
wins = 0
losses = 0
ties = 0

while True: # the main loop for the game
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # the player input loop
        print('Enter your move: (r)ock (p)aper (s)izz or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # quit the program
        if playerMove=='r' or playerMove=='p' or player=='s':
            break # leave player input loop
        print('Type one of r, p, s or q')

    # Display what the player chose
    if playerMove == 'r':
        print('ROCK verses...')
    if playerMove == 'p':
        print('paper verses...')
    if playerMove == 's':
        print('sizz verses...')

    # Display computer's choice
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove='r'
        print('ROCK')
    if randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    if randomNumber == 3:
        print('SIZZ')

    # Display and record win/loss/tie
    if (playerMove == computerMove):
        print('Its a tie!')
        ties = ties+1;
    elif playerMove=='r' and computerMove=='s':
        print('You Win')
        wins=wins+1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 's';
        print('You Win')
        wins = wins + 1