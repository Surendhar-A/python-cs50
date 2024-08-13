import random

while True:
    get_input = input("Level: ")
    if get_input.isnumeric() and get_input != "0":
        get_input = int(get_input)
        break
    else:
        continue

value = random.randint(1, get_input)

while True:
    guess = input("Guess: ")
    if guess.isnumeric():
        guess = int(guess)
        if guess < value:
            print("Too Small!")
        elif guess > value:
            print("Too Large!")
        else:
            print("Just Right!")
            break
    else:
        continue
