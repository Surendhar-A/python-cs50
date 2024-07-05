get_input = input('Input: ')
print("Output: ", end="")

for i in get_input:
    match i.lower():
        case "a"| "e"| "i"| "o"| "u":
            i = i.replace(i,'')
        case _:
            None
    print(i, end="")

print()
