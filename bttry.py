#import os

#bttry == substr(os.system("acpi -b")
#print(bttry)

import subprocess
#str outputcmd 
outputcmd = subprocess.check_output("acpi -b", shell=True)

# print(outputcmd[11:19].decode())

if (outputcmd[11:19].decode()=='Charging'):
  # print ('Cargando ....')
  pass 
elif (outputcmd[11:15].decode()=='Full'):
  pass 
elif (outputcmd[11:19].decode()=='Discharg'):
  # print ("⌁",outputcmd[24:27].decode())
  print ("⚡",outputcmd[24:27].decode())
else:
 # print ("⌁",outputcmd[24:27].decode())
  pass


#  upower -i $(upower -e | grep BAT) | grep --color=never -E "state|to\ full|to\ empty|percentage"
