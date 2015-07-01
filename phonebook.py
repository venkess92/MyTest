#phone book


contacts = ['appa:9677568419', '\namma:9443266560', 
'\npramesh:9629145623', '\naravinth:9677568419']
 
print "enter choice 0 to 3"
print "Type 'All' to view all contact"
print "Type names to view all names"

def option():
	print "enter choice 0 to 3"
	print "Type 'All' to view all contact"
	
	

	
contact = raw_input() 

if contact == '0':
	print contacts [0]
	
elif contact == '1':
	print contacts [1]
	
elif contact == '2':	
	print contacts [2]
	
elif contact == '3':
	print contacts [3]
	
elif contact == 'all':
 	print contacts [0] 
	print contacts [1]
	print contacts [2]
	print contacts [3]

elif contact == 'names':
	print contacts [9677568419]

else :
	print "enter correct number" 
	#option()
