# Pyfiglet documentation : https://pypi.org/project/pyfiglet/
import sys 
import random 
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        font = sys.argv[2]
        if font not in available_fonts:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid usage")
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()