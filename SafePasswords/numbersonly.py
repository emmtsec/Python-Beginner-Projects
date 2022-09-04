import random
from colorama import Fore
class NumberOnly(object):

    def JustNumbers(self):

        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        PasswordLen = input("No matter how long password: ")
        NumberPassword = ""
        if PasswordLen.isdigit():
            PasswordLen = int(PasswordLen)
            for Nmbr0 in range(PasswordLen):
                for Nmbr1 in random.choice(numbers):
                    NumberPassword = NumberPassword + Nmbr1
            NumberPassword = NumberPassword[:PasswordLen]
            NumberPassword = Fore.GREEN + NumberPassword + Fore.RESET
            Right = Fore.CYAN + "-> " + Fore.RESET
            Generated = "Generated " + Fore.RED + "Number Password " + Fore.RESET
            print(Generated + Right + NumberPassword)
        else:
            print("Please dial numeric expressions!")
start = NumberOnly()
start.JustNumbers()