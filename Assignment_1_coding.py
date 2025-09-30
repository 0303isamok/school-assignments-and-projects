import random

repeat_game = "yes"


while repeat_game == "yes":
    number = random.randint(1,100)
    tried = False
    attempts = 0

    print("I made up a number between 1 and 100, guess it with 5 tries if you can")

    while attempts < 5 and not tried:
        guess = int(input("Enter your guess"))
        attempts += 1
        if guess == number:
            tried = True
            print(f"Congratulations you guessed the right number in ", attempts, " attempts!")
            print(f"The correct number was ", number,"!")
        else:
            if guess < number:
                print("Too low")
            else:
                print("Too high")

    if not tried:
        print("You did not manage to guess the number. You have reached the guessing limit")
        print("The correct number was", number)
    repeat_game = input("Do you wanna play again? (yes/no)")
    repeat_game = repeat_game.lower()
    
print("Good job, thanks for playing my game broski")

            
