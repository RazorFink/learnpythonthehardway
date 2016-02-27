# assign formatted string to x 
x = "There are %d types of people." % 10
# assign simple string to binary
binary = "binary"
# assign simple string to do_not
do_not = "don't"
# assign formatted string with 2 arguments to y
y = "Those who know %s and those who %s." % (binary, do_not)

# print x
print x
# print y
print y

# print formatted string including formatted string as literal
print "I said: %r." % x
# print formatted string included formatted string as string
print "I also said:  '%s'." % y

# assign boolean False to hilarious
hilarious = False
# assign string with format token, but no arguments to joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# print formatted string incuding boolean argument
print joke_evaluation % hilarious

# assign simple string to w
w = "This is the left side of..."
# assign simple string to e
e = "a string with a right side."

# print concatenation of w and e
print w + e
