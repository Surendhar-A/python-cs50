import random


def main():
    level_value = get_level()
    score_count = 0

    for _ in range(10):
        X, Y = get_integer(level_value)
        answer = str(X+Y)
        err_count = 0

        while True:
            get_value = input(f"{X} + {Y} = ")

            if get_value == answer:
                score_count += 1
                break

            elif get_value != answer:
                err_count += 1

                if err_count >= 3:
                    print(f"{X} + {Y} =", answer)
                    break
                else:
                    print("EEE")
    print(f"Score: {score_count}")


def get_level():
    while True:
        get_input = input("Level: ")
        match get_input:
            case "1" | "2" | "3":
                get_input = int(get_input)
                break
            case _:
                continue
    return get_input


def get_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError
    return x, y


if __name__ == "__main__":
    main()
