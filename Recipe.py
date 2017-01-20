#David Kelly
#1/20/17
#Recipe Converter

print "--Original Recipe--"
print "Enter Original ammount in cups/teaspoons of:"
print "Flour:",
flour = raw_input()
print "Water:",
water = raw_input()
print "Salt",
salt = raw_input()
print "Yeast",
yeast = raw_input()

print "--Modified Recipe--"
print "Flour %.2f cups" % int(flour)*float(2.0)