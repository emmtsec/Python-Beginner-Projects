from colorama import Fore
class Menu(object):
    def MenuDesign(self):
        print("""               """ + Fore.LIGHTYELLOW_EX + """    +----------------+
                   """ + Fore.RED + """| Safe Passwords | www.instagram.com/pr0xy.dogus
                   """ + Fore.RESET + Fore.LIGHTGREEN_EX + """| pr0xy12        | www.github.com/pr0xy12
                """ + Fore.LIGHTYELLOW_EX + """   +----------------+   """ + Fore.RESET + Fore.CYAN + """
        [1] """ + Fore.YELLOW + """-> """ + Fore.RESET + Fore.MAGENTA + """Only letters are formed""" + Fore.RESET 
        + Fore.CYAN + """
        [2] """ + Fore.YELLOW + """-> """ + Fore.RESET + Fore.MAGENTA + """It only consists of numbers""" + Fore.RESET 
        + Fore.CYAN + """
        [3] """ + Fore.YELLOW + """-> """ + Fore.RESET + Fore.MAGENTA + """Get mixed password""" + Fore.RESET + Fore.GREEN + """ *[Character and Number]* """ + Fore.RESET  
        + Fore.CYAN + """
        [4] """ + Fore.YELLOW + """-> """ + Fore.RESET + Fore.MAGENTA + """Mixed and special characters """ + Fore.RESET + Fore.GREEN + """*[/ * $]*""" + Fore.RESET + """
        """ + Fore.CYAN + """[5] """ + Fore.RESET + Fore.YELLOW + """-> """ + Fore.RESET + Fore.MAGENTA + """Whether Caesar encryption method """ + Fore.RESET + Fore.GREEN + """*[Recommended]*
        """ + Fore.RESET)
start = Menu()
start.MenuDesign()