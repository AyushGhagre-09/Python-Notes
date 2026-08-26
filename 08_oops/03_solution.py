# polymorphism

class Car:
    total_car=0 # class  level varaible
    def __init__(self,brand,model):
        self._brand=brand
        self.__model=model
        Car.total_car+=1

    def display_car_name(self):
        print(f"Car Name : {self._brand},{self.__model}")

    def fuel_type(self):
        return "Petrol or Diesel"

    # static method
    @staticmethod
    def general_description():
         return "Cars are means of transport"

    
    
class ElectricCar(Car):
     def __init__(self,brand,model,battery_size):
         super().__init__(brand,model)
         self.battery_size=battery_size

     def fuel_type(self):
             return "Electric Charge"

# my_tesla=ElectricCar("Tesla","model S","85kwh")
# print(my_tesla.fuel_type())
# safari=Car("Tata","Safari")
# print(safari.fuel_type())

test=Car("test","test")
print(test.__dict__)

# print(Car.total_car)
# print(test.total_car)
# print(test.general_description())

#for static method  in defination we can't pass self and with instance
# if we call that method it will give error
print(Car.general_description())

# @staticmethod-> any thing start with @  is called as decorator






