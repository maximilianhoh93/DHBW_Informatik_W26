#############################################################################################
# Dateiname:       19_sortwords.py  [3-18 optional]                                         #
# ----------------------------------------------------------------------------------------- #
# Implementierung: https://www.programiz.com/python-programming/examples/alphabetical-order #
# Algorithmus:                                                                              #
# Ein-/Ausgabe:                                                                             #
# Beschreibung:    Alphabetische Sortierung von Wörtern einer Zeichenkette                  #
# Lernziele:       String-Manipulation (lower(), split(), sort())                           #
# Anmerkungen:                                                                              #
#############################################################################################

DEBUG_INFO = False

# change this value for a different result
my_str = "Hello this Is an Example With cased letters"
# uncomment to take input from the user
if not DEBUG_INFO:
   my_input = input("Enter a string: ").lower()
else:
   my_input ="Ich bin ein ganzer Satz!"

# You may want to execute sort function on all lower cased words
my_str_lower = my_str.lower()

if my_str_lower.__contains__(my_input):
   print("ist im string enthalten")
else:
   print("ist NICHT im string enthalten")

#my_str_low = my_str

# breakdown the string into a list of words
words = my_str_lower.split()

words.sort()


if DEBUG_INFO:
   print("Initial unsorted words:") 
   print(my_str)


# sort the list


# display the sorted words

print("Final sorted words:")
print(words)

# Alternative Ausgabe
"""
for word in words:
   print(word, end=', ')
"""