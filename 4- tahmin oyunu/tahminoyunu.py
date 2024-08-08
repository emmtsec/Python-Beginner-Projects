#!usr/bin/env python3

import random
import os

def clearmenu():
    os.system('cls' if os.name == 'nt' else 'clear')

class start(object):
    def __init__(self):
        clearmenu()
        print("\n Welcome to TAHMINOYUNU\n 1- Başla\n 2- Zor \n 3- Çıkış")

if __name__ == '__main__':
    start()
    rand = random.randint(1,100)
    counter = 0
    choice = input("Seçiminiz: ")
    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            while True:
                counter += 1
                closs = input("\n(1-100 arası sayı giriniz) > Tahminizi giriniz: ")
                if int(closs) > rand:
                    print("Yaklaştın sayı düşünüz!")
                elif int(closs) < rand:
                    print("Yaklaştın sayı çıkınız!")
                elif int(closs) == rand:
                    print("Tebrikler buldunuz şu kadar {} sayıda tahmin ettiniz..".format(counter))
                    break

        elif choice == 2:
            while True:
                counter += 1
                closs = input("\n(1-100 arası sayı giriniz Unutmayın sadece 5 canınız var!) > Tahminizi giriniz: ")
                if counter == 5:
                    print("Bütün tahmin hakkınızı kullandınız! Oyun bitti.. Tahmin sayısı şudur > {}".format(rand))
                    break
                elif int(closs) > rand:
                    print("Yaklaştın sayı düşünüz!")
                elif int(closs) < rand:
                    print("Yaklaştın sayı çıkınız!")
                elif int(closs) == rand:
                    print("Tebrikler buldunuz şu kadar {} sayıda tahmin ettiniz..".format(counter))
                    break

        elif choice == 3:
            pass

        else:
            print("1, 2 ve 3 sayılarından birini seçiniz..")
            pass

    else:
        print("Harf girmeyiniz!")