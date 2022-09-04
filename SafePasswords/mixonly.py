import random
from colorama import Fore
class MixOnly(object):

    def JustMix(self):

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

        numbers = [
        "1", "2", "3", "4", "5", 
        "6", "7", "8", "9", "0"
        ]

        PasswordLen = input("No matter how long password: ")
        mixPassword = ""
        if PasswordLen.isdigit():
            PasswordLen = int(PasswordLen)
            for Mix0 in range(PasswordLen):
                for Mix1 in random.choice(Characterlower):
                    mixPassword = mixPassword + Mix1
                    for Mix2 in random.choice(Characterupper):
                        mixPassword = mixPassword + Mix2
                        for Mix3 in random.choice(numbers):
                            mixPassword = mixPassword + Mix3
            mixPassword = mixPassword[:PasswordLen]
            mixPassword = Fore.GREEN + mixPassword + Fore.RESET
            Right = Fore.CYAN + "-> " + Fore.RESET
            Generated = "Generated " + Fore.RED + "Mix Password " + Fore.RESET
            print(Generated + Right + mixPassword)
        else:
            print("Please dial numeric expressions!")
start = MixOnly()
start.JustMix()