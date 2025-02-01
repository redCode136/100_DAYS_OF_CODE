import random

def compare(comp_score, user_score):
    if user_score > 21:
        return "You went over 21. You lose!"
    elif comp_score > 21:
        return "Computer went over 21. You win!"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif comp_score == 0:
        return "Computer has Blackjack. You lose!"
    elif user_score == comp_score:
        return "It's a draw!"
    elif comp_score > user_score:
        return "Computer wins!"
    else:
        return "You win!"

def calculate_sum(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Convert Ace from 11 to 1
    return sum(cards)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_sum(user_cards)
        computer_score = calculate_sum(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn to draw cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_sum(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(computer_score, user_score))

# Start the game
play_game()