

def main():
    print_square(3)

# Method 1
"""
def print_square(size):
    #print("#" * size)
    for i in range(size):
        print("#" * size)
"""

# Method 2
"""
def print_square(size):
    # For each row in a square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            print('#', end='')
        print()
"""

# Method 3

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print('#' * width)

main()