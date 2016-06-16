# function to output snack information
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# call function using literal values
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# call function using variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# call function with result of calculations using literals
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# call function with result of calculations with variables and literals
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def cube(a):
    a = int(a) if a else 0
    a_cubed = a * a * a
    print "Cube of %d: %d" % (a, a_cubed)
    return a_cubed

cube(10)
cube(10+3)
cube(cube(2))
number = 6
cube(number)
cube(cube(cube(number)))
print "Enter a number"
number = raw_input()
cube(number)
print "Enter another number"
number = cube(raw_input())
cube(number)
