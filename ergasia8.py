import random
import time

def findCombos(combos):
	num = 0
	num2 = random.sample(range(-30,30),30)
	for i in range(30):
		x = num2[i]
		for j in range(i+1,30):
			y = num2[j]
			for z in range(j+1,30):
				if -x == y+num2[z] :
					num = num+1
					combos.append([x,y,num2[z]])
	return num
def Print(combos,num):
	if combos == []:
		print ("Den uparxoun diathesimoi sundiasmoi!!")
	else:
		print (num)
		for i in range(num):
			print (combos[i])
			
start_time = time.time()
combos = []
num = findCombos(combos)
Print(combos,num)
print (time.time() - start_time)
