#encapsulation
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model

    
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    

my_car=Car("Toyata","Corolla")
# print(my_car.__brand)
print(my_car.get_brand())
print(my_car.get_model())