def main(): 
    coke_cost = 50
    check_due(coke_cost)

def check_due(coke_cost):
    while coke_cost > 0:
        print(f"Amount Due: {coke_cost}")
        x = int(input("Insert Coin: "))
        match x:
            case 25 | 10 | 5:
                coke_cost -= x
        if coke_cost == 0:
            print(f"Change Owed: {coke_cost}")
        elif coke_cost < 0:
            print(f"Change Owed: {-coke_cost}")
        else:
            None

main()


"""  # Method 1 -- not optimized

coke_cost = 50

print(f"Amount Due: {coke_cost}")
get_input = int(input("Insert Coin: "))

if get_input == 25 or get_input == 10 or get_input ==5:
    change_owed = coke_cost - get_input
    print(f"Amount Due: {change_owed}")
else:
    change_owed = coke_cost
    print(f"Amount Due: {change_owed}")

while change_owed > 0:
    get_input_again = int(input("Insert Coin: "))
    match get_input_again:
        case 25 | 10 | 5:
            change_owed -= get_input_again
            if change_owed == 0:
                print(f"Change Owed: {change_owed}")
            elif change_owed < 0:
                print(f"Change Owed: {-change_owed}")
            else:
                print(f"Amount Due: {change_owed}")
        case _:
            print(f"Amount Due: {change_owed}")
    
"""
