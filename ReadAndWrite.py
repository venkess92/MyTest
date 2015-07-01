from sys import argv #from system we are importing argument

script, filename = argv # argument passing

print "We're going to erase %r." % filename # getting file name  
print "If you don't want that, hit CTRL-C (^c)." # escape from program
print "If you do want that, hit RETURN." #press enter to continue

raw_input("?") #.....

print "Opening the file..." # printing statement
target = open(filename, 'w') # open the file. W represent write command 

print "Truncating the file. goodbye!" # printing statement
target.truncate() #truncate (erase)

print "Now I'm going to ask your for three lines." 

line1 = raw_input ("line 1: ") # variable 1
line2 = raw_input ("line 2: ") # variable 2
line3 = raw_input ("line 3: ") # variable 3

print "I'm going to write these to the file." 

target.write(line1) # writing to the file first line
target.write("\n")  # new line
target.write(line2) 
target.write("\n")
target.write(line3)
target.write("\n")

print "An finally, we close it."
target.close() # end of program by closing 