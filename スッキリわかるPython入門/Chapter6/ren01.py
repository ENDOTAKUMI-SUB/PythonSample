class Car:
    weight = 4000
    num_wheels = 4

    def calc_weight_per_wheel(self):
        return self.weight / self.num_wheels
    
my_car = Car()

print(type(my_car))
print(my_car.weight)
print(my_car.num_wheels)
print(my_car.calc_weight_per_wheel())