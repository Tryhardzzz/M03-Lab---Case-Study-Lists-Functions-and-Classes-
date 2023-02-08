class Vehicle:
    def __init__(self, vehicleType: 'Vehicle'):
        self.vehicleType = vehicleType
       
class Automobile(Vehicle):
    def __init__(self, year: 'Automobile', make: 'Automobile', model: 'Automobile', doors: 'Automobile', roof: 'Automobile', vehicleType):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        super().__init__(vehicleType)
        
    def __str__(self):
        return f"{self.year}{self.make}{self.model}{self.doors}{self.roof}"
    
car1 = Vehicle('car')
car2 = Automobile(2004, 'toyota', 'camry', 4, 'sun_roof', car1.vehicleType)

car1.vehicleType = input("Enter the vehicle you would like to enter: ")
car2.year = input("Enter the Year of the car: ")
car2.make = input("Enter the Make of the car: ")
car2.model = input("Enter the Model of the car: ")
car2.doors = input("Enter the number of doors of the car: ")
car2.roof = input("Enter the option of if the car has a sunroof or not: ")

print("Vehicle type: " + car1.vehicleType)
print("Year: " + car2.year)
print("Make: " + car2.make)
print("Model: " + car2.model)
print("Number of doors: " + car2.doors)
print("Type of roof: " + car2.roof)
