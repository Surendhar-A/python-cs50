distances ={
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    except KeyError:
        print(f"{spacecraft} is not in dictionary")
        return
    m = convert(au)
    print(f"{m} is m away")

def convert(n):
    return n * 149597870691

main()