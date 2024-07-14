def main():
    print(fuel_guage())

def fuel_guage():
    while True:
        get_input = input("Fraction: ")
        try:
            x, y = get_input.split("/")
            x = int(x)
            y = int(y)
            fuel_left = round((x/y) * 100)
            if x > y:
                True
            else:
                break
        except (ValueError,ZeroDivisionError):
            True
    if fuel_left <= 1:
        return ("E")
    elif fuel_left >= 99:
        return ("F")
    else:
        return (f"{fuel_left}%")

main()
