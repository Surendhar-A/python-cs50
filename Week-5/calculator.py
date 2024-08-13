def main():
    get_input = int(input("What's X? "))
    print("X squared is", square(get_input))

def square(n):
    return pow(n, 2)

if __name__ == "__main__":
    main()