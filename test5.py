from scapy.all import *
import sys
import os
import signal

try:
    SRCMAC - packet[0].addr2
    DSTMAC = packet[0].addr1
    BSSID = packet[0].addr3
except:
    print ("Cannor read MAC address")

try:
    SSIDSize = packet[0][Dot11Elt].len
    SSID = packet[0][Dot11Elt].info
except:
    SSID = ""
    SSIDSize = 0

if packet[0].type == 0:
    ST = packet[0][Dot11Elt].subtype
    if str(ST) == "8" && SSID != "" && DSTMAC.lower() == "ff:ff:ff:ff:ff:ff":
        p = packet[Dot11Elt]
        cap = packet.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}"
                            "{Dot11ProbeResp:%Dot11ProbeResp.cap%}").split("+")
        channel = None
        crypto = set()

os.system("ifconfig " + iface + " down")

try:
    os.system("iwconfig " + iface + " mode monitor")
except:
    print("Error")
    sys.exit(1)

os.system("ifconfig " + iface + " up")

if not os.geteuid() == 0:
    print("no root")
    exit(1)

parameters = {sys.argv[1]:sys.argv[2]}
if "mon" not in str(parameters["-i"]):
    newiface = setup_monitor(parameters["-i"])
else:
    newiface = str(parameters["-i"])

ssid_list = {}
s = conf.L2socket(iface=newiface)

print(str(newiface) + "\n")
sniff(iface=newiface, prn=sniffpackets, store=0)