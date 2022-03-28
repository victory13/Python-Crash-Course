# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

msg = input("What kind of rental car would you like ? ")
print(f"Let me see if I can find you a {msg.title()}")

# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

qs = input("How many people? ")

if int(qs) > 8:
    print("You need to wait for a table")
else:
    print("Your table is ready")
    

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the   number is a multiple of 10 or not.
number = "Lets see the number you enter is multiple of 10 or not "
number += "\n Please enter your number "
number = input(number)
if int(number) % 10 == 0:
    print(f"Yes! {number} you got a multiple of 10")
else:
    print(f"No ! {number} its not a multiple of 10")

 #7-4: Pizza Toppings
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value. As they enter each topping,print a message saying you’ll 
# add that topping to their pizza.

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

#  7-5. Movie Tickets:
# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, 
# the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
        
# 7.8 Deli
#As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made
sandwich_orders =['tuna sandwich', 'cheese toast sandwich','egg sandwich']
order_completed = []

while sandwich_orders:
    r = sandwich_orders.pop()
    order_completed.append(r)
    print(f" I made your {r}")
print("\n")
for item in  order_completed:
    print(f"{item} is completed")
    
 #7.9 No Pastrami:
sandwich_orders =['tuna sandwich','pastrami', 'cheese toast sandwich','egg sandwich','pastrami']
order_completed = []

print("Sorry we ran out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#7-10. Dream Vacation: Write a program that polls users about their dream vacation.
#Write a prompt similar to If you could visit one place in the world, where would you go?   
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place
    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(name.titl
    
while sandwich_orders:
    r = sandwich_orders.pop()
    order_completed.append(r)
    print(f" I made your {r}")
print("\n")
for item in  order_completed:
    print(f"{item} is completed")
