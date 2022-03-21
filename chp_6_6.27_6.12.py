#6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person

people=[]

person = {
  'first_name': 'alan',
  'last_name': 'brown',
  'age' : 34,
  'city' : 'london'  
}

people.append(person)

person = {
  'first_name': 'elon',
  'last_name': 'musk',
  'age' : 45,
  'city' : 'new york'  
}

people.append(person)

person = {
  'first_name': 'trisha',
  'last_name': 'miller',
  'age' : 26,
  'city' : 'new york'  
}

people.append(person)

# Display all of the information in the dictionary.
for p in people:
	name = p['first_name'].title() + " " +p['last_name'].title()
	age = str(p['age'])
	city = p['city'].title()

	print(name + ", of " + city+ " ,is " +age+ " years old" )
  
  
#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
#Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
pets = []

pet = {
  'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs'
}

pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)
# Display information about each pet.

for p in pets:
  print(f"\n Here's what I know about {p['name'].title()} :")
  for key,value in p.items():
    print(f" {key} : {str(value)}")
