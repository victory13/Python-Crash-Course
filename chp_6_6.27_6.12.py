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


#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places
#for each person.
favorite_places = {
	"nini":["mumbai","goa","pondi"],
	"niki":["japan","tokyo"],
	"taylor":["new_york","nashville"]
}



for name,place in favorite_places.items():
	print(f"\n{name.title()}'s favourite place are as follows :")
	for p in place:
		print("- " + p.title())	
		
#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'mumbai': {
        'country': 'india',
        'population': 450035678,
        'nearby mountains': 'sahyadri range',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himalaya',
        }
    }

for city,city_info in cities.items():
	country = city_info['country'].title()
	population = city_info['population']
	mountains = city_info['nearby mountains'].title()

	print(f"\n {city.title()} is in {country}. ")
	print("  It has a population of about " + str(population) + ".")
	print("  The " + mountains + " mountains are nearby.")
