import os
import time
import file_search
from colorama import Fore, init

os.system("cls")
mainc = "\u001b[35;1m"
white = Fore.RESET
banner = f"""
{mainc}
    ███████╗██╗██╗░░░░░███████╗ ░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗███████╗██████╗░
    ██╔════╝██║██║░░░░░██╔════╝ ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗
    █████╗░░██║██║░░░░░█████╗░░ ╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║█████╗░░██████╔╝
    ██╔══╝░░██║██║░░░░░██╔══╝░░ ░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║██╔══╝░░██╔══██╗
    ██║░░░░░██║███████╗███████╗ ██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║███████╗██║░░██║
    ╚═╝░░░░░╚═╝╚══════╝╚══════╝ ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝{white}

                                    Mady by Crazex0303

"""

print(banner)

print("[0] C:")
print("[1] D:")
print("[2] E:")
print("[3] F:")
print("[4] G:")

driveinput = input("What Drive do you want to scan: ")

if driveinput == "0":
    os.system("cls")
    os.chdir("C:")
    usrinput = input("Name of the File to search: ")
    os.system("cls")
    files = file_search.searchFile(usrinput)
    print("File found at:", files)
    time.sleep(1500)

if driveinput == "1":
    os.system("cls")
    os.chdir("D:")
    file_search.set_root("D:")
    usrinput = input("Name of the File to search: ")
    os.system("cls")
    files = file_search.searchFile(usrinput)
    if files == files:
        print("File found at:", files)
        time.sleep(1500)

if driveinput == "2":
    os.system("cls")
    os.chdir("E:")
    file_search.set_root("E:")
    usrinput = input("Name of the File to search: ")
    os.system("cls")
    files = file_search.searchFile(usrinput)
    if files == files:
        print("File found at:", files)
        time.sleep(1500)

if driveinput == "3":
    os.system("cls")
    os.chdir("F:")
    file_search.set_root("F:")
    usrinput = input("Name of the File to search: ")
    os.system("cls")
    files = file_search.searchFile(usrinput)
    if files == files:
        print("File found at:", files)
        time.sleep(1500)

if driveinput == "4":
    os.system("cls")
    os.chdir("G:")
    file_search.set_root("G:")
    usrinput = input("Name of the File to search: ")
    os.system("cls")
    files = file_search.searchFile(usrinput)
    if files == files:
        print("File found at:", files)
        time.sleep(1500)

else:
    os.system("cls")
    print("Please select one of the given Drives")
    time.sleep(1500)