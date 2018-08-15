#!/usr/local/bin/python3
# Last edited: 18/08/14

import sys
import math
from random import randint

# Constants
CRITICAL_FAIL = 20
ALWAYS_FAIL = 19

def roll(argv):
    if (len(argv) == 0 or "--help" in argv or "-h" in argv):
        print_help()
        sys.exit('help')

    # Roll characteristics
    die_range = 20
    dice_number = 1
    difficulty = 4

    # Get the arguments
    roll_type = argv.pop(0)
    if (roll_type == "d20"):
        die_range = 20
        dice_number = 1
        difficulty = int(argv.pop(0))
    elif (roll_type == "d6"):
        die_range = 6
        dice_number = int(argv.pop(0))
        difficulty = 4
    else:
        print("Error: The accepted values are 'd20' and 'd6'")
        sys.exit('wrong input')

    while len(argv) > 0:
        if (argv[0] == "--difficulty" or argv[0] == "-d"):
            argv.pop(0)
            difficulty = int(argv.pop(0))
    print("Roll type:", roll_type, "/ Dice number:", dice_number, "/ Difficulty:", difficulty)

    # Show results
    class bcolors:
        PURPLE = '\033[95m'
        GREY = '\033[92m'
        ORANGE = '\033[91m'
        LIGHT_RED = '\033[35m'
        YELLOW = '\033[0;32m'
        BLUE = '\033[0;34m'
        TEST = '\033[0;36m'

    # Find the result and print it out
    if (roll_type == "d20"):
        die_roll = randint(1,die_range)
        roll_result = "not assigned"
        victory_dice = 0
        victory_points = 0
        if (die_roll > difficulty) or (die_roll >=19):
            if (die_roll == CRITICAL_FAIL):
                font_roll_color = bcolors.GREY
                font_result_color = bcolors.PURPLE
                roll_result = "CRITICAL FAIL!!"
            else:
                font_roll_color = bcolors.GREY
                font_result_color = bcolors.BLUE
                roll_result  = "FAIL"
        else:
            font_roll_color = bcolors.YELLOW
            font_result_color = bcolors.ORANGE
            victory_dice = math.ceil( (die_roll-2)/3 )
            victory_points = max( 1, victory_dice )
            bonus_dice = max( 0, math.ceil((difficulty-20)/3 ))
            if (die_roll == difficulty):
                victory_points *= 2
                victory_dice *= 2
            victory_dice += bonus_dice
            roll_result = "+"+str(victory_points)+" VP / +"+str(victory_dice)+" dice"
        print(font_roll_color, die_roll, bcolors.LIGHT_RED, "-->", font_result_color, roll_result, bcolors.GREY)
        return(   { 'die_range': die_range,
                    'dice_number': dice_number,
                    'difficulty': difficulty,
                    'die_roll': die_roll,
                    'victory_points': victory_points,
                    'victory_dice': victory_dice }   )

    elif (roll_type == "d6"):
        results = []
        success_rolls = 0
        for _ in range (0, dice_number):
            die_roll = randint(1,die_range)
            results.append(die_roll)
            if (die_roll <= difficulty):
                success_rolls += 1
        results.sort()
        print(bcolors.YELLOW, results[0:success_rolls], bcolors.GREY, results[success_rolls:], bcolors.LIGHT_RED, "-->", bcolors.ORANGE, success_rolls, bcolors.GREY)
        return(   { 'die_range': die_range,
                    'dice_number': dice_number,
                    'difficulty': difficulty,
                    'die_roll': die_roll,
                    'success_rolls': success_rolls }   )

def print_help():
    print("    Pass the type of die to roll, followed by either")
    print("      - d20 difficulty")
    print("      - d6  number of dice")
    print("    Other options:")
    print("      -d, --difficulty, set the difficulty, relevant for the 'd6' dice sometimes.")
    print("    Examples:")
    print("        ./roll d20 15")
    print("        ./roll d20 24")
    print("        ./roll d6 6")
    print("        ./roll d6 7 -d 3")

if __name__ == "__main__":
   roll(sys.argv[1:])
