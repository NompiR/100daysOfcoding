import random


def cards():
    card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    random_card = random.choice(card)
    return random_card


user_card = []
computer_card = []
u_score = -1
c_score = -1

for _ in range(2):
    user_card.append(cards())
    computer_card.append(cards())



def add_total(all_cards):
    if sum(all_cards) == 21 and len(all_cards) == 2:
        return 0
    if sum(all_cards) > 21 and 11 in all_cards:
        all_cards.remove(11)
        all_cards.append(1)

    return sum(all_cards)


"""def calculate(card_a):
    if sum(card_a) == 21 and len(card_a) == 2:
        return 0
    if sum(card_a) > 21 and 11 in card_a:
        card_a.remove(11)
        card_a.append(1)
    return sum(card_a)"""


def compare(c_total, u_total):
    if c_total == u_total:
        return "It's a draw"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif c_total > 21:
        return  "Dealer went over, You win"
    elif u_total > 21:
        return "You went over, you lose"
    elif u_total > c_total:
        return "You win"
    else:
        return "You lose, Dealer Win"


is_game_on = False
while not is_game_on:

    u_score = add_total(user_card)
    c_score = add_total(computer_card)


    print(f"Your cards: {user_card}, current score: {u_score}")
    print(f"Computer's first card: {computer_card[0]}")



    if u_score == 0 or c_score == 0 or u_score >= 21:
        #print(f"Your final cards: {user_card}, final score: {u_score}")
        #print(f"Computer's final card: {computer_card}, final score: {c_score}")
        is_game_on = True

    else:
        choices = input("Type Y to continue, Type n to pass: ")[0].lower()
        if choices == 'y':
            user_card.append(cards())
        else:
            is_game_on = True


while c_score != 0 and c_score < 17:
    computer_card.append(cards())
    c_score = add_total(computer_card)

print("\n")
print(f"Your final cards at hand: {user_card}, Your final score: {u_score}")
print(f"Computers final cards at hand: {computer_card},  Computer's final score: {c_score}")
print(compare(c_score, u_score))




"""
user_total = add_total(user_card)
            print(f"Your final hand cards: {user_card}, final score: {add_total(user_card)}")
            print(f"Computer's final hand card: {computer_card}, final score: {add_total(computer_card)}")
        else:
            computer_card.append(cards())
            comp_total = add_total(computer_card)
            print(f"Your final hand cards: {user_card}, final score: {add_total(user_card)}")
            print(f"Computer's final hand card: {computer_card}, final score: {comp_total}")
            is_game_on = False

    print(compare(comp_total, user_total))

"""

"""
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) >= 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw "
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over, you lose"
    elif c_score > 21:
        return "Opponent went over, You Win!"
    elif u_score > c_score:
        return "You Win! :-D"
    else:
        return "You lose "


user_card = []
computer_card = []
computer_score = -1
user_score = -1

is_game_over = False


for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)


    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer card {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_deal = input("Type y to get another card, n to pass: ")[0]
        if user_deal == 'y':
            user_card.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)
    #print(f"Comp score {computer_score}")


print(f"Your final cards: {user_card} Your final score: {user_score}")
print(f"Computer's final cards: {computer_card} Computer's final score: {computer_score}")
print(compare(user_score, computer_score))





user_score = sum(user_card)
    computer_score = sum(computer_card)
    return (user_score, computer_score)
    
"""