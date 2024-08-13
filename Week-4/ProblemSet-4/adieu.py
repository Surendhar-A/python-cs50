import inflect

engine = inflect.engine()

name_list = []
while True:
    try:
        get_input = input()
        name_list.append(get_input)
    except EOFError:
        break
final = engine.join(name_list)
print(f"Adieu, adieu, to {final}")

"""
#Alternate method without using inflect

name_list = []
while True:
    try:
        get_input = input()
        name_list.append(get_input)
    except EOFError:
        break
print("Adieu, adieu, to ", end="")
if len(name_list) == 1:
    print(name_list[0])
elif len(name_list) == 2:
    print(name_list[0] + " and " + name_list[1])
else:
    print(", ".join(name_list[:-1]) + ", and " + name_list[-1])

"""