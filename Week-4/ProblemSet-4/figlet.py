import random
import sys
from pyfiglet import Figlet

def main():
    print_text()

def print_text():
    figlet = Figlet()
    font_list = figlet.getFonts()
    if len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
            figlet.setFont(font = sys.argv[2])
        else:
            sys.exit("Invalid Usage")
    elif len(sys.argv) == 1:
        figlet.setFont(font = random.choice(font_list))
    else:
        sys.exit("Invalid Usage")

    get_input = input("Input: ")
    print(figlet.renderText(get_input))

main()
