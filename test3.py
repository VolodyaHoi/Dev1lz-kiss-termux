# checking phone number

import subprocess
from colorama import Fore, Back, Style
import json
import urllib.request
from urllib.request import urlopen
from json import load
import os

phoneNumber = input(Fore.GREEN + "[" + Fore.CYAN + "DK" + Fore.GREEN + "]" + Style.RESET_ALL + " Enter phone number >>> ")
getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phoneNumber

try:
    infoPhone = urllib.request.urlopen(getInfo)
    infoPhone = json.load(infoPhone)

    print(" ")
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Phone Number: ", "+" + phoneNumber)
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Country: ", infoPhone["country"]["english"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Region: ", infoPhone["region"]["english"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " District: ", infoPhone["region"]["okrug"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " AutoCod: ", infoPhone["region"]["autocod"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Location: ", infoPhone["0"]["latitude"], infoPhone["0"]["longitude"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Operator: ", infoPhone["0"]["oper"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Timezone: ", infoPhone["0"]["tz"])

except:
    print(" ")
    print(Fore.GREEN + "[" + Fore.RED + "ERROR" + Fore.GREEN + "]" + Fore.CYAN + " Invalid phone number!" + Style.RESET_ALL)