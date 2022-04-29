# 针对数据的共性,我们可以创造类来表达
# 比如绝大多数狗狗,都有名字,年龄.而且基本都会坐下和握手,那么,对于狗狗来说,它们
# 的共性就是信息(名字和年龄),动作(坐下,握手).
# 因此我们可以创建以下类:
# Python中,默认首字母大写的名称是指类!
class Dog():

    # 初始化狗狗的信息元素,名字和年龄
    def __init__(self, name, age):
        # 类中的函数称之为方法,前面学到的所有函数都适用于方法

        # init_是一种特殊的方法,前后各有一个下划线表示这是一个python的默认方法.
        # init_作用是:每当根据Dog创建一个TODO:实例时,Python都会自动运行它.

        # self是必需的形参,且必须位于其他形参之前;
        # Python调用这个__init__() 方法来创建Dog实例时，将自动传入实参self 。每个与
        # 类相关联的方法调用都自动传递实参self ，它是一个指向实例本身的引用，让实例能够
        # 访问类中的属性和方法。我们创建Dog实例时，Python将调用Dog 类的方法__init__() 。
        # 我们将通过实参向Dog() 传递名字和年龄；self 会自动传递，因此我们不需要传递它。
        # 每当我们根据Dog 类创建实例时，都只需给最后两个形参（name 和age ）提供值。

        # self.name = name 获取存储在形 参name 中的值，并将其存储到变量name 中，然
        # 后该变量被关联到当前创建的实例。
        self.name = name
        self.age = age
    # 这里的动作,并不需要其他参数,因此只需要一个self形参

    def sit(self):
        print(self.name.title() + 'is now sitting.')

    def handshake(self):
        print(self.name.title() + ' make some handshake.')


my_dog = Dog('fubaobao', 2)
my_dog.sit()
my_dog.handshake()

first_dog = Dog('zhangpaopao', 5)
second_dog = Dog('fubaobao', 2)

print("My first dog's name is " + first_dog.name.title() + '.')
print("My first dog's age is " + str(first_dog.age) + '.')
first_dog.sit()

print("My second dog's name is " + second_dog.name.title() + '.')
print("My second dog's age is " + str(second_dog.age) + '.')
second_dog.handshake()
