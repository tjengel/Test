ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there are not 10 things in that list. Let's fix that."
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    # pop takes the last item in the list
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # fancy
print stuff.pop()
# join command separates each element with whatever
# precedes the .join command
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
print ' cat '.join(stuff)
