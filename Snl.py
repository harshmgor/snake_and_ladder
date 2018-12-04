# code for Snakes and Ladder Game

import time
import random
import os

snake_squares={}
ladder_squares={}

dice=[0]

# to roll a dice
def Roll_dice():
    return random.randint(1,6)

# to create dynamic locations of snakes and ladders
def dynamicSnL():
    scount = 12
    lcount = 12
    while len(snake_squares) < scount and len(ladder_squares) < lcount:
        # snake
        if scount > 0:
            key = random.randint(11, 99)
            value = random.randint(1, key)
            if value not in ladder_squares:
                snake_squares[key] = value
                scount = scount - 1
        # ladder
        if lcount > 0:
            key = random.randint(2, 90)
            value = random.randint(key, 99)
            if key not in snake_squares:
                ladder_squares[key] = value
                lcount = lcount - 1

# to move player
def Move(Player, value):
    snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
    ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}
    Throw = Roll_dice()
    dice[0] = Throw
    if Player == 1:
        num = value + Throw
        print("Player 1 Rolled a", Throw, "And is now on", num)
    if Player == 2:
        num = value + Throw
        print("Player 2 Rolled a", Throw, "And is now on", num)

    if num in snake_squares:
        print("\nPlayer got bitten by a snake at", num, "and is now on", snake_squares[num])
        num = snake_squares[num]
    elif num in ladder_squares:
        print("\nPlayer climbed a ladder at", num, "and is now on", ladder_squares[num])
        num = ladder_squares[num]
    else:
        print("")
    return num

# to displaye the location of snakes and ladders
def disp():
    print('\nSnakes\n')
    for x in snake_squares:
        print('{', x, '} -> {', snake_squares[x], '}')

    print('\nLadders\n')
    for x in ladder_squares:
        print('{', x, '} -> {', ladder_squares[x], '}')

input("Press Enter to Start...")
Num1 = 0
Num2 = 0

dynamicSnL()

x = 0
while Num1 < 100 and Num2 < 100:
    while x < 2:
        x=x+1
        os.system('cls') #for windows

        disp()

        print("\nPrev Dice :", dice[0])
        print('\nPlayer 1 :', Num1)
        print('Player 2 :', Num2, '\n')


        if x == 1:
            Num1 = Move(1, Num1)
            if Num1 > 99:
                print("Player 1 WINS!")
                time.sleep(3)
                exit()
        if x == 2:
            Num2 = Move(2, Num2)
            if Num2 > 99:
                print("Player 2 WINS!")
                time.sleep(3)
                exit()
        input("\nPress Enter")
    x=0
