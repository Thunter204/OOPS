# Programmer: Toni Hunter
# RUID: 187009925
# Date: 01/26/2022
#
# File: problem2.py
#
# Program Description: write a program to play craps to allow wagering; The player starts with an
# initial bank balance of $1000. Each game starts with a wager (no bigger than the current bank
# balance). After one game, the bank balance is updated and the player is allowed to play again,
# repeatedly, until she quits, or the bank balance falls to $0.
## Write a function called roll_dice with no parameters, The function rolls two dice and return the
# sum of the result randint(a, b) returns a random integer N such that a ≤ N ≤ b.
## Second function called play_one_game plays a single game of craps, prints out
# sentences informing player about the sequence of actions taking place in the game, It returns an
# integer value of 1 if the player wins the game, and in integer value of 0 if the player loses
# the game.
# third function called craps,  uses a while  uses a while loop to allow the player to play as many
# rounds of craps as she wants, as long as the bank balance is not $0. First prompt the user to enter
# a wager. If the wager is greater than the bank balance, repeatedly prompt the player to re-enter the
# wager until a valid wager is entered. should call play_one_game, If the new balance is $0, print a
# message ("Sorry, you’re broke!"), and quit. If the player quits with a bank balance greater than $0,
# print a congratulatory message if money was made and a sympathetic message if money was lost.
import random


def roll_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    N = a + b
    return N  # returned to be called


def play_one_game():
    num = roll_dice()
    if num in (7, 11):
        print()
        print("you rolled {}".format(num))
        print("you win!!")
        print()
        return 1
    elif num in (2, 3, 12):
        print()
        print("you rolled {}".format(num))
        print("Sorry, you lose!")
        print()
        return 0
    else:
        print()
        print("you rolled {}".format(num))
        print("your point is {}".format(num))
        print()
        nnum = roll_dice()
        if nnum == 7:
            print("you rolled {}".format(nnum))
            print("Sorry, you lose!")
            return 0
        while nnum != (7, num):
            nnum = roll_dice()
            print("you rolled {}".format(nnum))
            if nnum == num:
                print("you win!!")
                return 1
            elif nnum == 7:
                print("Sorry, you lose!")
                return 0


def craps():
    newG = True
    print("Your initial balance is $1000 ")
    print()
    wager = int(input("what is your wager? "))
    print("okay, lets play.")
    play = play_one_game()

    while newG:
        inbal = 1000
        while wager > inbal:
            wager = int(input("cannot wager more than ${}.".format(inbal)
                              + " Re-enter wager: "))
            print("okay, lets play.")
            print()
            play = play_one_game()
        if play == 0:
            inbal -= wager
            print()
            print("your new balance is ${}".format(inbal))
#            FIXXME
#            print("return 0, inbal:{}, wager:{}".format(inbal, wager))
#            loop not saving balance, accessing wrong if/elif
            print()
            newG = input("Do you want to play again? [y/n] ")
            print()
        elif play == 1:
            inbal += wager
            print("Your new bank balance is ${}".format(inbal))
#               FIXXME
#            print("return 1, inbal:{}, wager:{}".format(inbal, wager))
#            loop not saving balance, accessing wrong if/elif
            print()
            newG = input("Do you want to play again? [y/n] ")
            print()

        if inbal == 0:
            print("No money left! Try again")
        if newG == 'y':
            wager = int(input("What is your wager? "))
            play_one_game()
        else:
            newG = False
            if inbal < 1000:
                print("Sorry you lost money. Better luck next time!")
            else:
                print("Great Job, Good Game!")


print("{:^50}".format('-' * 30))
print("{:^50}".format('Welcome to the Craps program'))
print("{:^50}".format('-' * 30))
print()
craps()
