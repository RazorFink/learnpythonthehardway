tabby_cat = "\tI'm tabbed in."
persion_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
quote_escape = "A so-called \"quote escape\""
apos_escape = 'A so-called \'apos escape\''
sq = "\'"
dq = "\""
quotestring1 = "%sin quotes%s" % (sq, sq)
quotestring2 = "%sin quotes%s" % (dq, dq)
quotestring3 = "%rin quotes%r" % (sq, sq)
quotestring4 = "%rin quotes%r" % (dq, dq)

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass\r\t* Toys\v* Other Stuff\v* Mo Other Stuff\n\t* cheese
\f* FormFeed
\f* FormFeed
\f* FormFeed
"""

print tabby_cat
print persion_cat
print backslash_cat
print fat_cat
print "%s" % quote_escape
print "%r" % quote_escape
print "%s" % apos_escape
print "%r" % apos_escape
print quotestring1
print quotestring2
print quotestring3
print quotestring4
