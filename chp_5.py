fruits = ['apple','orange','banana','pineapple','kiwi','pomegranate','grapes','pears','strawberry','watermelon','lemon','mango','papaya','fig']

def in_list(object,list):
    if object in list:
        print("Yes "+object+ " is in fruits")
    else:
        print("No " + object + " is not in fruits")

in_list('tomatoe',fruits)
in_list('apple',fruits)

#######
#5-10. Checking Usernames:Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a
#new username. If a username has not been used, print a message saying that the username is available.
users = ['Nini','admin','Roro','niki','robo']
other_users = ['Niki','shivam','robo','nikita']


def check_name(new_user,users_lower):
    if new_user.lower() not in users_lower:
        print("Welcome to our website!")
        users.append(new_user)
    else:
        print("Sorry " + new_user +" is already taken.") 

def check_names():
    users_lower = [user.lower() for user in users]
    list(map(lambda x :check_name(x,users_lower),other_users))

check_names()

#########
#5-8. Hello Admin:
def welcome(user):
	if user == 'admin':
		print("Hello admin,would you like to see a status report?")
	else:
		print(f"Hello {user}, thank you for logging in again")

def greeting(user):
	if user_list:
		for i in user_list:
			welcome(i)
	else:
		print("where are users")

user_list = ['Nini','admin','Roro']
greeting(user_list)

##############
#5-11 Ordinals
num = [i for i in range (1,10)]

for i in num:
	if i==1:
		print("1st")
	elif i==2:
		print("2nd")
	elif i==3:
		print("3rd")
	else:
		print(f"{i}th")
