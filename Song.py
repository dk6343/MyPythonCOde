#David Kelly
#1/29/17
#Song Creator
#I understand that this is isn't exactly what it should be, but I'm a bit confused with
# ForLoops and I'd like to meet with you at some point so we could go over it.
import X

song = ("VER1" "\nCHORUS" "\nVER2" "\nCHORUS" "\nVER3" "\nCHORUS" "\nVER4" "\nCHORUS" "CHORUS")
song2 = ("-- one more time" "VER1" "\nCHORUS" "\nVER2" "\nCHORUS" "\nVER3" "\nCHORUS" "\nVER4" "\nCHORUS" "CHORUS")
ver1 = X.userString("Enter the first verse:")
ver2 = X.userString("Enter the second verse:")
ver3 = X.userString("Enter the third verse:")
ver4 = X.userString("Enter the fourth verse:")
chorus = X.userString("Enter the chorus:")
print "Enter chorus repeat factor:",
factor = raw_input()

print
song = song.replace("VER1", ver1)
song = song.replace("VER2", ver2)
song = song.replace("VER3", ver3)
song = song.replace("VER4", ver4)
song = song.replace("CHORUS", chorus * int(factor))
song = song.replace("CHORUS2", chorus * int(factor))
song2 = song.replace("VER1", ver1)
song2 = song.replace("VER2", ver2)
song2 = song.replace("VER3", ver3)
song2 = song.replace("VER4", ver4)
song2 = song.replace("CHORUS", chorus * int(factor))
song2 = song.replace("CHORUS2", chorus * int(factor))
print song
print song2