import random as rd

def main():
    again = "yes"
    while again == "yes":
        print("####################")
        print("ROCK PAPER SCISSORS!")
        print("####################")
        shapes = ["rock", "paper", "scissors"]
        
        while True:
            player_choice = get_player_choice(shapes)
            computer_choice = get_computer_choice(shapes)
            print(f"player: {player_choice} computer: {computer_choice}")
            result = winner(player_choice, computer_choice)
            print(result)

            again = input("do you want to play again? (yes/no)").strip().lower()
            while again != "yes" and again != "no":
                print("invalid user input")
                again = input("do you want to play again? (yes/no)").strip().lower()
            if again == "no":
                break
        


def get_computer_choice(shapes):
    return rd.choice(shapes)

def get_player_choice(shapes):
    while True:
        player_choice = input("you can choose between\n what do you want to throw?")
        if player_choice in shapes:
            return player_choice
        else:
            return "invalid user input"

def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "its a tie!"

    elif player_choice == "rock" and computer_choice == "scissors" or player_choice == "scissors" and computer_choice == "paper" or player_choice == "paper" and computer_choice == "rock":
        return "player won the game!"
    else:
        return "computer won :-("
    
main()