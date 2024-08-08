from os import system
from os import name
if __name__ == "__main__":
    if name == "win32" or name == "win64":
        system("cls")
    else:
        system("clear")
    from menu import Menu
    choice = input("Make your selection from the list: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            from chracteronly import CharacterOnly
        elif choice == 2:
            from numbersonly import NumberOnly
        elif choice == 3:
            from mixonly import MixOnly
        elif choice == 4:
            from specialmix import SpecialMixOnly
        elif choice == 5:
            from CaesarPass import Caesar
        else:
            print("Please only 1, 2, 3, 4 and 5 Your Keys!")
    else:
        print("Please dial numeric expressions!")
