def main():
    get_input = input()
    converted_txt = convert(get_input)
    print(converted_txt)

def convert(txt):
    return txt.replace(':)',"🙂").replace(':(','🙁')

main()
