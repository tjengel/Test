from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
# This is the function that rewinds to byte 0 in file.
def rewind(f):
    f.seek(0)
# use "," after f.readline() to print lines without space
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."
# rewinds the script. I was confused as to why when I read lines
# it all of a sudden would only show blank. This explains it.
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
