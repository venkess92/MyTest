def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = raw_input("Enter choice(1/2/3/4):")

if choice >= '5':
	
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))

#while choice >= '5':
#	print "please enter again 1 to 4 :"
#	choice = raw_input("Enter choice(1/2/3/4):")
	

if choice == '1':
   	print(add(num1,num2))
	
elif choice == '2':
   	print(subtract(num1,num2))
elif choice == '3':
   	print(multiply(num1,num2))
elif choice == '4':
	print "quotient  :",
   	print(divide(num1,num2))
	print "remainder :", 
	print(num1 % num2)

else:
   print("Invalid input")