nan = float('nan')
inf = float('inf')

# Function to add two numbers 
def add(num1 = nan, num2 = nan):
	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		return 0
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1 = nan, num2 = nan):
	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		return 0
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1 = nan, num2 = nan):
	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		return 0
	multiplication = num1 * num2 
	return multiplication

# Function to divide two numbers 
def divide(num1 = nan, num2 = nan):
	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		return 0
	if(num2 == 0 and num1 == 0):
		return 0
	elif(num2 == 0):
		return inf
	division = num1/num2 
	return division

#Added Factorial function for integers to implement exp and log functions

Factorials = [1,1]

def fact(num1 = nan):
	try:
		num1 = int(num1)
	except ValueError:
		return 0

	if(num1 < 0):
		return 0
	elif(num1 < len(Factorials)):
		return Factorials[num1]
	else:
		temp = num1 * fact(num1 -1)
		Factorials.append(temp)
		return Factorials[num1]

# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1 = nan, num2 = nan): #num1 ^ num2
	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		return 0 
	return power
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a = nan, r = nan, n = nan): 
	try:
		a = float(a)
		r = float(r)
		n_new = int(n)
	except ValueError:
		return 0

	gp = []

	if(float(n) - n_new != 0):
		return 0
	else:
		n = n_new

	if(n < 0):
		return 0
	elif(n == 0):
		pass
	elif(a == 0):
		gp=[0 for _ in range(0,n)]
	else:
		gp.append(a);
		for i in range(1,n):
			gp.append(gp[i-1]*r)
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a = nan, d = nan, n = nan): 
	ap=[]
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a = nan, d = nan, n = nan): 
	hp=[]
	return hp

