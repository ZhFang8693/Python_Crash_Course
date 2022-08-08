class Dog:
# 定义类的时候,必须首字母为大写
    def __init__(self, name, age):
    # __init__是一个特殊方法,每档根据类创建新实例时,Python都会自动运行它;
    # 形参self必不可少,且必须位于其他形参的前面;
        self.name = name
        self.age = age
        # 以self为前缀的变量都可供类中的所有方法使用;我们可以通过类的任何实例来访问这些变量;
    def sit(self):
        print(self.name.title() + " is now sitting!")

    def hand_shake(self):
        print(self.name.title() + " hand shaking!")

my_dog = Dog('zhangpaopao', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.hand_shake()