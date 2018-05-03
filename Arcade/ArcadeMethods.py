# Lucas and Ava Team method assignment

import random

from ArcadeMethods2 import *


def play():
    money = 500
    choice = 'indetermined'
    while (choice != "5") and (money != 0):
        choice = menu(money)
        playAgain = 'yes'

        if choice == '1':

            play = True
            while play and money != 0:
                money = guessingGame(money)
                currMoney = 'You now have $' + str(money)
                print currMoney
                if money <= 0:
                    print 'You do not have enough money to play again'
                    play = False
                else:
                    playAgain = raw_input('Play again? yes or no: ')
                    if len(playAgain) > 0 and playAgain.lower()[0] != 'y':
                        play = False

        elif choice == '2':

            play = True
            while play and money != 0:
                money = craps(money)
                currMoney = 'You now have $' + str(money)
                print currMoney
                if money != 0:
                    playAgain = raw_input('Play again? yes or no: ')
                    if len(playAgain) > 0 and playAgain.lower()[0] != 'y':
                        play = False

        elif choice == '3':

            play = True
            while play and money != 0:
                money = inBetween(money)
                currMoney = 'You now have $' + str(money)
                print currMoney
                if money != 0:
                    playAgain = raw_input('Play again? yes or no: ')
                    if len(playAgain) > 0 and playAgain.lower()[0] != 'y':
                        play = False

        elif choice == '4':
            directions()

        if money == 0:
            print 'You ran out of money...'

    print '\nThank you for playing!'
    return money

if __name__ == "__main__":
    money = play()
