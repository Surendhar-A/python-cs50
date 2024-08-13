import random

cards = ["jack", "queen", "king"]

def main():
    random.seed(1) #gives the same value when using choices, sample. Used for debugging.
    print(random.choices(cards, k=2)) #with replacement
    print(random.choices(cards, weights=[75, 20,5], k=2))
    print(random.sample(cards, k=2)) #without replacement
main()