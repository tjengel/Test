print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"

print "Let's play a game. Pick a number between 1 and 10."

number = raw_input("> ")

if number == "7":
    print "You win a car!"

else:
    print "You chose...poorly."

print "How about blackjack? Tell me to hit or stand. Dealer shows 2, you have 12."

input = raw_input("> ")

if input == "Hit" or input == "hit":
    print "That is cowwect."
    print "How much do you bet on next hand?"

    bet = raw_input("> ")

    if bet >= "10":
        print "Nice bet!"
    else:
        print "Why so shy?"

elif input == "Stand" or input == "stand":
    print "That's less than optimal."
    print "Dealer hits, gets a 7, and now has 19. You lose."

else:
    print "That was not the best play."
