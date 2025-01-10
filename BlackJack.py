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

print(logo)

while not game_over:
    start_hand()

    print(f"Your cards: {player_cards}")
    print(f"Computer cards: {computer_cards}")
    print(deck)

    game_over = True
