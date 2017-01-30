import X
    
kmWeekday = X.userInt("How many km did you travel on the weekdays?")
kmWeekend = X.userInt("How many km did you teavel on the weekend?")
miWeekday = X.kmToMi(kmWeekday)
miWeekend = X.kmToMi(kmWeekend)

dollarsWeekday = miWeekday * 0.13
dollarsWeekend = miWeekend * 0.24

print "Weekday $%.2f" % dollarsWeekday
print "Weekend $%.2f" % dollarsWeekend 
print "Total $%.2f" % (dollarsWeekday + dollarsWeekend)