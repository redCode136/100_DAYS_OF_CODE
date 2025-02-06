import logo
import game_data
import random

def format_data(account):
    """Format and display account data."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def check_answer(guess, follower_a, follower_b):
    """Check if the user's guess is correct."""
    return guess == "a" if follower_a["follower_count"] > follower_b["follower_count"] else guess == "b"

def get_random_account():
    """Return a random account from game data."""
    return random.choice(game_data.data)

def game():
    """Main game logic."""
    print(logo.logo)
    print("Welcome to the Game Higher vs Lower\n")

    score = 0
    game_over = False
    account_b = get_random_account()

    while not game_over:
        account_a = account_b
        account_b = get_random_account()

        # Ensure the two accounts are different
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Round: {score}\n")
        print(f"Compare A: {format_data(account_a)}")
        print(logo.vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B':\n").lower()

        if check_answer(guess, account_a, account_b):
            score += 1
            print(f"Correct! Current score: {score}\n")
        else:
            print(logo.lose)
            game_over = True

    print(f"Your final score is {score}")

# Run the game
game()