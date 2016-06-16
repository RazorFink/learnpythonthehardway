#import argv list containing command line arguments
from sys import argv

#unpack command line arguments into separate variables
script, input_file = argv

#print contents of file f
def print_all(f):
    print f.read()

#move to start of file f
def rewind(f):
    f.seek(0)

#print value of line_count and current line of f
def print_a_line(line_count, f):
    print line_count, f.readline()

#open input_file, set file object to current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

#call print_all function, printing contents of current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#call rewind function, setting current_file position to start
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
