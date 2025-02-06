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


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(u_score):
    if sum(u_score)==21 :
        return 0
    elif 11 in u_score and sum(u_score)>21:
        u_score.remove(11)
        u_score.append(1)
    return sum(u_score)


def play_game():
    user_card=[]
    computer_card=[]
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    game_is_over= False
    while not game_is_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score>21:
            game_is_over = True
        else:
            user_choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_choice == 'y':
                user_card.append(deal_card())
            else:
                game_is_over = True
            # Computer's turn to draw cards
            while computer_score != 0 and computer_score < 17:
                computer_card.append(deal_card())
                computer_score = calculate_score(computer_card)
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(computer_score, user_score))

play_game()