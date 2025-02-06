import random

def set_difficulty(difficulty):
    if difficulty == 'hard':
        return 5
    elif difficulty == 'medium':
        return 7
    else:
        return 10

def check_ergebnis(guess, live, genNumber):
    if guess > genNumber:
        print("too High!")
    elif guess < genNumber:
        print("Too Low!")
    else:
        print(f"Guessed the right Number. \n The right number was: {genNumber}. You won!!")

def game_play():
    genNumber = random.randint(1, 100)  # Zufallszahl für jedes Spiel neu
    guess = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
    attempts = set_difficulty(difficulty)

    while guess != genNumber and attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess:"))
        check_ergebnis(guess, attempts, genNumber)
        attempts -= 1
        if attempts == 0 and genNumber != guess:
            print(f"You lose. The right answer was: {genNumber}")
            return

game_play()
