# Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. C

class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 5

    def describe_restaurant(self):
        print(f"restaurant name {self.name.title()} and cuisine {self.cuisine.title()}")
        print(f"number of people served {self.number_served}")

    def open_restaurant(self):
        print("Resto is open")

    def set_number_served(self,number_served):
        if number_served > self.number_served:
            self.number_served = number_served
        else:
            print("cannot roll back")
        print(f"new number of people served {number_served}")

    def increment_number_served(self,increase_num):
        self.number_served+= increase_num




resto = Restaurant("nini's resto","mutli-cuisine")
# resto.describe_restaurant()
# resto.open_restaurant()
resto.number_served = 10
resto.describe_restaurant()

resto.set_number_served(15)
resto.increment_number_served(5)
resto.describe_restaurant()
