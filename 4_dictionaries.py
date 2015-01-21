# http://nssdc.gsfc.nasa.gov/planetary/factsheet/planet_table_ratio.html

mercury = { 'name': 'Mercury', 'mass': 0.6, 'distance': 0.4, 'moons': 0 }
venus = { 'name': 'Venus', 'mass': 0.8, 'distance': 0.7, 'moons': 0 }
earth = {  'name': 'Earth', 'mass': 1, 'distance': 1, 'moons': 1 }
mars = { 'name': 'Mars', 'mass': 0.1, 'distance': 1.5, 'moons': 2 }
jupiter = { 'name': 'Jupiter', 'mass': 317.8, 'distance': 5.2, 'moons': 67 }
saturn = { 'name': 'Saturn', 'mass': 95.2, 'distance': 9.6, 'moons': 62 }
uranus = { 'name': 'Uranus', 'mass': 14.5, 'distance': 19.2, 'moons': 27 }
neptune = { 'name': 'Neptune', 'mass': 17.1, 'distance': 30.1, 'moons': 14 }

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Write code that will answer the following questions:
# ----------------------------------------------------

# How many planets are there?
print(len(planets))


# How many moons revolve around Jupiter?
print(jupiter['moons'])

# How many moons are there in our solar system?
number_of_moons = 0
for planet in planets:
  number_of_moons = number_of_moons + planet['moons']
print("There are", number_of_moons, "in our solar system.")

# display all of the planet names

# display planet names in alphabetical order

