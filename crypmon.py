
# import urllib library
from urllib.request import urlopen
  
# import json
import json
import os
# store the URL in url as 
# parameter for urlopen
import time
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text
    
x = 3600 # Put in whatever seconds you want it to wait

def get_info(cryptocoin):
	prev = ""
	url = "https://min-api.cryptocompare.com/data/price?fsym="+cryptocoin+"&tsyms=USD"
	  
	# store the response of URL
	response = urlopen(url)
	  
	# storing the JSON response 
	# from url in data
	data_json =json.loads(response.read())
	current=data_json['USD']
	# print(str(current))

	with open('/home/shared/Apps/pyths/.prevcry'+cryptocoin+'.txt', 'r') as reader:
		prev=reader.read()
		#print(prev)

	# print (prev)	

	previous = float(prev)
	flo = ((current- previous)/previous)*100

	with open('/home/shared/Apps/pyths/.prevcry'+cryptocoin+'.txt', 'w') as writer:
		writer.write(str(current))
		
	threshold=2.00
	# print(str(round(flo,3))+'%')
		
	#if (flo>threshold):
	#  print("BTC "+str(current)+" | " + str(round(flo,3)) + "% Increase")
	#elif(flo<-threshold):
	#  print("BTC "+str(current)+" | " + str(round(flo,3)) + "% Decrease")
	#else:
	# print("₿")
	#print(cryptocoin+" "+str(current)+" | " + str(round(flo,3)) + "% Change from "+prev)
	print(cryptocoin+" "+str(current)+" | " + str(round(flo,2)) + "% ")
	



while True:

	get_info("BTC")
	get_info("ETH")
	get_info("ADA")
	get_info("SOL")
	get_info("XRP")
	get_info("PAXG")
	get_info("LUNA")
	get_info("DOT")
	
	time.sleep(x) 
	clear()



