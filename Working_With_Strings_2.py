phrase = "Giraffe Academy"

print(phrase.upper().isupper())   # combination functions

print(len(phrase))                # length of string

print(phrase[0])                  # Grab a specific character G=0 ; i=1; r=2;.......

print(phrase.index("G"))          # Return back the index of "G "

print(phrase.index("Acad"))       # A = 8(index value)

print(phrase.replace("Giraffe","Elephant"))   # Replace "Giraffe" to "Elephant"
 
print(phrase.index("z"))          # Gives an error bcz z is not the string
