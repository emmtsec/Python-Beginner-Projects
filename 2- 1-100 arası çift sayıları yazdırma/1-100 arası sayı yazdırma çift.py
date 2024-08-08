#!usr/bin/env python3
import os

def clearmenu():
    if os.name == "nt" or os.name == "win32" or os.name == "win64":
        os.system("cls")
    else:
        os.system("clear")

class start(object):

    def __init__(self):
        clearmenu()
        print("\n 1- 1-100 arası sayı yazdır\n 2- Çıkış")

if __name__ == "__main__":
    start()
    choice = input("Seçiminiz: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            prompt = input("Birinci sayıyı giriniz: ")
            prompt2 = input("İkinci sayıyı giriniz: ")
            if prompt > prompt2:
                print("Birinci sayı ikinci sayıdan büyük olamaz!")
                pass

            elif int(prompt) and int(prompt2) > 100:
                print("100 üstü sayı girmeyiniz!")
                pass

            elif prompt.isdigit() and prompt2.isdigit():
                counter = 0
                for i in range(int(prompt), int(prompt2) + 2):
                    if i % 2 == 0:
                        print(i)
                        counter += i
                print("Bütün sayıların toplamı : {}".format(counter))

        elif choice == 2:
            pass

        else:
            print("1 veya 2 seçimini yapınız..")

    else:
        print("Harf girmeyiniz!")


