class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        print("----Car Details----")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print("---------------------")


# Subclass
class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_capacity):
        super().__init__(brand, model, year, color)  # Call parent constructor
        self.battery_capacity = battery_capacity

    def display(self):
        super().display()  # Call parent display()
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        print("---------------------")


# Creating instances
car1 = Car("Tesla", "Model S", 2023, "Midnight Silver")
car1.display()

ecar1 = ElectricCar("Tesla", "Model 3", 2022, "Pearl White", 75)
ecar1.display()






