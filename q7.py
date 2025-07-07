class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


# Create the Car object
my_car = Car(make="Toyota", model="Corolla", year=2020)

# Invoke describe_car()
my_car.describe_car()
# Expected output:
# 2020 Toyota Corolla
