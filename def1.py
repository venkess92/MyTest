def hello():
    print '\nHello!'
 
def area(width, height):
    return width * height
 
def print_welcome(name):
    print 'Welcome,', name
 
name = raw_input('\nYour Name: ')
hello(),
print_welcome(name)
print '\nTo find the area of a rectangle,'
print 'enter the width and height below. \n'

w = input('Width: ')
while w <= 0:
    print 'Must be a positive number'
    w = input('Width: ')
 
h = input('Height: ')
while h <= 0:
    print 'Must be a positive number'
    h = input('Height: ') 
 
print '\n Width =', w, 'Height =', h, 'so Area =', area(w, h)