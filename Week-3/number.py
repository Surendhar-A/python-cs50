def main():
    get_input = get_int("What's x? ")
    print(f"x is {get_input}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            #pass
            print("x is not an integer")
        else:
            #break
            return x  #breaks and returns the value
    #return x


main()

"""
try:
    x = int(input("What's x? "))
except ValueError:
    print("X is not a integer")
else:
    print (f"x is {x}")
"""

"""
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
"""