import os
os.system('cd')
os.system('cd')
os.system('cd ../usr/etc')
os.system('rm -rf bash.bashrc')
isim = input('İsim yaz >>> ')
alt = input('Alt yazı >>> ')
code = """shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth
PROMPT_DIRTRIM=2
PS1='\[\e[1;40m\]┌(\[\e[1;31m\]Termux@localhost\e[0m\]\[\e[1;40m\])-[\[\e[1;32m\]\w\[\e[0m\]\[\e[0;97m\]\[\e[1;35m\]]
└\[\e[1;40m\]\$\[\e[0m\] \[\e[1;36m\]'
"""
ıs = (isim)
pyf = "pyfiglet"
bos = " "
code2 = (pyf+bos+ıs)
code3 = """
ec = echo
code4 =(ec)                                       (alt)
"""
code5 ="""
 if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
"""
ths = open("bash.bashrc", "w")
ths.write(code+code2+code3+code4+code5)
