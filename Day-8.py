class Car:
    def __init__(self,brand,model,year,color):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
    def display(self):
        print("----Car Details----")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print("---------------------")

car1=Car("Tesla", "Model S", 2023, "Midnight Silver")
car1.display()
car2=Car("Ford", "Mustang", 2021, "Race Red")
car2.display()

