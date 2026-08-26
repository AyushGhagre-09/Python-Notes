#mutiple inheritence
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


class Battery:
     def battery_info(self):
         return "this is battery"


class Engine:
    def engine_info(self):
        return "this is engine"


class ElectricCar(Battery,Engine,Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
                 return "Electric Charge"


tesla=ElectricCar("Tesla","Model S")

print(tesla.engine_info())
print(tesla.battery_info())
print(tesla.fuel_type())

