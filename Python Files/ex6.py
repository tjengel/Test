x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# String in a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# String in a string
print "I said: %r." % x
# String in a string
print "I also said: '%s'." % y

hilarious = False
# String in a string
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

print w + e
