#A simple python program where the user has to guess the number picked by computer withing a specified range by minimum guess.

import random

def user_input():
    a, b = input("Enter the Start and Stop number seperated by a Single Space(e.g. ->2 3): ").split()

    start_range = int(a)
    end_range = int(b)

    count = len(range(start_range,end_range))

    if count > 0:
        

    
    print(count)
    comp_num = random.randint(start_range, end_range)

    guess(start_range, end_range, comp_num)


def guess(a, b, c):
    
    print(f"Computer Has choosen a Number from your given range({a}, {b}). You have n chances to guess that number!! BEST OF LUCK :)")
    temp = 0
    while temp < 5:
        num = int(input("Guess What the number can be: "))
        temp += 1  
        if temp == 1 and num == c:
            print("Excellent!! You got it in first Chance!")
            break
        elif num == c:
            print("You took ",temp," guesses to find the number.")
            break
        elif num > c:
            print("Your expectations are high ha! Too Big for my number.")
        elif num < c:
            print("Your mentality is low man* Increase your thoughts.")
   

if __name__ == "__main__":
    user_input()
