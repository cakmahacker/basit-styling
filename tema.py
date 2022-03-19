import os
import colorama
import time
from colorama import Fore, Back, Style
from termcolor import colored

class bcolors:
    PEMBE = '\033[95m'
    MAVI = '\033[94m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    BEYAZ = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#coded by Cakma_H4CK3R


os.system('clear')
os.system('cd')
os.system('cp /data/data/com.termux/files/usr/etc/bash.bashrc /data/data/com.termux/files/home/basit-styling')

print(f'''
    {bcolors.KIRMIZI}[ {bcolors.YESIL}✓{bcolors.KIRMIZI} ] {bcolors.BEYAZ} Eski tema kaydedildi...

    ''')

code= """

clear
shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth
PROMPT_DIRTRIM=2
PS1='\[\e[1;40m\]┌(\[\e[1;31m\]termux@localhost\e[0m\]\[\e[1;40m\])-[\[\e[1;32m\]\w\[\e[0m\]\[\e>
└\[\e[1;40m\]\$\[\e[0m\] \[\e[1;36m\]'
printf "\e[40m\e[31m"

"""
isim = input('İsim » ')
pyfb = "pyfiglet "
#
ara = """

"""
##########################
#coded by Cakma_H4CK3R
#coded by Cakma_H4CK3R
##########################
tgn = input('Tg nick » ')
#
beyaz = '''
printf "\e[37m\e[40m"

'''
#
ec = "echo           Telelgram ⌲ ⌲ ⌲ "


tam = """


echo '  '
 if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
"""

ths = open("/data/data/com.termux/files/usr/etc/bash.bashrc", "w")
ths.write(code+pyfb+isim+ara+beyaz+ec+tgn+tam)
#coded by Cakma_H4CK3R
#coded by Cakma_H4CK3R
