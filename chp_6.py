#6-5. Rivers:
river = {'nile':'egypt','ganga':'india','amazon':'us'}


for i,j in river.items():
	print(f"The {i.title()} runs through {j.title()}")
  
#o/p
The Nile runs through Egypt
The Ganga runs through India
The Amazon runs through Us

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
    
#6-6.Polling - Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
#Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding.
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'ari': 'java',
'nini': 'spark'
}

need_to_list = ['phil', 'sarah','nini','roro']
#If they have not yet taken the poll, print a message inviting them to take the poll.
for i in need_to_list:
	if i in favorite_languages:
		print(f"Thank you {i.title()} for responding")
	else:
		print(f"Please {i.title()} take the poll")
    
#o/p
Thank you Phil for responding
Thank you Sarah for responding
Thank you Nini for responding
Please Roro take the poll

