class Car:
    """ This class makes a car. """
    def __init__ (self, brand, color, age):
        self.brand = brand
        self.color = color
        self.age = age

    def __str__ (self):
        returned_string = self.brand + ' ' + self.color + ' ' + str(self.age)

    def get_brand (self):
        return self.brand

    def get_color (self):
        return self.color

    def get_age (self):
        return self.age

    def order_car_brand(car1, car2, car3):
        cars = [car1.brand, car2.brand, car3.brand]
        cars_1 = []
        cars_2 = [car1, car2, car3]
        cars.sort()
        for item in cars_2:
            if cars[0] == item.brand:
                cars_1.append(item)
        for item in cars_2:
            if cars[1] == item.brand:
                cars_1.append(item)
        for item in cars_2:
            if cars[2] == item.brand:
                cars_1.append(item)
        
        return cars_1

    def get_oldest_car(car1, car2, car3):
        x = car1.age
        y = car2.age
        z = car3.age
        
        x_1 = [car1.age, car1.color]
        y_1 = [car2.age, car2.color]
        z_1 = [car3.age, car3.color]
        
        if x > y:
            if x > z:
                return x_1
            else:
                return z_1
        else:
             if y > z:
                return y_1
             else:
                return z_1

    def birthday_car (self):
        self.age = self.age + 1
        return self.age
        
mom_car = Car("toyota", "white", 4)
my_car = Car("ferari", "blue", 10)
dad_car = Car("bmw", "red", 2)

        
print(Car.get_oldest_car(mom_car, dad_car, my_car))
print(Car.order_car_brand(mom_car, dad_car, my_car))
print(Car.birthday_car(my_car))
