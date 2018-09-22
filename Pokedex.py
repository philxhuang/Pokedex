#################################################
# rock_paper_scissors.py
#################################################
#Hi, this is Gwyneth
import random

def getTurnsToPlay():
    rawInput = input('How many turns to play --> [or just hit enter for 5] ')
    if (rawInput == ''):
        return 5
    else:
        return int(rawInput)

def getComputerChoice():
    option = random.randint(0, 4)
    if (option == 0):
        print('I choose rock!')
        return 'r'
    elif (option == 1):
        print('I choose paper!')
        return 'p'
    elif (option == 2):
        print('I choose scissors!')
        return 's'
    elif (option == 3):
        print('I choose lizard!')
        return 'l'
    elif (option == 4):
        print('I choose spoch!')
        return 'spo'

def getUserChoice():
    while True:
        # keep looping until the user enters a legal value
        userChoice = input('You choose: [r]ock, [p]aper, or [s]cissors, or [l]lizard, or [spo]ch: ')
        if ((userChoice != 'r') and (userChoice != 'p') and (userChoice != 's') and (userChoice != 'l') and (userChoice != 'sp')):
            print('Illegal choice.  Enter r, p, or s.  Please try again!')
        else:
            return userChoice

def playOneTurn():
    # returns the winner of the turn -- 'computer', 'user', or None
    userChoice = getUserChoice()
    computerChoice = getComputerChoice()
    if (userChoice == computerChoice):
        print('Tie! No winner this turn!')
        return None
    elif (((userChoice == 'r') and (computerChoice == 'p')) or
          ((userChoice == 'p') and (computerChoice == 's')) or
          ((userChoice == 's') and (computerChoice == 'r')) or
            ((userChoice == 'r') and (computerChoice == 'l')) or
            ((userChoice == 'p') and (computerChoice == 'l')) or
            
            ((userChoice == 's') and (computerChoice == 'spo')) or
            ((userChoice == 'l') and (computerChoice == 's')) or
            
            ((userChoice == 'l') and (computerChoice == 'r')) or
            ((userChoice == 'spo') and (computerChoice == 'l')) or
            
            ((userChoice == 'spo') and (computerChoice == 'p'))):
        print('I win this turn!')
        return 'computer'
    else:
        print('You win this turn!')
        return 'user'

def reportResults(userWins, computerWins):
    print('----------------------------')
    print('Game Over!')
    print('Your score:', userWins)
    print('My score:', computerWins)
    if (userWins > computerWins):
        print('YOU WON!!!!')
    elif (computerWins > userWins):
        print('I WON!!!!')
    else:
        print('We TIED!!!')
    print('----------------------------')

def rockPaperScissors():
    turns = getTurnsToPlay()
    userWins = 0
    computerWins = 0
    for turn in range(turns):
        print('----------------------')
        print('Turn', (turn+1), 'of', turns, ':')
        winner = playOneTurn()
        if (winner == 'user'):
            userWins += 1
        elif (winner == 'computer'):
            computerWins += 1
    reportResults(userWins, computerWins)

rockPaperScissors()
