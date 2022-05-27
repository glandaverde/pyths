#import os

import subprocess

outputcmd = subprocess.check_output("uname", shell=True)

try:
	outputcmd = subprocess.check_output("playerctl metadata title", shell=True)
except subprocess.CalledProcessError as e:
        pass
    
var1 = outputcmd[0:5].decode()



if (var1 =="Linux"):
  pass
else:
    print ("▶⏸")



