class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_desciptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the mileage!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

#1. 创建子类-电动车
class ElectricCar(Car):
#父类必须在当前文件中,且在子类前面
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # super()是一个特殊函数,将父类和子类关联起来,让子类实例包含父类的所有属性
        # 父类也称超类

        #2.为子类定义特殊属性和方法
        self.battery_size = 70
    #2.描述电池
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

#电动车基础属性
my_hate_car = ElectricCar('tesla', 'Model S', 2020)
print(my_hate_car.get_desciptive_name())
#2. 展示电池
my_hate_car.describe_battery()