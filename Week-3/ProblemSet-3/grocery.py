def main():
    grocery_list = []
    grocery_dict = {}
    while True:
        try:
            get_input = input().upper()
            grocery_list.append(get_input)
        except EOFError:
            break
    for items in grocery_list:
        # gets the value of item in dict and increments the value by 1. if the item is not already present in th dict then default value is 0
        grocery_dict[items] = grocery_dict.get(items,0) + 1
    sorted_dict = dict(sorted(grocery_dict.items()))
    for i in sorted_dict:
        print(sorted_dict[i], i)

main()

"""
Method 2:
def main():
    grocery_dict = {}
    while True:
        try:
            get_input = input().upper()
            if get_input in grocery_dict:
                grocery_dict[get_input] += 1
            else:
                grocery_dict[get_input] = 1
        except EOFError:
            sorted_dict = dict(sorted(grocery_dict.items()))
            for i in sorted_dict:
                print(sorted_dict[i],i)
            break
main()

"""