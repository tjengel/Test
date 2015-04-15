from sys import exit

def el_cortez():
    print "You have finally reached El Cortez. Blackjack?"
    blackjack = raw_input("> ")

    if blackjack == "Yes" or blackjack == "yes":
        print "Excellent. Let's play."
    else:
        end("Um...Ok...")

    print "You win big and spend all those winnings on a lovely chicken fried steak."
    end("I think that's a day.")

def pool():
    print "Would you like to sit in the pool or hot tub?"
    water = raw_input("> ")

    if water == "hot tub" or water == "Hot tub":
        print "I'm always down with the hot tub."
        print "Should we get a drink?"
        print "Are we in the hot tub? Of course we will"
    else:
        print "It\'s getting late anyway."
        breakfast()

    show()

def breakfast():
    print "Now that it\'s 11:30, let\'s go to breakfast."
    print "Where should we go?"
    answer = raw_input("> ")
    answer_list = ["Denny's", "dennys", "denny's"]

    if answer == "Buffet" or answer == "buffet":
        print "Great, let's do it!"
        buffet()
    elif answer in answer_list:
        print "That's acceptable."
    else:
        end("No food for us!")

def buffet():
    print "Oh my god, there's so much food."
    print "What should we do next?"
    post_buffet = raw_input("> ")

    if post_buffet == "Nap" or post_buffet == "nap":
        end("Excellent choice.")

def show():
    print "Let's go to a show. You have any preferences?"

    show_choice = raw_input("> ")

    if show_choice == ("Cirque du Soleil" or "Cirque du soleil"):
        print "I agree."
    elif show_choice == "I don't care.":
        print "Fine. I'm picking then."
    else:
        end("You went to a cheap show. Sucked. Now you\'re bummed.")

def end(how):
    print how, "You've finally made it to bed."
    exit(0)

def start():
    print "We've finally made it to Vegas. There will be lots to do."
    print "Where should we start? We have the pool or blackjack."

    choice = raw_input("> ")
    choice_list = ["Pool", "pool"]
    blackjack_list = ["Blackjack", "blackjack"]

    if choice in choice_list:
        pool()
    elif choice in blackjack_list:
        el_cortez()
    else:
        print "Try again."
        choice = raw_input("> ")


start()
