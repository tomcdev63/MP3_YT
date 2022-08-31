import youtube_dl
import sys 
from tkinter import *
import time
import shutil
import os

# import serial.tools.list_ports
# Dans powershell pr lister les path des periph USB Get-PnpDevice -PresentOnly | Where-Object { $_. InstanceId -match '^USB' }

# MUSIC_PATH = r"Ce PC\Galaxy S8\Phone\Music\DOWN"
# print("Before moving file:") 
# print(os.listdir(MUSIC_PATH))


TARGET = r"\\192.168.1.148\NAS Tom\MUSIC2"
PATH_LOCAL = "\MUSIC"

VERSION="2.5"
AUTHOR="ThomaC"

BLACK="\033[0;30m"
RED="\033[0;91m"
BRED="\033[1;91m"
GREEN="\033[0;32m"
BGREEN="\033[1;32m"
YELLOW="\033[0;33m"
BYELLOW="\033[1;33m"
BLUE="\033[0;34m"
BBLUE="\033[1;34m"
PURPLE="\033[0;35m"
BPURPLE="\033[1;35m"
CYAN="\033[0;36m"
BCYAN="\033[1;36m"
WHITE="\033[0;37m"
NC="\033[00m"

LOGO='''
'''+PURPLE+''' __  __ ____ _____  __   _______   ____   ____ ____  ___ ____ _____ 
'''+BLUE+'''|  \/  |  _ \___ /  \ \ / /_   _| / ___| / ___|  _ \|_ _|  _ \_   _|
'''+PURPLE+'''| |\/| | |_) ||_ \   \ V /  | |   \___ \| |   | |_) || || |_) || |  
'''+BLUE+'''| |  | |  __/___) |   | |   | |    ___) | |___|  _ < | ||  __/ | |  
'''+PURPLE+'''|_|  |_|_|  |____/    |_|   |_|   |____/ \____|_| \_\___|_|    |_|
'''+WHITE

DESCRIPTION=f'''
'''+WHITE+'''Author :'''+BLUE+''' '''+ AUTHOR+'''
'''+WHITE+'''Version :'''+PURPLE+''' '''+ VERSION+'''
'''+BLUE+'''FOR EDUCATIONAL PURPOSE ONLY.
'''+WHITE


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


# samsung_connected = False

# def check_mobile():
#     ports = serial.tools.list_ports.comports()
#     print(f"\n{PURPLE}{ports}")
#     if samsung_connected == False and ports != []:
#         print("\nSamsung connecté!")
#         samsung_connected == True
#     elif samsung_connected == True and ports == []:
#         print("deconnection")
#     return ports
        


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def check_NAS(TARGET):
    
    on_off = 1
    if os.path.exists(TARGET):
        print(f"{GREEN}Server NAS connected")
    else:
        print(f"{RED}Server NAS not connected")
        on_off = 0
    return on_off


def definitive_path(TARGET, on_off):
    if on_off == 1:
        response_path = input(f"{BLUE}Would you like to copy the music to your NAS server? Y/N : {PURPLE}")
        if response_path == "Y":
            PATH_DEFINITIF = TARGET
        else:
            PATH_DEFINITIF = PATH_LOCAL
    else:
        PATH_DEFINITIF = PATH_LOCAL
    return PATH_DEFINITIF
    

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)


def slowprint2(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.03)


def run(LOGO, DESCRIPTION):
    # slowprint(LOGO)
    # slowprint2(DESCRIPTION)

    ### SAMSUNG
    # ports = check_mobile()
    # if len(ports) != 0:
    #     print(f"\n{GREEN}Your cell phone is ready to receive music!{WHITE}")
    # else:
    #     print("Your cell phone is not connected")
    # print("")

    ### NAS
    try:
        os.makedirs(PATH_LOCAL)
    except FileExistsError:
        pass

    nas_on_off = check_NAS(TARGET)
    path = definitive_path(TARGET, nas_on_off)

    on_off = 0
    while on_off == 0:
        try:
            video_url = input(f"{BLUE}Please enter YOUTUBE video URL or 'Q' for quit this program : {PURPLE}")
            if video_url == "Q":
                slowprint2(f"\nHave a good day!{WHITE}")
                on_off = 1
            else:
                video_info = youtube_dl.YoutubeDL().extract_info(
                    url = video_url,download=False
                )
                filename = f"{video_info['title']}.mp3"
                options={
                    'format':'bestaudio/best',
                    'keepvideo':False,
                    'outtmpl':filename,
                }

                with youtube_dl.YoutubeDL(options) as ydl:
                    ydl.download([video_info['webpage_url']])

                print(f"{GREEN}Download complete... {filename}{WHITE}")
                try:
                    shutil.move(filename, path)
                except:
                    pass
        except:
            print(f"{RED}Le format de la vidéo n'est pas ok{WHITE}")
            

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

if __name__=='__main__':

        run(LOGO, DESCRIPTION)
        
