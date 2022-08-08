
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 此处可以增加默认值,且,类中的每个属性都必须有初始值,哪怕是0或者空字符串
        # 当设置默认值时,在方法__init__中,则无需包含为它提供初始值的形参,因此在def后的括号中没有odometer_reading
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print ("This car has" + str(self.odometer_reading)+ " miles on it.")

    # 2再次定义一个函数,为odometer_reading提供一个接受值的方法
    def update_odometer(self,mileage):
        # 3增加条件:禁止调表
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print ("Odometer can not roll back!")
    
    # 4递增增量历程
    def increase_odometer(self,mile):
        self.odometer_reading += mile

class ElectricCar(Car):
    # 继承父类
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # super是特殊函数,帮助python将父类和子类关联,这里是调用ElectricCar的父类方法__init__
        # 这里是包含了所有属性
        # 父类也叫超类,因此名为super
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
print (my_tesla.get_descriptive_name())