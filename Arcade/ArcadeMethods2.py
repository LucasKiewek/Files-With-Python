import random


def bet_for_craps(money):

    bet = raw_input('place your bet: $')
    if bet.isdigit():
        bet = int(bet)

        while bet == 0:
            print 'please bet something...'
            bet = raw_input('place your bet: $')
            if bet.isdigit():
                bet = int(bet)

        while bet > money:
            print 'You do not have enough money'
            currBalance = 'Your current balance is: $'+str(money)
            print currBalance
            bet = raw_input('place your bet: $')
            if bet.isdigit():
                bet = int(bet)
                while bet == 0:
                    print 'please bet something...'
                    bet = raw_input('place your bet: $')
                    if bet.isdigit():
                        bet = int(bet)

    else:
        while bet > money:
            print 'You do not have enough money'
            currBalance = 'Your current balance is: $'+str(money)
            print currBalance
            bet = raw_input('place your bet: $')
            if bet.isdigit():
                bet = int(bet)
                while bet == 0:
                    print 'please bet something...'
                    bet = raw_input('place your bet: $')
                    if bet.isdigit():
                        bet = int(bet)

    bet = int(bet)

    return bet


def bet_for_inBetween(money):

    bet = raw_input('place your bet: $')
    if bet.isdigit():
        bet = int(bet)

        while bet < 5:
            print 'the minimum bet is $5...'
            bet = raw_input('place your bet: $')
            if bet.isdigit():
                bet = int(bet)

        while bet > money:
            print 'You do not have enough money'
            currBalance = 'Your current balance is: $'+str(money)
            print currBalance
            bet = raw_input('place your bet: $')
            if bet.isdigit():
                bet = int(bet)
                while bet < 5:
                    print 'the minimum bet is $5...'
                    bet = raw_input('place your bet: $')
                    if bet.isdigit():
                        bet = int(bet)

    else:
        while bet > money:
            print 'You do not have enough money'
            currBalance = 'Your current balance is: $'+str(money)
            print currBalance
            bet = raw_input('place your bet: $')
            if bet.isdigit():
                bet = int(bet)
                while bet < 5:
                    print 'the minimum bet is $5...'
                    bet = raw_input('place your bet: $')
                    if bet.isdigit():
                        bet = int(bet)

    bet = int(bet)
    return bet


def bet_for_guessingGame(money):

    bet = raw_input('place your bet: $')
    if bet.isdigit():
        bet = int(bet)

        while bet < 5:
            print 'the minimum bet is $5...'
            bet = raw_input('place your bet: $')
            if bet.isdigit():
                bet = int(bet)

        while bet > money:
            print 'You do not have enough money'
            currBalance = 'Your current balance is: $'+str(money)
            print currBalance
            bet = raw_input('place your bet: $')
            if bet.isdigit():
                bet = int(bet)
                while bet < 5:
                    print 'the minimum bet is $5...'
                    bet = raw_input('place your bet: $')
                    if bet.isdigit():
                        bet = int(bet)

    else:
        while bet > money:
            print 'You do not have enough money'
            currBalance = 'Your current balance is: $'+str(money)
            print currBalance
            bet = raw_input('place your bet: $')
            if bet.isdigit():
                bet = int(bet)
                while bet < 5:
                    print 'the minimum bet is $5...'
                    bet = raw_input('place your bet: $')
                    if bet.isdigit():
                        bet = int(bet)

    bet = int(bet)
    return bet

def guessingGameGuess():
    y=raw_input("Guess a number between 1 and 100: ")
    while not y.isdigit():
        y=raw_input("Guess a number between 1 and 100: ")
    y = int(y)
    return y

def guessingGame(money):

    x = random.randint(1,100)
    tries = 5
    guess = 1000
    bet = bet_for_guessingGame(money)

    while guess!= x and tries!= 0:
        if tries != 5:
            print "You have", tries, "tries left."
        else:
            print "you get 5 tries."
        guess = guessingGameGuess()
        if guess > x:
            print "Too high, guess again"
        if guess < x:
            print "Too low, guess again"
        tries -= 1


    if guess == x:
        print "You guessed it!"
        money += bet

    else:
        print "\ntoo bad\n"
        print "the number was", x, "\n"
        money -= bet

    return money

