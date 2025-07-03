# initiate a Class
class employee:
    # special method/magic method/ dunder method -constructor
    def __init__(self):
        print("started executing attributes/data")  
        self.id = 122
        self.salary = 50000
        self.designation = "CTO"

    def travel(self, destination):
        print("this travel method was called manually")
        print(f"Employee is now travelling to {destination}")


# create an object 
Fahad = employee()

#print(Fahad.salary)
#Fahad.travel("hyderabad")

print(type(Fahad))



