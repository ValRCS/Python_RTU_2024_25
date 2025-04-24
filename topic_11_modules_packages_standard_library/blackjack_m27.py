# now let's use CardDeck to play a game of blackjack

# so simple blackjack rules are:
# 1. player and dealer get two cards each, player can see both of his cards and one of the dealer's cards
# 2. player can hit (get another card) or stand (keep his cards and end his turn)
# 3. player can hit as many times as he wants, but if his cards exceed 21, he loses (busts)
# 4. dealer must hit until his cards are at least 17, then he must stand

# 5. if player and dealer have the same value, it's a push (draw)
# 6. if player has a higher value than dealer, he wins

# so let's import CardDeck class from card_deck_m27.py and use it to play a game of blackjack
from card_deck_m27 import CardDeck # we just need the CardDeck class from card_deck_m27.py


# let's make a function that will calculate the value of the hand
def get_hand_value(hand): # hand will be list of tuples (rank, suit)
    value = 0
    aces = 0
    for card in hand:
        if card[0] in ("J", "Q", "K"): # so card[0] is the rank of the card
            # face cards are worth 10 points
            value += 10
        elif card[0] == "A":
            aces += 1
            value += 11 # we will handle aces later
        else:
            value += int(card[0])
    # now let's handle aces, if value is over 21, we will subtract 10 for each ace until value is under 21 or we run out of aces
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

# now we can make the main function that will play the game
def play_blackjack():
    # let's make a deck of cards
    # deck = CardDeck(shuffle=True, seed=42) # we will use the same seed for testing purposes
    deck = CardDeck(shuffle=True ) # we will use the same seed for testing purposes
    # let's make a player and dealer hands
    player_hand = [deck.draw(), deck.draw()]
    dealer_hand = [deck.draw(), deck.draw()]
    
    # let's show the player his hand and one of the dealer's cards
    print(f"Your hand: {player_hand}, value: {get_hand_value(player_hand)}")
    print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
    
    # now let's ask the player if he wants to hit or stand
    while True:
        action = input("Do you want to hit (h) or stand (s)? ").lower()
        if action == "h":
            player_hand.append(deck.draw())
            print(f"Your hand: {player_hand}, value: {get_hand_value(player_hand)}")
            if get_hand_value(player_hand) > 21:
                print("You busted! Dealer wins!")
                return
        elif action == "s":
            break
        else:
            print("Invalid input, please enter 'h' or 's'")
    
    # now let's show the dealer's hand and let him play his turn
    print(f"Dealer's hand: {dealer_hand}, value: {get_hand_value(dealer_hand)}")
    
    while get_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.draw())
        print(f"Dealer's hand: {dealer_hand}, value: {get_hand_value(dealer_hand)}")
    
    # now let's compare the hands and determine the winner
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    
    if dealer_value > 21:
        print("Dealer busted! You win!")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a push!")

# let's run the game and put it main guard
if __name__ == "__main__":
    play_blackjack()
    # we could add a loop here to play multiple games, but let's keep it simple for now