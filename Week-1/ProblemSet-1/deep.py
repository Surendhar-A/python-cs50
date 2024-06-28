get_input = input('What is the answer to the Great Question of Life, the Universe and Everything? ')

match get_input.strip().casefold():
    case 'forty-two' | 'forty two' | '42':
        print('Yes')
    case _:
        print('No')
