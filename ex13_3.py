from sys import argv

script, first, second, third = argv

third = raw_input("I don't like %r, type something else: " % third)
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
