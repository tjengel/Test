num = 0
print "Enter an integer between 1-100"
count = int(raw_input("> "))

while (count < 1 or count > 100):
    print "Re-type a number in the 1-100 range"
    count = int(raw_input("> "))
else:
    while num < 51:
        num += count
        print "This is your number: ", num
