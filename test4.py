from proxy_parse import ProxyParser
import requests
import urllib
import json
import socks5
#proxy_parser = ProxyParser()
#proxies_list = proxy_parser.parse()

#my_file = open("BabyFile.txt", "w+")
#my_file.write(proxies_list)
#my_file.close()

#print(f'Обнаружено бесплатных прокси - {len(proxies_list)}:')
#for i in range(len(proxies_list)):
#    print(f"{i+1}) {proxies_list[i]}")

#session = requests.Session()

#proxies_list = {
#    'https': 'socks://172.64.157.2:80'
#}
#export all_proxy="socks://172.64.157.2:8080"

#r = session.get("https://ipinfo.io", proxies=proxies_list, timeout=1.5).text.strip()
#resp = requests.get('http://go.to',
                    #proxies=dict(http='s/172.64.1ocks:/57.2:8080',
                                 #https='socks://172.64.157.2:8080'))
#print(resp)


#print("Страница запроса с IP:", requests.get("http://icanhazip.com", timeout=1.5, proxies=proxies).text.strip())