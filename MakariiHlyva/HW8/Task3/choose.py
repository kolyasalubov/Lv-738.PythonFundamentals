#--------This function helps user to choose figure, and return name of function for calculating it's area--------#

from functions import *

def choose_menu():

    """This menu will help you to choose figure which area you want to calculate"""

    print("For rectangle please eneter 'r' or 'R'\nFor triangle please enter 't' or 'T'\nFor circle please enter 'c' or 'C'\n")
    while True:
        try:
            type = str(input("Youre choose is: "))
            match type:
                case 'R' | 'r':
                    return "rectangle_area"
                case 't' | 'T':
                    return "triangle_area"
                case 'c' | 'C':
                    return "circle_area"
                case other:
                    raise ValueError
        except ValueError:
            print("Please choose figure type")