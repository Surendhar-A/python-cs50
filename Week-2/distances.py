distances = {
    "Voyager 1": 163,
    "Voyager": 162,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 14
}

def main():
    for i in distances:
        print(f"{distances[i]} AU is {convert(distances[i])} meters from earth")
    for i in distances.values():
        print(f"{i} AU is {convert(i)} meters from earth")


def convert(au):
    return au * 149597870700

main()
"""
for i in distances:
    print(f"{i} is {distances[i]} AU from earth" )
"""
