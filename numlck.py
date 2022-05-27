#import os

#bttry == substr(os.system("acpi -b")
#print(bttry)

import subprocess
#str outputcmd 
outputcmd = subprocess.check_output("xset q|grep 'Num Lock'", shell=True)
keyb = subprocess.check_output("setxkbmap -v | awk -F '+' '/symbols/ {print $2}'", shell=True)
#print(outputcmd[21:23].decode())

if (outputcmd[45:47].decode()=='on' and outputcmd[21:23].decode()=='on'):
	print ("NL CL "+keyb.decode().upper())
elif (outputcmd[45:47].decode()=='on'):
	print ("NL "+keyb.decode().upper())
elif (outputcmd[21:23].decode()=='on'):
	print ("CL "+keyb.decode().upper())
else:
        print (keyb.decode().upper())


