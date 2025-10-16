class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand}'s speed accelerates with {amount}, current speed is {self.speed}")
    
    def describe(self):
        print(f"current speed is {self.speed}")

car1 = Car("alpha", "red")

car1.describe()
car1.accelerate(30)
car1.accelerate(40)