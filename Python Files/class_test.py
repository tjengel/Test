class Team(object):
    def __init__(self, city, mascot):
        self.city = city
        self.mascot = mascot

    def team(self):
        combined = self.city + ' ' + self.mascot
        return combined

packers = Team("Green Bay", "Packers")
print packers.team()

input1 = raw_input("Enter city.\n")
input2 = raw_input("Enter mascot.\n")
team = Team(input1, input2)
print team.team()
