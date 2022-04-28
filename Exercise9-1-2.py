# 创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。
# 在类User 中定义一个名 为describe_user() 的方法，它打印用户信息摘要；
# 再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。

from typing_extensions import Self


class User():

    def _init_(self, first_name, last_name, **others):

        self.first = first_name
        self.last = last_name

        other_describe = {}
        for key,value in others.items():
            other_describe [key] = value

    def describe_user(self):
        print (first_name.title() + ' ' + str(last_name.title()))
        print ("And your others descirbe is: \n" + other_describe)

    def greet_user():
        print ("Hello" + str)