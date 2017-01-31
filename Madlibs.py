import X

sentence = ("In the shadowy world of spies, a/an ADJ1 organization like the US Government uses"
            " spies to infiltrate ADJ2 groups for the purpose of obtaining top secret PLNOUN1."
            " A teacher, CELEB, or even the little old NOUN with a cane and 15 pet PLNOUN2 could"
            " be a spy.")
            #space at the beginning of these lines
            
adj1 = X.userString("Enter an adjective:")
adj2 = X.userString("Enter another adjective:")
plnoun1 = X.userString("Enter a plural noun:")
plnoun2 = X.userString("Enter another plural noun:")
celeb = X.userString("Enter a celebrity:")
noun = X.userString("Enter a noun:")

print

sentence = sentence.replace("ADJ1", adj1)
sentence = sentence.replace("ADJ2", adj2)
sentence = sentence.replace("PLNOUN1", plnoun1)
sentence = sentence.replace("PLNOUN2", plnoun2)
sentence = sentence.replace("CELEB", celeb)
sentence = sentence.replace("NOUN", noun)

print sentence