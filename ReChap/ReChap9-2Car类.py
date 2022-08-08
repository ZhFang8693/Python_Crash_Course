class Car:
    #1.定义车辆的基本属性
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #2.为属性指定默认值
        self.odometer_reading = 0

    def get_desciptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    #2.读取行驶里程
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    #4. 创建方法更新里程
    def update_odometer(self, mileage):
        #5. 阻止调表
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the mileage!")

    #5. 将里程增加特定量
    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_fav_car = Car('Shenshou', 'Zhizun',2021)
print(my_fav_car.get_desciptive_name())
#3. 调整初始里程
my_fav_car.odometer_reading = 170
#2.展示行驶里程
my_fav_car.read_odometer()

#4. 更新里程
my_fav_car.update_odometer(23)
my_fav_car.read_odometer()

#5. 增加特定里程
my_fav_car.increment_odometer(77)
my_fav_car.read_odometer()