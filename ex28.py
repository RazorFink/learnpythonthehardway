""" Boolean practice """
print "1  True:  ", True and True
print "2  False: ", False and True
print "3  False: ", 1 == 1 and 2 == 1
print "4  True:  ", "test" == "test"
print "5  True:  ", 1 == 1 or 2 != 1
print "6  True:  ", True and 1 == 1
print "7  False: ", False and 0 != 0
print "8  True:  ", True or 1 == 1
print "9  False: ", "test" == "testing"
print "10 False: ", 1 != 0 and 2 == 1
print "11 True:  ", "test" != "testing"
print "12 False: ", "test" == 1
print "13 True:  ", not (True and False)
print "14 False: ", not (1 == 1 and 0 != 1)
print "15 False: ", not (10 == 1 or 1000 == 1000)
print "16 False: ", not (1 != 10 or 3 == 4)
print "17 True:  ", not ("testing" == "testing" and "Zed" == "Cool Guy")
print "18 True:  ", 1 == 1 and (not ("testing" == 1 or 1 == 0))
print "19 False: ", "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
print "20 False: ", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

