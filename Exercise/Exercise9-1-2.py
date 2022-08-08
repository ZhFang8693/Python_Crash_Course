# 创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。
# 在类User 中定义一个名 为describe_user() 的方法，它打印用户信息摘要；
# 再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。

class User():

    def __init__(self, first_name, last_name, **others):

        self.first = first_name
        self.last = last_name

        other_describe = {}
        self.other_describe = others
        for key, value in others.items():
            other_describe[key] = value

    def describe_user(self):
        print(self.first.title() + ' ' + str(self.last.title()))
        print("And your others describe is: \n" + str(self.other_describe))

    def greet_user(self):
        print("Hello" + str(self.first) + str(self.last))


my_profile = User('zhang', 'fang', weight='180', height='172')

my_profile.describe_user()
my_profile.greet_user()
