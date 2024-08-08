#!usr/bin/env python3

import re

def check_password(password):
    if len(password) < 8: # Şifre uzunluğu
        return "Zayıf: Şifreniz çok kısa!"
    if not re.search(r"[A-Z]", password):
        return "Zayıf: En az bir büyük harf içermelidir!"
    if  not re.search(r"[a-z]", password):
        return "Zayıf: En az bir küçük harf içermelidir!"
    if not re.search(r"[0-9]", password):
        return "Zayıf: En az bir sayı içermelidir!"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Zayıf: En az bir özel karakter içermelidir!"
    return "Güçlü: Şifreniz güçlüdür!"

if __name__ == "__main__":
    password = input("Şifrenizi giriniz: ")
    print(check_password(password))