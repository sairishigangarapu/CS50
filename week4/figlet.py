from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
x = figlet.getFonts()
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in x:
        figlet.setFont(font = sys.argv[2])
        s = str(input("Input: "))
        print("Output:",figlet.renderText(s))
        sys.exit()
    else:
        sys.exit("Invalid Usage")

if len(sys.argv) == 2 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    figlet.setFont(font = random.choice(x))
    a = str(input("Input: "))
    print("Output:",figlet.renderText(a))
    sys.exit()
else:
    sys.exit("Invalid Usage")
