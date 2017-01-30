import X

flavors = ['Chocolate', 'Vanilla', 'Strawberry']
ratings = []
for flavor in flavors:
    rating = X.userString('Rate %s from 1 to 5:' % flavor)
    ratings.append("%s rated as a %s" % (flavor, rating)) 
    #ratings = ratings + ["%s rated as a %s" % (flavor, rating)]
print ratings