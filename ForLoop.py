import X

word = X.userString("Please enter a word:")

for letter in word:
    letter = letter + " "
    print letter,
    
print "\nAll done!"


words = ['cat', 'dog', 'apple']
lengths = []

for word in words:
    l=len(word)
    lengths.append(l)
    
print '\nThese are the lenghts %s' % lengths