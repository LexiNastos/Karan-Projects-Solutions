import random #importing the old random module

def coinflip(times): #define the coinflip function with the argument as the number of times 
	heads = 0
	tails = 0
	
	for x in range(times):
		i = random.choice([0,1])
		
		if i == 0:
			print "Heads"
			heads += 1
		
		else:
			print "Tails"
			tails += 1
		
		print ('heads count' + str(heads))
		print ('tails count' + str(tails))

coinflip(int(raw_input('> How Many Coin Flips? Input A Number > ')))
