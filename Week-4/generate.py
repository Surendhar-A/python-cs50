"""imports everything from the library random"""
import random

"""imports the choice function from library random"""
#from random import choice 

import statistics

coin = random.choice(["heads","tails"])
random_int = random.randint(1,10)

cards = ["king","queen","jack"]
random.shuffle(cards)

mean = statistics.mean([100,90])

print(coin)
print(random_int)

for i in cards:
    print(i)

print(mean)