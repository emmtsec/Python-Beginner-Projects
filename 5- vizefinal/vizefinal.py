#!usr/bin/env python3
import os
import time


def clearmenu():
    if os.name == "win64" and os.name == "win32" or os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class start(object):

    def __init__(self):
        print("""
            1- Vize ve Final hesaplama
            2- Çıkış
              """)

if __name__ == '__main__':
    clearmenu()
    start()
    choice = input("Seçim yapınız: ")
    if choice.isdigit():
        choice = int(choice)
        if int(choice) == 1:
            prompt = input("Vize notunuzu giriniz : ")
            time.sleep(0.5)
            prompt2 = input("Final notunuzu giriniz: ")
            if prompt and prompt2.isdigit():
                conclusion = (float(prompt) * 0.3) + (float(prompt2) * 0.7)
                if conclusion >= 50:
                    print("Tebrikler geçtiniz Sonuç : {}".format(conclusion))
                else:
                    print("Kaldınız... sonucunuz : {}".format(conclusion))
        elif choice == 2:
            pass
        else:
            print("sadece 1 veya 2 giriniz.")
    else:
        print("sadece rakam girebilirsiniz.")
