import random # this is part of standard library, so we don't need to install it
# this is a simple script that creates a deck of cards and shuffles it
import itertools # this is part of standard library, so we don't need to install it
# itertools makes all kind of iterators for efficient looping
 
def get_shuffled_cards(seed = None):
    # card_deck = [("2","kāravs"),("2","ercens"),("2","kreics"),("2","pīķis"),
    #              ("3","kāravs"),("3","ercens"),("3","kreics"),("3","pīķis"),
    #              ("4","kāravs"),("4","ercens"),("4","kreics"),("4","pīķis"),
    #              ("5","kāravs"),("5","ercens"),("5","kreics"),("5","pīķis"),
    #              ("6","kāravs"),("6","ercens"),("6","kreics"),("6","pīķis"),
    #              ("7","kāravs"),("7","ercens"),("7","kreics"),("7","pīķis"),
    #              ("8","kāravs"),("8","ercens"),("8","kreics"),("8","pīķis"),
    #              ("9","kāravs"),("9","ercens"),("9","kreics"),("9","pīķis"),
    #              ("10","kāravs"),("10","ercens"),("10","kreics"),("10","pīķis"),
    #              ("J","kāravs"),("J","ercens"),("J","kreics"),("J","pīķis"),
    #              ("Q","kāravs"),("Q","ercens"),("Q","kreics"),("Q","pīķis"),
    #              ("K","kāravs"),("K","ercens"),("K","kreics"),("K","pīķis"),
    #              ("A","kāravs"),("A","ercens"),("A","kreics"),("A","pīķis")]
    # let's generate our unshuffled deck of cards 
    suits = ("♠", "♣", "♥", "♦")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    # card_deck = list(itertools.product(ranks, suits)) # very pythonic way to do it
    # if we did not know about itertools.product we could do regular nested loops
    card_deck = []
    for suit in suits:
        for rank in ranks:
            card_deck.append((rank, suit)) # this is a tuple of rank and suit
    # i couuld manually add two jokers here but let's not do it for now
    # let's set seed first to get the same result each time we run the script
    if seed is not None:
        random.seed(seed) # this will give us the same result each time we run the script
    random.shuffle(card_deck)
    return card_deck
 
card_deck = get_shuffled_cards()
# print(f"Random card from deck: {random.choice(get_shuffled_cards())}")
# first random card from deck
print(f"Random card from deck: {card_deck[0]}")
