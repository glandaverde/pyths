
# import urllib library
from urllib.request import urlopen
  
# import json
import json
import os
# store the URL in url as 
# parameter for urlopen

	
prev = ""
url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json =json.loads(response.read())
current=data_json['USD']
# print(str(current))

with open('.prevbtc.txt', 'r') as reader:
	prev=reader.read()
	#print(prev)

# print (prev)	

previous = float(prev)
flo = ((current- previous)/previous)*100

with open('.prevbtc.txt', 'w') as writer:
	writer.write(str(current))
	
threshold=2.00
# print(str(round(flo,3))+'%')
	
if (flo>threshold):
  print("BTC "+str(current)+" | " + str(round(flo,3)) + "% Increase")
elif(flo<-threshold):
  print("BTC "+str(current)+" | " + str(round(flo,3)) + "% Decrease")
else:
  print("₿")


