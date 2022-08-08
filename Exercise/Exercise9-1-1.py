# 创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。
# 创建一个名 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，
# 而后者打印一条消息，指出餐馆正在营业。 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant():

    def __init__(self, restaurant, cuisine):
        self.restaurant = restaurant
        self.cuisine = cuisine

    def open(self):
        print('The ' + self.restaurant.title() + ' is opening!')


YDC = Restaurant('Yu de cuo', 'Fish')

print("This restaurant's name is " + YDC.restaurant.title())
print("And it's cuisine is " + YDC.cuisine.title())
YDC.open()
