#import os

import subprocess

outputcmd = subprocess.check_output("df -h /home", shell=True)


var1 = int(outputcmd[83:85].decode())

var2 = outputcmd[83:86].decode()
min = 97  #threshold
# print (outputcmd[83:85].decode())
if (var1 < min):
  # print ("poquitos " + var2)
  pass 
elif (var1 >= min):
  #pass 
   print ("/home " + var2 + " ")
else:
 # print ('descargando ....')
  print ("👽 ",var2)


