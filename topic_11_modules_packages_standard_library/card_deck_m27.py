# let's generated a CardDeck class that can be used in a game
# we will have following methods
# shuffle - shuffle the deck
# peek - peek at the top card of the deck
# draw - draw a card from the deck
# __str__ - print the deck
# __init__ - initialize the deck

import itertools
import random

class CardDeck:
    def __init__(self, 
                 # let's use emoji suits
                 suits = ("♠", "♣", "♥", "♦"),
                 ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"),
                 shuffle=False, 
                 seed=None):
        self.suits = suits
        self.ranks = ranks
        # self.deck = [(rank, suit) for rank in self.ranks for suit in self.suits]
        # above is a fine approach but we could do the same with two loops which is longer
        # also we could do it with itertools.product
        self.deck = list(itertools.product(self.ranks, self.suits))
        if seed: # without seed we will get different results each time we run the script
            random.seed(seed)
        if shuffle:
            self.shuffle()
        print("Jauns kāršu komplekts izveidots!")

    # now let's make __str__ method that prints the deck
    def __str__(self):
        return str(self.deck) # we could think of some more formatted output TODO
    
    # let's define shuffle method
    def shuffle(self):
        random.shuffle(self.deck) # note that random.shuffle is IN PLACE, it does not return a new list
        return self # so we can chain methods like deck.shuffle().peek()  

    # peek method
    def peek(self):
        return self.deck[-1] # this will return the last card in the deck, which is the top card   

    # draw method
    def draw(self):
        return self.deck.pop() # reminder that self.deck is modified IN PLACE
        # pop returns the last element of the list and removes it from the list 