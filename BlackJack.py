import random

from ascii_art import logo

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4
game_over = False
player_cards = []
computer_cards = []
final_message = ""

def pick_a_card():
    card = random.choice(deck)
    deck.remove(card)
    return card

def start_hand():
    player_cards.append(pick_a_card())
    player_cards.append(pick_a_card())
    computer_cards.append(pick_a_card())
    computer_cards.append(pick_a_card())

def calculate_score(current_score, card):
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

def print_result():
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

print(logo)
start_hand()
player_score = calculate_score(0, player_cards[0])
player_score = calculate_score(player_score, player_cards[1])
computer_score = calculate_score(0, computer_cards[0])
computer_score = calculate_score(computer_score, computer_cards[1])

print_result()

while not game_over:
    need_card = input_another_card()

    if need_card == 'y':
        player_cards.append(pick_a_card())
        player_score = calculate_score(player_score, player_cards[-1])

        if player_score > 21:
            final_message = "You went over. You lose."
            game_over = True

        print_result()
    else:
        while computer_score < 17:
            computer_cards.append(pick_a_card())
            computer_score = calculate_score(computer_score, computer_cards[-1])
            print_result()
            if computer_score > 21:
                final_message = "You win!"
        game_over = True

if not final_message:
    if player_score > computer_score:
        final_message = "You win!"
    elif player_score == computer_score:
        final_message = "Draw!"
    else:
        final_message = "You lose."

print()
print("Game finished")
print(f"Your final hand: {player_cards}, final score: {player_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(final_message)