def main():
    height = int(input("Height: "))
    pyramid(height)
def pyramid(n):
    for i in range(n):
        print("#" * n)

if __name__ == "__main__":
    main()