def main():
    X = int(input('Enter value of X: '))
    print('Square of X is', square(X))

def square(n):
    return pow(n,2)
    # return n * n
    # return n ** 2

main()