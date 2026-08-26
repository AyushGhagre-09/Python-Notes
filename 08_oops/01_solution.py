# class and object
class Car:
    # __init__ is constructor and self refer to calling object
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display_car_name(self):
        print(f"Car Name : {self.brand},{self.model}")
#inheritance
class ElectricCar(Car):
     def __init__(self,brand,model,battery_size):
         super().__init__(brand,model)
         self.battery_size=battery_size

my_car=Car("Toyota","Corolla") 
print(my_car.brand)
print(my_car.model)


my_tesla=ElectricCar("Tesla","Model S","85kwh")
print(my_tesla.brand,my_tesla.model,my_tesla.battery_size)
my_tesla.display_car_name()


