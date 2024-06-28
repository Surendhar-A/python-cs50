def main():
    get_input = math(input('Expression: '))
    print(f'{get_input:.1f}')

def math(m):
    x, y, z = m.split(' ')
    x = int(x)
    z = int(z)
    match y:
        case '+':
            return x + z
        case '-':
            return x - z
        case '*':
            return x * z
        case '/':
            return x / z
main()