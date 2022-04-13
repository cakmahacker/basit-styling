import os
import os.path
import colorama
import random
import time
from colorama import Fore, Back, Style
from termcolor import colored



os.system('clear')

class bcolors:
    CYAN = '\033[36m'
    PEMBE = '\033[95m'
    MAVI = '\033[94m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    BEYAZ = '\033[0m'
    BOLD = '\033[1m'
    ALTCIZGI = '\033[4m'
#coded by Cakma_H4CK3R

print(f"""
   
    {bcolors.KIRMIZI}[{bcolors.YESIL}01{bcolors.KIRMIZI}]{bcolors.BEYAZ}Styling oluştur...
    {bcolors.KIRMIZI}[{bcolors.YESIL}02{bcolors.KIRMIZI}]{bcolors.BEYAZ}Eski temayı geri yükle...
    {bcolors.KIRMIZI}[{bcolors.YESIL}03{bcolors.KIRMIZI}]{bcolors.BEYAZ}Güncelle (GitHub)

""")



secim = input(f"""{bcolors.MAVI}Seçenek giriniz {bcolors.KIRMIZI}»{bcolors.BEYAZ} """)




if secim=="00":
    os.system('python3 tema.py')


if secim=="01":
    
    os.system('clear')
    time.sleep(2)
    print(f'''{bcolors.CYAN}

    Eski dosyanın kaydedileceği dosyanın adı{bcolors.MAVI} ¦{bcolors.SARI}örn{bcolors.KIRMIZI} ({bcolors.SARI} eskitema {bcolors.KIRMIZI}) ''')
    print()
    print()
    eskkyt = input(f'{bcolors.MAVI}    Kayıt alanı » ')

    if eskkyt=='':
        f0 = 'rastgele_'
        f1 = '139594'
        f2 = 'abcdefg'
        f3 = str("". join(random.choice(f1)for i in range(8)))
        f4 = str("". join(random.choice(f2)for i in range(1)))
        ffortopklsr = f0+f3+f4
        print(f'''
    {bcolors.BEYAZ} Bu alanı boş bıraktığınız için''')
        print(f'{bcolors.BEYAZ}    Dosya{bcolors.SARI} '+ffortopklsr+f'{bcolors.BEYAZ} klosörüne kaydedilecek')

        def save_file_at_dir(dir_path, filename, file_content, mode='w'):
            os.makedirs(dir_path, exist_ok=True)
            with open(os.path.join(dir_path, filename), mode) as f:
                f.write(file_content)

        save_file_at_dir('/data/data/com.termux/files/home/basit-styling/'+ffortopklsr, 'not.txt', '''Bu araç gelişim aşamasındadır ''')
        os.system("cp /data/data/com.termux/files/usr/etc/bash.bashrc /data/data/com.termux/files/home/basit-styling/"+ffortopklsr)

#......#

#......#

    def save_file_at_dir(dir_path, filename, file_content, mode='w'):
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, filename), mode) as f:
            f.write(file_content)

    save_file_at_dir('/data/data/com.termux/files/home/basit-styling/'+eskkyt, 'not.txt', '''Bu araç gelişim aşamasındadır ''')

#
#    os.system('clear')


    kyt1 = ('cp /data/data/com.termux/files/usr/etc/bash.bashrc /data/data/com.termux/files/home/basit-styling/')
    os.system(kyt1+eskkyt)





#    os.system('clear')
    time.sleep(2)
    print(f'''
    {bcolors.KIRMIZI}[ {bcolors.YESIL}✓{bcolors.KIRMIZI} ] {bcolors.BEYAZ} Eski tema kaydedildi...

    ''')





#coded by Cakma_H4CK3R



    time.sleep(1)
    devammı = input(f"""{bcolors.BEYAZ}Devam ise {bcolors.YESIL}> 
{bcolors.BEYAZ}Geri dönmek için {bcolors.KIRMIZI}< {bcolors.BEYAZ}yazınız...
{bcolors.CYAN}
└$ """)

    if devammı==">":
        print()
        print()


        code= """

    clear
    shopt -s histappend
    shopt -s histverify
    export HISTCONTROL=ignoreboth
    PROMPT_DIRTRIM=2
    PS1='\[\e[1;40m\]┌(\[\e[1;31m\]"""

#coded by Cakma_H4CK3R

        codeee= """\e[0m\]\[\e[1;40m\])-[\[\e[1;32m\]\w\[\e[0m\]]\[\e[0;97m\]\[\e[1;35m\]\033[44;37;5m Dizin \033[0m
└\[\e[1;40m\]\$\[\e[0m\] \[\e[1;36m\]'
    printf "\e[40m\e[31m"

"""





        isim= input(f'{bcolors.MAVI}Figlet İsmi{bcolors.BEYAZ} »{bcolors.SARI} ')
        pyfb= "pyfiglet "
        terminalnck = input(f'{bcolors.MAVI}Terminal ismi {bcolors.SARI}örn{bcolors.MAVI} ¦{bcolors.KIRMIZI}({bcolors.BEYAZ} cakma@localhost{bcolors.KIRMIZI} ){bcolors.BEYAZ} »{bcolors.BEYAZ} ')


