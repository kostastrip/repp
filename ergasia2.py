import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

def Read_Picks(picks):
	for i in range(10):
		exit = True
		while exit:
			num = raw_input("dwse arithmo %s : "%(i+1))
			try:
				num = int(num)
				
				if num in range(1,81) and not(num in picks):
					exit = False
					picks[i] = num
				else:
					print ("Dwse arithmo metaksu 1 kai 80")
			except:
				print ("Dwse arithmo metaksu 1 kai 80")


def Find_Wins(data,i):
	wins = 0
	for j in data['draws']['draw']:	
		tk = 0	
		num = data['draws']['draw'][i]['results']
		for z in range(10):
			if picks[z] in num:
				tk+=1
		if tk>4:
			wins+=1
		i+=1
	return wins
def Pull_Data(pro):
	now = pro.strftime("%d-%m-%Y")
	url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json"%now
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	data = json.loads(data)
	return data
def Save_Wins(pro):
	data = Pull_Data(pro)
	i = 0
	wins = Find_Wins(data,i)
	wins.append(wins)
	wins.append(pro.strftime("%d-%m-%Y"))
picks = [""]*10
Read_Picks(picks)
n = datetime.datetime.now()
wins = []

while pro>=de:
	Save_Wins(pro)
	pro = pro - datetime.datetime.now(pro=1)
datetime = wins.index(max(wins))

if max(wins) == 0:
        
	print ("kamia niki")
	print  ("???")
	
else:
	print ("pio polles nikes:"+wins)
