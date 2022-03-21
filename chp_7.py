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
