from deck import Deck
from player import Player
from dealer import Dealer
import time

deck = Deck()
dealer = Dealer(deck)

player_names = []

taking_names = True

while taking_names:
    user_input = input("Name a player? ").title()
    if user_input == "Done":
        break
    player_names.append(user_input)

players = [dealer]

for name in player_names:
    players.append(Player(name))

for _ in range(2):
    for player in players:
        dealer.deal_card(player.hand)
        player.update_score()

playing = True

while playing:
    for i in range(1, len(players)):
        player_turn = True
        print(f"The computers first card is: {dealer.hand[0]["card_name"]} {dealer.hand[0]["card_value"]}")
        while player_turn:
            print(f"{players[i].name} your score is {players[i].score}")
            print(f"{players[i].name} your hand is {players[i].hand}")
            player_choice = input("Hit or Stand: ").title()

            if player_choice == "Stand" or players[i].score == 21:
                print(f"{players[i].hand}")
                print(f"{players[i].name} stood with a score of {players[i].score}\n")
                player_turn = False

            if player_choice == "Hit":
                dealer.deal_card(players[i].hand)
                print(f"{players[i].name} hits and draws {players[i].hand[-1]}")
                players[i].update_score()

            if players[i].is_player_bust():
                print(f"{players[i].hand}")
                print(f"{players[i].name} busted with a score of {players[i].score}\n")
                player_turn = False

    dealer_turn = True
    while dealer_turn:
        time.sleep(0.5)
        print(f"The computers cards are {dealer.hand}")
        print(f"With a score of {dealer.score}")
        if dealer.stand():
            dealer_turn = False
        dealer.deal_card(dealer.hand)
        print(f"{dealer.name} hits and draws {dealer.hand[-1]}")
        dealer.update_score()
    print("\n")
    for player in players[1: -1]:
        if dealer.score < player.score < 22:
            print(f"{player.name} Wins with a score of {player.score}")
        elif player.score == dealer.score:
            print(f"{player.name} drew with the dealer")
        else:
            print(f"{player.name} loses with a score of {player.score}")

    playing = False
