months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            get_input = input("Date: ").strip().title()
            if get_input.count("/") == 2:
                month , day, year = get_input.split("/")
                if 0 < int(month) <=12 and 0 < int(day) <=31:
                    break
                else:
                    continue
            elif get_input.count(",") == 1:
                month , day, year = get_input.split()
                month = months.index(month)+1
                day = day.removesuffix(",")
                if 0 < int(day) <=31:
                    break
                else:
                    continue
            else:
                continue
        except ValueError:
            continue
    month = int(month)
    day = int(day)
    year = int(year)
    print(f"{year}-{month:02}-{day:02}")

main()
