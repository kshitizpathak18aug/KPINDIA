
i=int(input("enter the value of i:"))
j=int(input("enter the value of j:"))
o=int(input("what do you want to do?+,-,*,/:"))



def add():
	return i+j
def sub():
	return i-j
def mult():
	return i*j
def dev():
	return i/j

	if(o=='+'):
		print("addition=",add())
	elif(o=='-'):
		print("subtraction=",sub())
	elif(o=='*'):
		print("multiplication=",mult())
	elif(o=='/'):
		print("devision=",dev())
		





