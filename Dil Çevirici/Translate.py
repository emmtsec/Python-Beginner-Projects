# -*- coding: utf-8 -*-
from colorama import Fore
from googletrans import Translator
from os import system
from os import name

class Translete(object):
    def __init__(self):
        print("""
            [1] Çevir
            [2] Toplu Çevir
            [3] Çıkış
            """)
    def TransL(self):
        if name == "win32" or name == "win64":
            system("cls")
        else:
            system("clear")
        translator = Translator()
        sentence = input("Çevirilecek Cümleyi Giriniz: ")
        language = input("Çevirilecek dili giriniz Örneğin " + Fore.GREEN +"(en, ru, kr)" + Fore.RESET + ": ")
        if sentence.isdigit() and language.isdigit():
            sentence = Fore.RED + sentence + Fore.RESET
            language = Fore.RED + sentence + Fore.RESET
            print("Numara tuşlamayınız! Error : {} and Error : {}".format(sentence, language))
        else:
            translated = translator.translate(sentence, dest=language).text
            sentence = Fore.YELLOW + sentence + Fore.RESET
            translated = Fore.GREEN + translated + Fore.RESET
            language = Fore.RED + language + Fore.RESET
            direction = Fore.YELLOW + " -> " + Fore.RESET
            print(sentence + direction + translated)
    def TransX(self):
        translator = Translator()
        array_trans = []
        isSentences = False
        while not isSentences:
            fore_repeat = Fore.RED + "(E/h)" + Fore.RESET
            repeat = input("Çevirmek ister misiniz? {}: ".format(fore_repeat))
            if repeat == "E" or repeat == "e":
                if name == "win32" or name == "win64":
                    system("cls")
                else:
                    system("clear")
                sentences = input("Çevirilecek Cümleyi Giriniz: ")
                if sentences in array_trans:
                    print("Girdiğiniz cümle daha önce eklemişsiniz!")
                else:
                    array_trans.append(sentences)
            else:
                isSentences = True
        fore_language = Fore.RED + "(en - kr - ru): " + Fore.RESET
        arg = Fore.GREEN + ":" + Fore.RESET
        language = input("Hangi dile çevrilsin? {}".format(fore_language))
        translations = translator.translate(array_trans, dest=language)
        b = 0
        for translation in translations:
            b += 1
            translation.origin = Fore.RED + translation.origin + Fore.RESET
            translation.text = Fore.GREEN + translation.text + Fore.RESET
            direction = Fore.YELLOW + " -> " + Fore.RESET
            print("{}.".format(b), translation.origin + direction + translation.text)
    def Exit(self):
        pass
if __name__ == "__main__:
    if name == "win32" or name == "win64":
        system("cls")
    else:
        system("clear")
    start = Translete()
    choice = input("Seçiminiz: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            start.TransL()
        elif choice == 2:
            start.TransX()
        elif choice == 3:
            start.Exit()
        else:
            print("Lütfen 1, 2 veya 3 tuşlayınız!")
    else:
        print("Sayısal ifade tuşlayınız!")
