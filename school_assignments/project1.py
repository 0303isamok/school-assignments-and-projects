# Made by Isam Kartit and Ghulam Hussain Jarwar
import random

repeat_game = "YES" 



while repeat_game == "YES":
    number = random.randint(1,100)
    tried = False
    attempts = 0

    print("I made up a whole number between 1 and 100 (no decimals), guess it with 5 tries")

    while attempts < 5 and not tried:
        guess = int(input("Enter your guess:"))
        attempts += 1
        if guess == number:
            tried = True
            print("Congratulations you guessed the right number in ", attempts, " attempts!")
            print("The correct number was ", number,"!")
        else:
            if guess < number:
                print("Too low")
                print(5 - attempts, "attempts remaining")
            else:
                print("Too high")
                print(5 - attempts, "attempts remaining")

    if not tried:
        print("You did not manage to guess the number. You have reached the guessing limit")
        print("The correct number was", number)
    repeat_game = input("Do you wanna play again? (YES/NO)")
    repeat_game = repeat_game.upper()
    
print("Good job, thanks for playing my game")
