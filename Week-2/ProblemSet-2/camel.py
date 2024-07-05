def main():
    get_input = input("camelCase: ")
    print("snake_case: ", end="")
    checkCase(get_input)


def checkCase(n):
    for i in n:
        if i == i.upper():
            i = i.replace(i, f'_{i.lower()}')
            #print(i.replace(i, f'_{i.lower()}'))
        else:
            None
        print(i,end="")
    print()
     
          
main()