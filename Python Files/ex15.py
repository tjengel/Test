from sys import argv

script, filename = argv

# Opens the file you want opened and calls it txt
txt = open(filename)

print "Here's your file %r:" % filename
# Prints the read command of the text. .read after txt is command
print txt.read()

# Asking for input to display text again
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
