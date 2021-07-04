#!/usr/bin/env python 

import os 

os.system("pkg install cowsay")
os.system("pkg install figlet")
os.system("clear")
os.system("figlet TUNGA")
os.system("cowsay coded by ALP ER TUNGA")
print("""

web hacking tool

(1) nikto
(2) sqlmap
(3) admin panel finder 
(4) rapidscan
(5) RED_HAWK
(6) SiteBroker
(7) XSS 
(8) cupp (wordlist)
(9) site bilgi toplama
(10) hizli port tarama
(11) versiyon bilgisi
(12) easymap
(Q) cikis

""")

giris=input("SECİM: ")

if giris=="1":
	os.system("git clone https://github.com/sullo/nikto.git")
	os.system("clear")
if giris=="2":
	os.system("git clone https://github.com/sqlmapproject/sqlmap")
	os.system("clear")
if giris=="3":
	os.system("git clone https://github.com/bdblackhat/admin-panel-finder")
	os.system("clear")
if giris=="4":
	os.system("git clone https://github.com/skavngr/rapidscan")
	os.system("clear")
if giris=="5":
	os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
	os.system("clear")
if giris=="6":
	os.system("git clone  https://github.com/Anon-Exploiter/SiteBroker.git")
	os.system("clear")
if giris=="7":
	os.system("git clone https://github.com/ujjwal96/njaXt")
	os.system("clear")
if giris=="8":
	os.system("git clone https://github.com/Mebus/cupp")
	os.system("clear")
if giris=="9":
	hedefip= input("hedef  site giriniz: ")
	os.system("whois "+hedefip)
if giris=="10":
	hedefip= input("hedef  site giriniz: ")
	os.system("nmap "+hedefip)
if giris=="11":
	hedefip= input("hedef  site giriniz: ")
	os.system("nmap -sV "+hedefip)
if giris=="12":
	os.system("git clone https://github.com/Cvar1984/Easymap")
	os.system("clear")
if giris=="Q" or giris=="q":
	quit()
else:
	print("iyi günler")
