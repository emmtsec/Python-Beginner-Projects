#!usr/bin/env python3
import os
import time
def clearmenu():
    if os.name == 'nt' or os.name == "win32" or os.name == "win64":
        os.system("cls")
    else:
        os.system("clear")

class start(object):

    def __init__(self):
        clearmenu()
        print("\n 1- Ortalama hesaplma \n 2- Çıkış")

if __name__ == "__main__":
    start()
    choice = input("Seçiminiz: ")

    if choice.isdigit():
        if int(choice) == 1:
            prompt = input("İlk notunuzu giriniz: ")
            time.sleep(0.5)
            prompt2 = input("İkinci notunuzu giriniz: ")
            time.sleep(0.2)
            try:
                sonuc = (float(prompt) + float(prompt2)) /2
                if sonuc >= 50:
                    print("Geçtiniz! Sonucunuz : {}".format(sonuc))
                else:
                    print("Kaldınız! Sonucunuz : {}".format(sonuc))
            except ValueError:
                print("sayı girişi yapınız!")
        elif int(choice) == 2:
            pass
        else:
            print("1 or 2!")
    else:
        print("Harf kullanmayınız")

