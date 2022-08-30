import youtube_dl
import socket
import sys 
import time

VERSION="2.0"
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
'''+BLUE+'''                                                                    
'''+PURPLE+'''
'''

DESCRIPTION=f'''
'''+WHITE+'''Author :'''+BLUE+''' '''+ AUTHOR+'''
'''+WHITE+'''Version :'''+PURPLE+''' '''+ VERSION+'''
'''+BLUE+'''FOR EDUCATIONAL PURPOSE ONLY.
'''+WHITE


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
    slowprint(LOGO)
    slowprint2(DESCRIPTION)
    print("")

    on_off = 0

    while on_off == 0:
        video_url = input(f"{BLUE}Please enter youtube video URL or Q for quit this program : {PURPLE}")
        if video_url == "Q":
            print(f"Have a good day!{WHITE}")
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

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

if __name__=='__main__':

        run(LOGO, DESCRIPTION)
        
