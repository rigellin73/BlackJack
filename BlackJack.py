import random

from ascii_art import logo

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4
game_over = False
player_cards = []
computer_cards = []

def pick_a_card():
    card = random.choice(deck)
    deck.remove(card)
    return card

def start_hand():
    player_cards.append(pick_a_card())
    player_cards.append(pick_a_card())
    computer_cards.append(pick_a_card())
    computer_cards.append(pick_a_card())

def calculate_score(current_score, new_cards):
    for card in new_cards:
        if card == "A":
            if current_score + 11 > 21:
                current_score += 1
            else:
                current_score += 11
        elif card == "J" or card == "Q" or card == "K":
            current_score += 10
        else:
            current_score += card

    return current_score

def input_another_card():
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while not (another_card == "y" or another_card == "n"):
        print("Unexpected input")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    return another_card

print(logo)
start_hand()
player_score = calculate_score(0, player_cards)
computer_score = calculate_score(0, computer_cards)

while not game_over:
    need_card = input_another_card()

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer cards: {computer_cards}, computer score: {computer_score}")
    #print(deck)

    if player_score > 21:
        print("You lose!")
        game_over = True

    if computer_score > 21:
        print("You win!")
        game_over = True
