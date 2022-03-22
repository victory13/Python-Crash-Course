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
