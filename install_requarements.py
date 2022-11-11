# installing libs

import subprocess

try: # install colorama
    import colorama 
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mColorama already installed!'])
except ImportError as e:
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mColorama not installed! Installing..'])
    subprocess.run(['pip', 'install', 'colorama'])
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mColorama installed!'])

try: # install requests
    import requests
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mRequests already installed!'])
except ImportError as e:
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mRequests not installed! Installing..'])
    subprocess.run(['pip', 'install', 'requests'])
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mRequests installed!'])

try: # install pif
    import pif
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mPif already installed!'])
except ImportError as e:
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mPif not installed! Installing..'])
    subprocess.run(['pip', 'install', 'pif'])
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mPif installed!'])

try: # install json
    import json
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mJson already installed!'])
except ImportError as e:
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mJson not installed! Installing..'])
    subprocess.run(['pip', 'install', 'json'])
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mJson installed!'])

try: # install urllib
    import urllib
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mUrllib already installed!'])
except ImportError as e:
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mUrllib not installed! Installing..'])
    subprocess.run(['pip', 'install', 'urllib'])
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mUrllib installed!'])

try: # install beatifulsoap
    import beautifulsoup4
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mBS4 already installed!'])
except ImportError as e:
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mBS4 not installed! Installing..'])
    subprocess.run(['pip', 'install', 'beautifulsoup4'])
    subprocess.run(['echo', '-e', '\033[32m[\033[31mINFO\033[32m] \033[36mBS4 installed!'])
