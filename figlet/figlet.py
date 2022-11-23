import sys
from pyfiglet import Figlet

font = sys.argv[2]
f = Figlet(font=font)

if sys.argv[1] != '-f':
    sys.exit("Invalid usage")
else:
    text = input('Input: ')
    print(f.renderText(text))