#
        ara = """

"""
##########################
#coded by Cakma_H4CK3R
#coded by Cakma_H4CK3R
##########################
        print()
        print()
        print(f'''{bcolors.MAVI}Sosyal medya bırak {bcolors.SARI}örn{bcolors.KIRMIZI}({bcolors.SARI} Instagram @cakma_hack3r {bcolors.KIRMIZI}) ''')
        print()
        tgn = input(f'{bcolors.MAVI}Sosyal medya{bcolors.BEYAZ} »{bcolors.PEMBE} ')
#
        print(f'{bcolors.BEYAZ}')

        beyaz = '''
printf "\e[37m\e[40m"

'''
#
        ec = "echo    ㅤㅤㅤ"


        tam = """


        echo '  '
         if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
                command_not_found_handle() {
                        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
                }
        fi
        """

        dosyaa= open("/data/data/com.termux/files/usr/etc/bash.bashrc", "w")
        dosyaa.write(code+terminalnck+codeee+pyfb+isim+ara+beyaz+ec+tgn+tam)
        dosyaa.close()


        time.sleep(2)
        print(f'''
    {bcolors.KIRMIZI}[ {bcolors.YESIL}✓{bcolors.KIRMIZI} ] {bcolors.BEYAZ} Yeni tema uygulandı

    ''')
        time.sleep(3)
        annaaa= input('    Ana menü için ¦ENTER¦')
        os.system('python3 tema.py')


#coded by Cakma_H4CK3R
#coded by Cakma_H4CK3R




    if devammı=="<":
        print('''         GERİ DÖNÜLÜYOR...  ''')
        time.sleep(3)
        os.system('python3 tema.py')

    else:
        print()
        print(f"""    {bcolors.YESIL}[{bcolors.KIRMIZI}×{bcolors.YESIL}]{bcolors.BEYAZ} HATALI KOD YAZILDI

    LÜTFEN DAHA DİKKATLİ OL             """)
        time.sleep(2)
        print()
        print()
        annaaa= input(f'''{bcolors.CYAN}   Ana menü için ¦ENTER¦{bcolors.BEYAZ}''')
        os.system('python3 tema.py')





if secim=="02":
    print('''
    Eski temanın kaydedildiği dizin adını giriniz ''')

    eskdizini = input(f'{bcolors.CYAN}    Eski tema dizini:{bcolors.BEYAZ} ')
    if eskdizini=='':
        print('''
    Bu alan boş bırakılamaz..!

''')
        time.sleep(3)
        print()
        annaaa= input('    Ana menü için ¦ENTER¦')
        os.system('python3 tema.py')



#coded by Cakma_H4CK3R
#coded by Cakma_H4CK3R


    kyt11=('/data/data/com.termux/files/home/basit-styling/'+eskdizini+'/bash.bashrc')


    PATH=(kyt11)
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print (f"""

    {bcolors.KIRMIZI}[ {bcolors.YESIL}...{bcolors.KIRMIZI} ] {bcolors.BEYAZ} İşlem başlatılıyor...""")
        os.system('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
        os.system('cp '+kyt11+' /data/data/com.termux/files/usr/etc')
        time.sleep(3)
        print()
        print (f"""

    {bcolors.KIRMIZI}[ {bcolors.YESIL}✓{bcolors.KIRMIZI} ] {bcolors.BEYAZ} Seçilen tema uygulandı...""")
        time.sleep(3)
        print()
        annaaa= input('    Ana menü için ¦ENTER¦')
        os.system('python3 tema.py')

    else:
        print (f"""

    {bcolors.YESIL}[{bcolors.KIRMIZI}×{bcolors.YESIL}]{bcolors.BEYAZ} Dosya bulunamadı..!""")
        time.sleep(3)
        print()
        annaaa= input('    Ana menü için ¦ENTER¦')
        os.system('python3 tema.py')

if secim=="03":
    print (f"""

    {bcolors.SARI}[ {bcolors.YESIL}!{bcolors.SARI} ] {bcolors.BEYAZ} Güncelleme başlatılıyor...""")
    time.sleep(3)
    os.system('rm -rf /data/data/com.termux/files/home/basit-styling/tema.py&&curl -L -O https://github.com/cakmahacker/basit-styling/raw/main/tema.py')
    print (f"""
    {bcolors.SARI}[ {bcolors.YESIL}✓{bcolors.SARI} ] {bcolors.BEYAZ} Güncelleme bitti.""")
    time.sleep(3)
    annaaa= input('    yeniden başlatmak için ¦ENTER¦')
    os.system('python3 tema.py')
else:
    print (f"""

    {bcolors.YESIL}[{bcolors.KIRMIZI}×{bcolors.YESIL}]{bcolors.BEYAZ} Hatalı seçim..!""")
    time.sleep(3)
    print()
    annaaa= input('    Ana menü için ¦ENTER¦')
    os.system('python3 tema.py')
