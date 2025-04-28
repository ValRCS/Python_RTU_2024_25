import random
from itertools import product
 
def get_shuffled_cards():
    # atsevišķie kāršu "cipari" un simboli
    cipars = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    simbols = ["ercens", "kāravs", "pīķis", "kreics"]
 
    # no iepriekšējā saraksta izveidojam pilni kāršu komplektu, savienojot ciparus ar simboliem
    # komplekts = []
    # for rank in cipars:
    #     for suit in simbols:
    #         komplekts.append((rank, suit))
    # alterantive is to use product from itertools
    komplekts = list(product(cipars, simbols)) 
    
    # izmanto random, lai saliktu visu nejaušā secībā
    random.shuffle(komplekts)
 
    return komplekts
 
# print katru reizi dos citu nejaušu rezultātu
cards = get_shuffled_cards()
print(f"How many cards: {len(cards)}")
print(f"First card: {cards[0]}")
print(f"Last card: {cards[-1]}")