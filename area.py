def square(length):
    return length * length
 
def rectangle(width , height):
    return width * height
 
def circle(radius):
    return 3.14 * radius ** 2
 
def options():
    print					#this will create blank line 
    print "Options:"
    print "s = calculate the area of a square."
    print "c = calculate the area of a circle."
    print "r = calculate the area of a rectangle."
    print "q = quit"
    print					
 
print "This program will calculate the area of a square, circle or rectangle."
choice = ()
options()
while choice != "q":  #if not equals to "q" it will continue to program other wise it return to elif statement. 
    choice = raw_input("Please enter your choice: ") #we can enter our choice
    if choice == "s":    #length of square
        length = input("Length of square: ")
        print "The area of this square is", square(length)
        options()
    elif choice == "c": # radius of circle
        radius = input("Radius of the circle: ")
        print "The area of the circle is", circle(radius)
        options()
    elif choice == "r":  #W & H of rectangle
        width = input("Width of the rectangle: ")
        height = input("Height of the rectangle: ")
        print "The area of the rectangle is", rectangle(width, height)
        options()
    elif choice == "q": # quit line
         print "", # this make the program to quit
    else:
        print "Unrecognised option."
        options()