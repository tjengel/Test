import hashmap
import pprint

pp = pprint.PrettyPrinter(indent=4)

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

pp.pprint(hashmap.list(states))

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

pp.pprint(hashmap.list(cities))

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print '-' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas."

# default values using //= with the nil result
# can you do this on one line?

city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

german_states = hashmap.new()
hashmap.set(german_states, 'Bayern', 'BY')
hashmap.set(german_states, 'Nordrhein Westfalen', 'NRW')
hashmap.set(german_states, 'Saarland', 'SL')
hashmap.set(german_states, 'Berlin', 'BL')
hashmap.set(german_states, 'Brandenberg', 'BB')
hashmap.set(german_states, 'Hamburg', 'HB')
hashmap.set(german_states, 'Bremen', 'BM')
hashmap.set(german_states, 'Sachsen', 'SCH')

print '-' * 10

hashmap.list(german_states)
