# checking ip

# libs
import subprocess
from pif import get_public_ip
from colorama import Fore, Back, Style
import json
import urllib.request
from urllib.request import urlopen
from json import load
import os


print(Fore.GREEN + "[" + Fore.MAGENTA + "x" + Fore.GREEN + "]" + Style.RESET_ALL + " YOUR IP: " + get_public_ip()) # your ip address
print(" ")

getIP = input(Fore.GREEN + "[" + Fore.CYAN + "DK" + Fore.GREEN + "]" + Style.RESET_ALL + " Enter IP Address >>> ") # enter ip address
url = "https://ipinfo.io/" + getIP + "/json"

try: # get info about entered ip address
    url = "https://ipinfo.io/" + getIP + "/json"
    getInfo = urllib.request.urlopen(url)
    infoList = json.load(getInfo)

    print(" ")
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " IP: ", infoList["ip"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " City: ", infoList["city"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Region: ", infoList["region"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Country: ", infoList["country"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Location: ", infoList["loc"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Organisation: ", infoList["org"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Postal: ", infoList["postal"])
    print(Fore.GREEN + "[" + Fore.MAGENTA + "+" + Fore.GREEN + "]" + Style.RESET_ALL + " Timezone: ", infoList["timezone"])          
        
except: # error
    print(" ")
    print(Fore.GREEN + "[" + Fore.RED + "ERROR" + Fore.GREEN + "]" + Fore.CYAN + " Invalid IP Address!" + Style.RESET_ALL)
