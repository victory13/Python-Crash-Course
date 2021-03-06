favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print("I really love " + pizza + " pizza!")

print("\nI really love pizza!")



#4.5 Summing a Million
numbers = list(range(1, 1000001))

min(numbers)
max(numbers)
sum(numbers)



#4.7 Threes
#Make a list of the multiples of 3 from 3 to 0. Use a for loop to print the numbers in your list.
for i in range(3,31,3):
    print(i)
    
    
#4-8: Cubes
cubes = []
for number in range(1, 11):
    cubes.append(number**3)

for cube in cubes:
    print(cube)
    
#4-9: Cube Comprehension
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)
  
#4-10: Slices
players = ['charles', 'martina', 'michael', 'florence', 'eli','nina','roby']
print("First three items are ",players[:3])
print("Middle three items are",players(1:4))
print("Last three items are" ,players[-3:])

#4-11: Pizza
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)
