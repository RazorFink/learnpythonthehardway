name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
in_cm = 2.540
lb_kg = 0.454 

print "Let's talk about %s" % name
print "He's %d inches or %f centimeters tall." % (height, height * in_cm)
print "He's %d pounds or %f kilograms heavy." % (weight, weight * lb_kg)
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)
