#!/usr/bin/python
# coding=utf-8
#jangan di recode ngentot
#recode jomblo seumur hidup
# (MR.K7C8NG) PEMBUAT
#SUBSCRIBE CHANNEL mrk7c8ng-ices
#FOLLOW INSTAGRAM @pranata_pasha

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding( utf8 )
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [( User-Agent , Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16 )]

#-Keluar-#
def keluar():
	print "\033[1;91m[!] Exit"
	os.sys.exit()
	
#-Warna-#
def acak(x):
    w =  mhkbpcP 
    d =   
    for i in x:
        d +=  ! +w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
def cetak(x):
    w =  mhkbpcP 
    for i in w:
        j = w.index(i)
        x= x.replace( !%s %i, \033[%s;1m %str(31+j))
    x +=  \033[0m 
    x = x.replace( !0 , \033[0m )
    sys.stdout.write(x+ \n )
	
#-Animasi-#
def jalan(z):
	for e in z +  \n :
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
##### LOGO #####
logo = """\033[1;96m█████████
\033[1;96m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;96m█\033[1;91m▼▼▼▼▼ \033[1;95m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
\033[1;96m█ \033[1;92m \033[1;95m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;96m█\033[1;91m▲▲▲▲▲\033[1;95m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;96mGOLD-SETAN
\033[1;96m█████████      \033[1;92m«----------✧----------»
\033[1;96m ██ ██
\033[1;96m╔══════════════════════════════════════════════╗
\033[1;96m║\033[1;96m* \033[1;95mAuthor  \033[1;93m: \033[1;95mBrother•MR.K7C8NG \033[1;96m                ║
\033[1;96m║\033[1;96m* \033[1;96mGitHub  \033[1;93m: \033[1;96m\033[4mhttps://github.com/pashayogi\033[0m \033[1;96m     ║
\033[1;96m║\033[1;96m*\033[1;93mYOUTUBE  \033[1;93m: \033[1;91m\033mhttps://youtube.com/c/mrk7c8ng\033[0m \033[1;96m   ║
\033[1;96m║\033[1;97m*\033[1;97mINSTAGRAM\033[1;92m: \033[1;96m\033m@pranata_pasha\033[0m \033[1;96m                   ║
\033[1;96m╚══════════════════════════════════════════════╝"""

# titik #
def tik():
	titik = [ .    , ..   , ...  ]
	for o in titik:
		print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### LICENSE #####
#=================#
def lisensi():
	os.system( reset )
	masuk()

##### Pilih Login #####
def masuk():
	os.system( reset )
	print logo
	print "\033[1;91m║--\033[1;91m> \033[1;95m1.\033[1;96m Login"
	print "\033[1;92m║--\033[1;91m> \033[1;95m2.\033[1;96m Login using token"
	print "\033[1;93m║--\033[1;91m> \033[1;95m0.\033[1;96m Exit"
	print "\033[1;95m║"
	msuk = raw_input("\033[1;96m╚═\033[1;1mD \033[1;93m")
	if msuk =="":
		print"\033[1;91m[!] Wrong input"
		keluar()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="0":
		keluar()
	else:
		print"\033[1;91m[!] Wrong input"
		keluar()
		
##### LOGIN #####
#================#
def login():
	os.system( reset )
	try:
		toket = open( login.txt , r )
		menu() 
	except (KeyError,IOError):
		os.system( reset )
		print logo
		print( \033[1;96m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆] )
		id = raw_input( \033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m  )
		pwd = getpass.getpass( \033[1;95m[+] \033[1;93mPassword \033[1;93m:\033[1;95m  )
		tik()
		try:
			br.o
