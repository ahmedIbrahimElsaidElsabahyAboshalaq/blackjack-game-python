from art import logo
import random
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def the_card():
    return random.choice(cards)
def sum_card(cards):
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)
def Who_win(dealer_card, player_card):
    if sum_card(dealer_card) > sum_card(player_card):
         print(f"You Lose! your sum is:{sum_card(player_card)} and dealer sum is:{sum_card(dealer_card)}")
    elif sum_card(player_card) == sum_card(dealer_card):
         print(f"Withdraw! your sum is:{sum_card(player_card)} and dealer sum is:{sum_card(dealer_card)}")

    else:
        print(f"You Win! your sum is:{sum_card(player_card)} and dealer sum is:{sum_card(dealer_card)}")



game_over = False
while not game_over:
    player_lost = False
    dealer_card = []
    player_card = []
    for i in range(2):
        dealer_card.append(the_card())
        player_card.append(the_card())
    print(f"your cards:{player_card}")
    print(f"Dealer card first paper: {dealer_card[0]}")
    print(f"Sum of your papers: {sum_card(player_card)}")
    while True:
        play=input("Do you want to hit or stand (h/s): ").lower()
        if play == "h":
            player_card.append(the_card())
            if sum_card(player_card) > 21:
                print(f"You Lose your sum is:{sum_card(player_card)}")
                player_lost = True
                break

            print(f"Sum of your card: {sum_card(player_card)}")
        else:
            print(f"Sum of your card: {sum_card(player_card)}")
            break
    while not player_lost:
        if sum_card(dealer_card)<17:
            dealer_card.append(the_card())
            if sum_card(dealer_card) > 21:
                 print(f"You Win your sum is:{sum_card(player_card)} and dealer sum is:{sum_card(dealer_card)}")
                 print(f"Dealer cards: {dealer_card}")
                 break


        else:
            Who_win(dealer_card, player_card)
            break
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        game_over = False
    else:

        game_over = True