def craps(money):

    bet = bet_for_craps(money)

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dsum = dice1 + dice2

    print 'You rolled', dsum

    if (dsum == 7) or (dsum == 11):
        print 'You win!'
        money += bet
        return money

    elif (dsum == 2) or (dsum == 3) or (dsum == 12):
        print 'You Lose...'
        money -= bet
        return money

    else:

        nextRound = True
        print 'hit RETURN for next roll'
        while nextRound:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            dsum2 = dice1 + dice2

            ret = raw_input('')
            print 'You rolled', dsum2


            if dsum2 == dsum:
                print 'You win!'
                money += bet
                return money

            elif dsum2 == 7:
                print 'You lose...'
                money -= bet
                return money

def inBetween(money):

    num1 = random.randint(1,13)
    num2 = random.randint(1,13)
    while num1 == num2 or num1+1 == num2 or num2+1 == num1:
        num1 = random.randint(1,13)
        num2 = random.randint(1,13)


    legitOptions = []

    if num1>num2:
        print 'The numbers are', num2,num1
        for i in range(num2+1,num1):
            legitOptions.append(i)

    else:
        print 'The numbers are', num1,num2
        for i in range(num1+1,num2):
            legitOptions.append(i)

    bet = bet_for_inBetween(money)

    betNum = random.randint(1,13)
    print 'The number was ',betNum

    if betNum in legitOptions:
        print 'You win!'
        money += bet
    else:
        print 'You lose...'
        money -= bet

    return money

def directions():

    di = True
    while di:
        print '\nWelcome to directions!'
        print '\nHere are the games:\n'
        print '1 - Guessing Game'
        print '2 - Craps'
        print '3 - In Between\n'
        print 'Other:\n4 - Directions'
        print '5 - Quit\n'

        about = raw_input('enter the number corresponding to the game you would like to learn about: ')

        aboutValues = ['1','2','3','4','5']

        while about not in aboutValues:
            print 'please choose an option'
            about = raw_input("enter the number corresponding to your choice: ")

        if about == '1':
            print '\nGuessing Game:\n'
            print 'comming soon'
            exit = raw_input('Hit "RETURN" to exit this menu')
        elif about == '2':
            print '\nCraps:\n'
            print 'Rules for Craps:\nCraps is a dice-rolling game (Ever see Guys and Dolls?).\nYou bet and then roll.\nIf you roll 7 or 11, the you win.\nIf you roll 2, 3 or 12, you lose.\nIf anything else, the you roll again, and continue rolling, until one of the following is true:\n\nYou roll 7:  you loose\nYou roll what you rolled on your first roll:  you win.\n'
            exit = raw_input('Hit "RETURN" to exit this menu')
        elif about == '3':
            print '\nIn Between:\n'
            print "Two numbers are picked at random, from 1-13.\nThen you bet that the next number will be in between the first 2 values.\nIf it is, you win.\nIf it is not between (and that includes if it is one of the numbers) you lose.\n"
            exit = raw_input('Hit "RETURN" to exit this menu')
        elif about == '4':
            print '\nDirections:\n'
            print 'Whoa, this is pretty meta...\nDirections is just the place you can learn how to play the many games we offer!\nBut you already knew that!\n'
            exit = raw_input('Hit "RETURN" to exit this menu')
        else:
            di = False

def menu(money):

    balance = 'your balance: $' + str(money)
    if money <= 0:
        return

    print balance
    print ''
    print 'Games:\n1 - Guessing Game'
    print '2 - Craps'
    print '3 - In Between\n'
    print 'Other:\n4 - Directions'
    print '5 - Quit'
    print ''


    choiceValues = ['1','2','3','4','5']

    choice = raw_input("enter the number corresponding to your choice: ")

    w = True

    while w:
        if choice in choiceValues:
            w = False
            return choice
        else:
            print 'please choose an option'
            choice = raw_input("enter the number corresponding to your choice: ")
