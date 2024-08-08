#!usr/bin/env python3
import os
import random

def clearmenu():
    if os.name == "nt" or os.name == "win32" or os.name == "win64":
        os.system("cls")
    else:
        os.system("clear")

class start(object):

    def __init__(self):
        print(" \n 1- Pozitif ve negatif sayı hedefleme\n 2- çıkış ")

if __name__ == "__main__":
    clearmenu()
    start()
    choice = input("\n Seçim yapınız: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            detected = ["pozitif", "negatif"]
            s = random.choice(detected)
            if s == "pozitif":
                print("Pozitif sayı girişi yapınız!")
                while True:
                    try:
                        prompt = int(input("Sayı girişi yapınız : "))
                        if prompt < 0:
                            print("Negatif sayı girdiniz.")
                        else:
                            print("Doğru...")
                            break
                    except ValueError:
                        print("Harf eklemeyiniz")
            else:
                    print("Negatif sayı girişi yapınız!")
                    while True:
                        try:
                            prompt = int(input("Sayı girişi yapınız : "))
                            if prompt >= 0:
                                print("Pozitif sayı girdiniz.")
                            else:
                                print("Doğru...")
                                break
                        except ValueError:
                            print("Harf eklemeyiniz.")

