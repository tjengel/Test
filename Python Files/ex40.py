class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally round tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

class new_song(object):

    def __init__(me, sings):
        me.sings = sings

    def i_will_sing(me):
        for line in me.sings:
            print line

print '-' * 10

lost_that_loving_feeling = new_song(["You've lost that loving feeling",
                                    "Oh that loving feeling"])

lost_that_loving_feeling.i_will_sing()

class count(object):

    def __init__(number, count):
        number.count = count

    def count_me(number):
        for i in number.count:
            i += 1
            print i

range = count([0,1,2,3])

range.count_me()
