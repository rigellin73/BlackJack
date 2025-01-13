import random

from ascii_art import logo

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4
game_over = False
player_cards = []
computer_cards = []
player_score = -1
computer_score = -1
final_message = ""

def deal_card():
    """Pick a random card from the deck, remove it from the deck and return"""

    card = random.choice(deck)
    deck.remove(card)
    return card

def update_score(current_score, card):
    """Add card value to the current score. Ace can be 11 or 1. Jack, Queen or King add 10 points to the score.
    Return updated score"""

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

def user_wants_card():
    """Ask player if they want to deal another card. Return boolean value"""

    answer = input("Type 'y' to get another card, type 'n' to pass: ")
    while not (answer == "y" or answer == "n"):
        print("Unexpected input")
        answer = input("Type 'y' to get another card, type 'n' to pass: ")
    if answer == "y":
        return True
    return False

def print_result():
    """Print current information: player hand, player score and computer's first card"""

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    #print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

print(logo)

for _ in range(2):
    player_cards.append(deal_card())
    player_score = update_score(player_score, player_cards[-1])
    computer_cards.append(deal_card())
    computer_score = update_score(computer_score, computer_cards[-1])

print_result()

"""Check for blackjack before dealing another cards"""

if player_score == 21 and computer_score == 21:
    game_over = True
    final_message = "Push. You both have blackjacks."
elif player_score == 21:
    game_over = True
    final_message = "Blackjack! You win!"
elif computer_score == 21:
    game_over = True
    final_message = "Computer has blackjack. You lose."

while not game_over:

    if user_wants_card():
        player_cards.append(deal_card())
        player_score = update_score(player_score, player_cards[-1])

        if player_score > 21:
            final_message = "You went over. You lose."
            game_over = True

        print_result()
    else:
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = update_score(computer_score, computer_cards[-1])
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