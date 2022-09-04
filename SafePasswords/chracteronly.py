import random
import os
from colorama import Fore
class CharacterOnly(object):

    def JustCharacter(self):

        Characterlower = [
        "q","w", "e", "r", "t", "y", 
        "u", "i", "o", "p", "a", "s", 
        "d", "f", "g", "h", "j", "k", 
        "l", "z", "x", "c", "v", "b", 
        "n","m"
        ]

        Characterupper = [
        "Q", "W", "E", "R", "T", "Y", 
        "U", "I", "O", "P", "A", "S",
        "D", "F", "G", "H", "J", "K",
        "L", "Z", "X", "C", "V", "B", 
        "N", "M"
        ]

        PasswordLen = input("No matter how long password: ")
        SafePassword = ""

        if PasswordLen.isdigit():
            PasswordLen = int(PasswordLen)
            for Chr0 in range(PasswordLen):
                for Chr1 in random.choice(Characterlower):
                    SafePassword = SafePassword + Chr1
                for Chr2 in random.choice(Characterupper):
                    SafePassword = SafePassword + Chr2

            SafePasswor_d = SafePassword[PasswordLen:]
            SafePasswor_d = Fore.GREEN + SafePasswor_d + Fore.RESET
            Right = Fore.CYAN + "-> " + Fore.RESET
            Generated = "Generated " + Fore.RED + "Character Password " + Fore.RESET
            print(Generated + Right + SafePasswor_d)
        else:
            print("Please dial numeric expressions!")


start = CharacterOnly()
start.JustCharacter()