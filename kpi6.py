import random
while True:
	k=input("press 'r' to roll the dice and 'q' to quit")
	if (k=='r'):
		print(random.randint(1,6))
	elif(k=='q'):
		print("GOOD BYE!")
		exit()
	else:
		print("give either 'r' or 'q'")
		