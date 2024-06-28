"""
# Function to print hello and provide a default value
def hello(x='World'):
    print('Hello,',x)

name  = input('What is your name? ')
hello()
hello(name)
"""

def main():
    name = input('What is yout name? ')
    hello(name)

def hello(x='World'):
    print('Hello,',x)

main()