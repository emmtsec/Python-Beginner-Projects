#!usr/bin/env python3
#-*- coding:utf-8 -*-

from os import system
from os import name
from time import sleep
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ChromaModule import RED, GREEN, YELLOW, ITALIC, BOLD, CLEAR
from TimeModule import Hours, Minutes

NAME = "Pr0xy"
APPNAME = "AutoMessage"
VERSION = "1.0.0"
OS = "Windows - Linux - Mac OS"
CODENAME = "xWhatsapp"

class AutoMessage(object):
    def __init__(self):
        if(name == "win32" or name == "win64"):
            system("cls")
            print(BOLD+ RED+ "Translete" +CLEAR)
            print(BOLD+ "Developed: " +CLEAR+ BOLD+ RED+ ITALIC+ "Pr0xy" +CLEAR)
        else:
            system("apt-get install boxes && apt-get install figlet")
            system("clear")
            system("figlet -f slant AutoMessage | boxes -d peek -pa2t0b0")
    def Whatsapp(self):
        self.victims = input(BOLD+ "Who: " +CLEAR)
        self.message = input(CLEAR+ BOLD+ "Message: " +CLEAR+ BOLD+"(" +CLEAR+ BOLD+ GREEN+ "Yes " +CLEAR+ BOLD+ "or " +CLEAR+ BOLD+ RED+ "No" +CLEAR+ BOLD+ "): ")
        if(self.message == "Yes") or (self.message == "yes"):
            self.driver = webdriver.Firefox()
            self.driver.get("https://web.whatsapp.com/")
            input("Do this after reading the QR Code.")
            self.victimsUsername = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, '//span[@title = "{}"]'.format(self.victims))))
            self.victimsUsername.click()
            self.messagewhatsapp = input(CLEAR+ BOLD+ "Message: ")
            self.messagepiece = int(input("Piece: " +CLEAR))
            self.msgbox = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')))
            for Bots in range(self.messagepiece):
                self.msgbox.send_keys(self.messagewhatsapp)
                self.msgbox.send_keys(Keys.ENTER)
                print(RED+ BOLD+ "[ * ] "+CLEAR+ BOLD+ GREEN+ "Successfully posted!")
            print(RED+ BOLD+ "[ ** ] "+CLEAR+ BOLD+ GREEN+ "All Successfully posted")
            self.driver.quit()
        elif(self.message == "No") or (self.message == "no"):
            self.driver = webdriver.Firefox()
            self.driver.get("https://web.whatsapp.com/")
            input("Do this after reading the QR Code.")
            self.victimsUsername = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, '//span[@title = "{}"]'.format(self.victims))))
            self.victimsUsername.click()
            self.messagepiece = int(input("Piece: " +CLEAR))
            for troll in range(self.messagepiece):
                sleep(1)
                self.image = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]')))
                self.image.click()
                self.findimage = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')))
                self.findimage.click()
                self.keyboard = Controller()
                sleep(1)
                self.keyboard.press(Key.enter)
                self.keyboard.sleep(1)
                print(RED+ BOLD+ "[ * ] "+CLEAR+ BOLD+ GREEN+ "Successfully posted!")
            print(RED+ BOLD+ "[ ** ] "+CLEAR+ BOLD+ GREEN+ "All Successfully posted")
start = AutoMessage()
start.Whatsapp()
