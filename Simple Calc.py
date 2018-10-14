# SimpleCalc can Add, Subtract, Multiply and Divide 2 Numbers

# This Function Adds Two Numbers : 
def add(x, y):
   return print("\nResult: {0} + {1} = {2}".format(x,y,x + y))

# This Function Subtracts 2 Numbers :
def subtract(x, y):
   return print("\nResult: {0} - {1} = {2}".format(x,y,x - y))

# This Function Multiplies Two Numbers :
def multiply(x, y):
   return print("\nResult: {0} * {1} = {2}".format(x,y,x * y))

# This Function Divides 2 Numbers :
def divide(x, y):
   return print("\nResult: {0} / {1} = {2}".format(x,y,x / y))

while True:
	print("\n ****** Welcome to SimpleCalc by Abhi. ****** \nThis Calculator Performs Operations on 2 Numbers.\nSelect Desired Option To Continue...")
	print("\n1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")
	print("5. Exit")	
	
	# Input From User 
	choice = input("\nEnter Choice (1/2/3/4/5): ")

	if choice == '1':
		num1 = int(input("\nEnter 1st Number: "))
		num2 = int(input("Enter 2nd Number: "))
		add(num1,num2)

	elif choice == '2':
		num1 = int(input("\nEnter 1st Number: "))
		num2 = int(input("Enter 2nd Number: "))
		subtract(num1,num2)

	elif choice == '3':
		num1 = int(input("\nEnter 1st Number: "))
		num2 = int(input("Enter 2nd Number: "))
		multiply(num1,num2)

	elif choice == '4':
		num1 = int(input("\nEnter 1st Number: "))
		num2 = int(input("Enter 2nd Number: "))
		divide(num1,num2)
	
	elif choice == '5':
		exit()
	
	else:
		print("\nInvalid Input")