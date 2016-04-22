# import argv from sys module
from sys import argv

# unpack argv into variables
script, filename = argv

# open filename into file object txt
txt = open(filename)

# print filename argument and contents of file
print "Here's your file %r:" % filename
print txt.read()

# prompt for filename
print "Type the filename again:"
file_again = raw_input("> ")

# assign file contents to txt_again
txt_again = open(file_again)

# print contents of file_again
print txt_again.read()
