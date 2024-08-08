import random
from colorama import Fore
class SpecialMixOnly(object):

    def JustSpecialMix(self):

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

        specials = [
            "$", "&", "!", "%",
            "+", "-", "/", ".",
            "*", "[", "]", "|"
        ]
        PasswordLen = input("No matter how long password: ")
        SpecialMix = ""
        if PasswordLen.isdigit():
            PasswordLen = int(PasswordLen)
            for SpclMix0 in range(PasswordLen):
                for SpclMix1 in random.choice(Characterlower):
                    SpecialMix = SpecialMix + SpclMix1
                    for SpclMix2 in random.choice(Characterupper):
                        SpecialMix = SpecialMix + SpclMix2
                        for SpclMix3 in random.choice(numbers):
                            SpecialMix = SpecialMix + SpclMix3
                            for SpclMix4 in random.choice(specials):
                                SpecialMix = SpecialMix + SpclMix4
            SpecialMix = SpecialMix[:PasswordLen]
            SpecialMix = Fore.GREEN + SpecialMix + Fore.RESET
            Right = Fore.CYAN + "-> " + Fore.RESET
            Generated = "Generated " + Fore.RED + "Special Mix Password " + Fore.RESET
            print(Generated + Right + SpecialMix)
        else:
            print("Please dial numeric expressions!")
start = SpecialMixOnly()
start.JustSpecialMix()      