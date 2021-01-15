class Car:
    weight = 4000
    num_wheels = 4

    def __init__(self, car_name='NoName'):
        self.name = car_name

    def calc_weight_per_wheel(self):
        return self.weight / self.num_wheels
    
my_car = Car()
print(my_car.calc_weight_per_wheel())

default_car = Car()
print(default_car.name)


my_car = Car('DeLorean')
print(my_car.name)