name = 'Zed A. Shaw'
age = 35 
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "let's talk about %s." % name
print "He's %d inches tall." % height
print "he's %d pounds heavy." % weight
print "Actually that's not too heavy." 
print "He's got %s eyes and %s hair."%(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)