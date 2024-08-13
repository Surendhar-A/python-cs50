def main():
    get_input = input("What's your name? ")
    print(hello(get_input))

def hello(to = "world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()