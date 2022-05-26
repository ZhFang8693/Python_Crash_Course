class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print ("This car has" + str(self.odometer_reading)+ " miles on it.")

    
    def update_odometer(self,mileage):
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print ("Odometer can not roll back!")
    
    
    def increase_odometer(self,mile):
        self.odometer_reading += mile


# 将电池属性抽离出来,作为一个单独的类
class Battery():
    # 定义电池容量
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    
    # 
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + ' Kwh battery.')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 在此继承Battery的属性,注意这里是个类
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
# 首先定义属性是my_tesla,然后指定继承的是battery(battery指向的是Battery(),见line43)
# 然后调用Battery()类中的describe_battery()
my_tesla.battery.describe_battery()