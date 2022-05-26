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


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " +str(self.battery_size) + ' Kwh battery.')


    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go nearly " + str(range) + ' miles on a full charge.'
        print(message)
        self.upgrade_battery()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def describe_battery(self):
        self.battery_size.battery_size()

    def get_range(self):
        self.battery_size.get_range()

my_geele = ElectricCar('Geele', 'Boyue', '2018')
my_geele.get_range()
my_geele.get_range()
