get_input = input('Greeting: ').strip().casefold()

if get_input.startswith('hello'):
    print('$0')
elif get_input.startswith('h'): #and get_input.startswith('hello') == False:
    print('$20')
else:
    print('$100')
