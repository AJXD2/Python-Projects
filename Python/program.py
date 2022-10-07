
import pyfiglet
from colorama import init, Fore, Back, Style
global FORES
global BACKS
global BRIGHTNESS
global color
# essential for Windows environment
print(Fore.GREEN)
# all available foreground colors
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]
color = FORES.GREEN
print(color)
def main():
    ASCII_art_1 = pyfiglet.figlet_format("AJ's Terminal")
    print(ASCII_art_1)
    print(color "Please select an option to continue")
    print("Options:")
    print(" -ping -t: -t = target")
    print(" -exit")
    print(" -changecolor -c: -c color of terminal")
def command(command):
    return
    
while True:
    main()
    


    






print(Fore.WHITE)
exitt = input()