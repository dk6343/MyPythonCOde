#David Kelly
#1/20/17
#Recipe Converter

print "--Original Recipe--"
print "Enter Original ammount in cups/teaspoons of:"
print "Flour:",
flour = raw_input()
print "Water:",
water = raw_input()
print "Salt:",
salt = raw_input()
print "Yeast:",
yeast = raw_input()
print "Enter loaf adjustment factor (e.g. 2.0 for double the size):",
factor = raw_input()

print "--Modified Recipe--"

# Hi David, notice that I added () around your calculation
print "Flour %.2f cups." % (float(flour)*float(factor))
print "Water %.2f cups." % (float(water)*float(factor))
print "Salt %.2f teaspoons." % (float(salt)*float(factor))
print "Yeast %.2f teaspoons" % (float(yeast)*float(factor))

print "--Modified Recipe in grams--"

print "Flour %.2f g." % (float(flour)*float(factor)*125.0)
print "Water %.2f g." % (float(water)*float(factor)*236.0)
print "Salt %.2f g." % (float(salt)*float(factor)*7.0)
print "Yeast %.2f g." % (float(yeast)*float(factor)*3.0)