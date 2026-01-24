import random

def get_value():
    player_choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
    options = ["rock", "paper", "scissors"]
    
    if player_choice not in options:
        return None 
    
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    print(f"You choose {player.capitalize()}, Computer chooses {computer.capitalize()}")
    
    if player == computer:
        return "It's a tie!!"
    
    if player == "rock":
        if computer == "paper":
            return "Paper covers Rock! You lose."
        else:
            return "Rock breaks Scissors! You win."
    
    if player == "paper":
        if computer == "rock":
            return "Paper covers Rock! You win."
        else:
            return "Scissors cuts Paper! You lose."
    
    if player == "scissors":
        if computer == "paper":
            return "Scissors cuts Paper! You win."
        else:
            return "Rock breaks Scissors! You lose."

choices = get_value()

if choices is None:
    print("Invalid input! Please enter Rock, Paper, or Scissors.")
else:
    result = check_win(choices["player"], choices["computer"])
    print(result)
