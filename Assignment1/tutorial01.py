nan = float('nan')

# Function to add two numbers 
def add(num1 = nan, num2 = nan):
	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		return "Invalid arguments passed."
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1 = nan, num2 = nan):
	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		return "Invalid arguments passed."
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1 = nan, num2 = nan):
	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		return "Invalid arguments passed."
	multiplication = num1 * num2 
	return multiplication

# Function to divide two numbers 
def divide(num1 = nan, num2 = nan):
	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		return "Invalid arguments passed."
	if(num2 == 0):
		return "Division by 0 is not possible."
	division = num1/num2 
	return division
	
