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

# 将电池属性抽离出来,作为单独类
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
#子类
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        # 在此创建实例,并存储在self.battery中;因此每一个EkectricCar实例都包含一个自动创建的Battery实例

my_tesla = ElectricCar('tesla', 'Model S', 2020)
my_tesla.battery.describe_battery()
#一个猜想:my_tesla是self的实例,battery是ElectricCar的属性,指向Battery类,然后在Battery类中调用describe_battery方法
