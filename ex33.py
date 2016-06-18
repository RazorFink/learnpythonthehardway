def print_int(maxint):
    i = 0
    numbers = []
    while i < maxint:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

print "The numbers: "

for num in print_int(6):
    print num
