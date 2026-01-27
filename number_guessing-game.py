#A simple python program where the user has to guess the number picked by computer withing a specified range by minimum guess.

import random
import math

def user_input_and_mode():
    
    print("""
-:RULES TO KNOW:-
    1) First Enter your Starting & Ending number for the range from which
    the computer is going to choose a random number.
    2) Then choose the mode.
    3) Depending upon the mode u have choosen you are given chances, you
    have to guess the correct number withing those number of guesses.\n""")
    
    a, b = input("Now enter the Starting and Ending of the range, seperated by a Single Space(e.g. ->2 3): ").split()

    start_range = int(a)
    end_range = int(b)

    comp_num = random.randint(start_range, end_range)
    
    if (start_range >= 0 and end_range>0):
        count = ((len(range(start_range,end_range)))+1)

        print("-:CHOOSE YOUR MODE:-\nEasy\tMedium\tHard")
        a = input("=>").lower()

        if a == 'easy':
            chances_e = (math.ceil(math.log10(count)) * 10)
            print("-:EASY MODE:-")
            guess(start_range, end_range, comp_num, chances_e)
        elif a == 'medium':
            chances_m = (math.ceil(math.log10(count)) * 7)
            print("-:MEDIUM MODE:-")
            guess(start_range, end_range, comp_num, chances_m)
        elif a == 'hard':
            chances_h = (math.ceil(math.log10(count)) * 5)
            print("-:HARD MODE:-")
            guess(start_range, end_range, comp_num, chances_h)
        else:
            print("Oops!Enter a Correct Choice!")
    else:
        print("Enter Correct Range!!")
        

def guess(a, b, c, d):
    
    print(f"Computer Has choosen a Number from your given range({a}, {b}). You have {d} chances to guess that number!! BEST OF LUCK :)")
    temp = 0
    while temp != d:
        num = int(input("Guess What the number can be: "))
        temp += 1  
        if temp == 1 and num == c:
            print("Excellent!! You got it in first Chance!")
            exit()
        elif num == c:
            print(f"Nice!! You took {temp} chances to guess the number.")
            exit()
        elif num > c:
            print(f"OHH!!!u are Flying too High, Go-Down SOLDIER....{d-temp} chances left!!")
        elif num < c:
            print(f"I know u have potential,FLY-HIGH SOLDIER.....{d-temp} chances left!!")
        else:
            print("Better Luck next time!! Try Again....:)")
            exit()

if __name__ == "__main__":
    user_input_and_mode()
