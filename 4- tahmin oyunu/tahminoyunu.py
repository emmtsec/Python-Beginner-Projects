#!/usr/bin/env python3

import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Game:
    def __init__(self):
        clear_screen()
        print("\nWelcome to TAHMINOYUNU")
        print("1- Başla\n2- Zor\n3- Çıkış")

    def play(self, max_attempts=None):
        rand = random.randint(1, 100)
        counter = 0
        while True:
            counter += 1
            try:
                guess = int(input(f"\n(1-100 arası sayı giriniz{' Unutmayın sadece 5 canınız var!' if max_attempts else ''}) > Tahminizi giriniz: "))
                if guess > rand:
                    print("Yaklaştın, sayı düşürünüz!")
                elif guess < rand:
                    print("Yaklaştın, sayı yükseltiniz!")
                else:
                    print(f"Tebrikler, {counter} denemede buldunuz!")
                    break

                if max_attempts and counter >= max_attempts:
                    print(f"Bütün tahmin hakkınızı kullandınız! Oyun bitti. Sayı şuydu: {rand}")
                    break

            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")

if __name__ == '__main__':
    game = Game()
    choice = input("Seçiminiz: ")
    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            game.play()
        elif choice == 2:
            game.play(max_attempts=5)
        elif choice == 3:
            print("Oyun kapatılıyor.")
        else:
            print("1, 2 veya 3 sayılarından birini seçiniz.")
    else:
        print("Lütfen bir sayı giriniz.")
