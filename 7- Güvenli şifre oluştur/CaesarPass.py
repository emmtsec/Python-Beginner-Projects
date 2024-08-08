from colorama import Fore
class Caesar(object):

    def CryptologyPassword(self):

        CryptoPassword = input("Enter the password to be encrypted: ")
        CryptoASCİİ = input("The sentence will be increased many times you Şifrenel ASCII characters: ")
        Password = ""
        if CryptoASCİİ.isdigit():
            CryptoASCİİ = int(CryptoASCİİ)
            for Crypto in CryptoPassword:
                Password = Password + chr(ord(Crypto) + CryptoASCİİ)
            Password = Fore.GREEN + Password + Fore.RESET
            Right = Fore.CYAN + "-> " + Fore.RESET
            Generated = "Generated " + Fore.RED + "Caesar Password" + Fore.RESET
            print(Generated, Right, Password)
        else:
            print("Please dial numeric expressions!")
start = Caesar()
start.CryptologyPassword()