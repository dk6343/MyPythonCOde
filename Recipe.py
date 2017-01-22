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
print "Flour %.2f cups." % (int(flour)*int(factor))
print "Water %.2f cups." % (int (water)*int(factor))
print "Salt %.2f teaspoons." % (int(salt)*int(factor))
print "Yeast %.2f teaspoons" % (int(yeast)*int(factor))

print "--Modified Recipe in grams--"

print "Flour %.2f g." % (int(flour)*int(factor)*125.0)
print "Water %.2f g." % (int(water)*int(factor)*236.0)
print "Salt %.2f g." % (int(salt)*int(factor)*7.0)
print "Yeast %.2f g." % (int(yeast)*int(factor)*3.0)