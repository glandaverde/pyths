#import os

#bttry == substr(os.system("acpi -b")
#print(bttry)

import subprocess
#str outputcmd 
outputcmd = subprocess.check_output("sudo dnf check-update|wc", shell=True)

# print(outputcmd[11:19].decode())
var1 = int(outputcmd[5:8].decode())
var2 = str(var1-2)
var1 = var1-2
min = 30

if (var1 < min):
  # print ("poquitos " + var2)
  pass 
elif (var1 >= min):
  #pass 
   print ("🡇" + var2 + " ")
else:
 # print ('descargando ....')
  print ("👽 ",var2)




