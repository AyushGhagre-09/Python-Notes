#decorator
class Car:
    total_car=0 # class  level varaible
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1

    def display_car_name(self):
        print(f"Car Name : {self.__brand},{self.__model}")

    def fuel_type(self):
        return "Petrol or Diesel"

    # static method
    @staticmethod
    def general_description():
         return "Cars are means of transport"

    @property
    def brand(self):
         return self.__brand
         

    
    
class ElectricCar(Car):
     def __init__(self,brand,model,battery_size):
         super().__init__(brand,model)
         self.battery_size=battery_size

     def fuel_type(self):
         return "Electric Charge"



safari=Car("Tata","Safari")
print(safari.__dict__)
# print(safari.__brand)
safari.__brand="BMW"
print(safari.__dict__)
print(safari.__brand)

#  not recommended way we can access private varaible
print(safari._Car__brand)  

print(safari.brand)









