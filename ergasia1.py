from __future__ import division
import random

def setTable(gn):
	num=[]
	for i in range(100):
		tabNum.append(random.sample(gn,5))	
	return num

def findNum(choice,gn):
	x=[0]*80
	exit=True
	bingo=0
	while exit:
		bingo=bingo+1
		y=random.sample(gn,1)
		gn.remove(y[0])
		for i in range(0,80):
			if y[0] in choice[i]:
				x[i]+=1
				if x[i]==5:
					exit=False
	return bingo

bingo2=0
for i in range(1000):
	gn=range(1,81)
	players=setTable(gn)
	bingo2+=findNum(players,gn)
print (bingo2/1000)
