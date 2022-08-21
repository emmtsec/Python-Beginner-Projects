# -*- coding:utf-8 -*-
#! usr/bin/env python3

# Burada kullanmamız gereken kütüphanemizi ekledik Pytube içinde ki YouTube import ettik.
from pytube import YouTube

# İşimize yarıyacak diğer kütüphaneler
from platform import python_version
from os import system
from os import name
from time import sleep
from colorama import Fore


class PythonVersionControl(object):
    @staticmethod
    def __init__():
        if int(python_version()[0]) < 3:
            print("{0}[!] {1}Supports Python3 and higher!".format(Fore.LIGHTRED_EX, Fore.RESET))
            exit()
        else:
            print("{0}[OK] {1}Version güncel...".format(Fore.LIGHTGREEN_EX, Fore.RESET))

class ModuleControl(object):
    @staticmethod
    def __init__():
        try:
            from colorama import Fore
            print("{0}[OK] {1}Modülleriniz güncel...".format(Fore.LIGHTGREEN_EX, Fore.RESET))
        except ModuleNotFoundError:
            if name == "posix":
                print("{0}[*] {1}pip3 install colorama [LİNUX]".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
            else:
                print("{0}[*] {1}pip install colorama [Win32 and Win64]".format(Fore.LIGHTYELLOW_EX, Fore.RESET))

class Menu(object):
    @staticmethod
    def __init__():
        print("""

            {0}*{1} {2}YouTube Downloader{1} {0}*{1}
            {3}1-{1} Video Download
            {3}2-{1} Exit


            """.format(Fore.LIGHTYELLOW_EX, Fore.RESET, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX))

class YouTube_Download(object):
    @staticmethod
    def Download_Settings():
        link = input("{0}[*] {1}Enter your download video adress: ".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
        sleep(0.5)
        print("{0}[*] {1}Please wait...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
        yt = YouTube(link)
        print("""

        Title : {0}
        Number of Views : {1}
        Lenght of video : {2} seconds
        Description : {3}
        Ratings : {4}

            """.format(yt.title, yt.views, yt.length, yt.description, yt.rating))
        input("{0}[*] {1}Press to Enter Key...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
        ys = yt.streams.get_highest_resolution()
        sleep(0.5)
        print("{0}[*] {1}Download video...".format(Fore.LIGHTYELLOW_EX, Fore.RESET, Fore.LIGHTRED_EX,))
        ys.download("Masaüstü/")

if __name__ == "__main__":
    pc = PythonVersionControl()
    mc = ModuleControl()
    #sleep(5)
    if name == "win32" and name == "win64":
        system("cls")
    else:
        system("clear")
    sm = Menu()
    yd = YouTube_Download()
    choice = input("{0}[?] {1}{2}What is your choice:{1} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET, Fore.LIGHTGREEN_EX))
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            yd.Download_Settings()
        elif choice == 2:
            print("{0}[!] {1}Logget out...".format(Fore.LIGHTRED_EX, Fore.RESET))
            sleep(1.7)
            exit()
        else:
            print("{0}[!] {1}{2}Please enter number 1-2!{1}".format(Fore.LIGHTRED_EX, Fore.RESET, Fore.LIGHTYELLOW_EX))
            exit()
    else:
        print("{0}[!] {1}{2}Please just enter number!{1}".format(Fore.LIGHTRED_EX, Fore.RESET, Fore.LIGHTYELLOW_EX))
        exit()
