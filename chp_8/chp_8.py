# Write a function that accepts a list of items a person wants on a sandwich.

def sandwich(*args):
    for i in args:
        print(i)

sandwich('chicken sandwich')
sandwich('paneer','turkey sandwich','cheese')

#8.13 User Profile: Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(), using your first and last names 
# and three other key-value pairs that describe you.

def build_profile(fname,lname,**user_info):
    user_info['first_name']= fname
    user_info['last_name'] = lname

    return user_info

user=build_profile('nini','malg',gender='female',location='mumbai')

print(user)
