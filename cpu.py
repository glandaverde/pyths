#import os

import subprocess

outputcmd = subprocess.check_output("top -bn1 | grep '%Cpu(s)' | awk -F',' '{printf $4}'", shell=True)


var1 = float(outputcmd[0:6].decode())
#print(outputcmd[0:6].decode())
var2 = str(100-var1)
var3 = 100-var1
min = 90  #threshold


if (var3 < min):
  pass 
elif (var3 >= min):
  print("🔥")
  # print ("CPU " + var2 + "% ")
else:
  print ("👽 ",var2)



#Linux 5.16.18-200.fc35.x86_64 (fedorabox) 	04/07/2022 	_x86_64_	(2 CPU) avg-cpu:  %user   %nice %system %iowait  %steal   %idle          17.6%    4.6%   11.3%    0.1%    0.0%   66.4%
# top -bn1 | grep '%Cpu(s)' | awk -F',' '{printf "CPU id %: %.2f%\n", $4}'
# top -bn1 | grep '%Cpu(s)' | awk -F',' '{printf $4}'
# 41.9
