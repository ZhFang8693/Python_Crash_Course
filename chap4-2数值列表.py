# chap4-2数值列表

# 函数range()生成一系列数
from pickletools import UP_TO_NEWLINE
from tkinter import N


for number in range(1,5):
    print (number)
# 函数range(x,y)会从x开始数,到y之前停止,因此range(1,5)会数到4,因为5前停止

# 使用list()创建数字列表,可以直接将range()作为list的一个参数
number = list(range(1,5))
print (number)

# 可以用z值定义range(x,y,z)的步长(即每一步加几)
Up_to_three = list(range(1,9,3))
print (Up_to_three)

# 1-10的平方数打印
pingfang = []
for value in range(1,11): # 要打印1-10,需要range长度定义为11
    pingfang.append(value**2) # **代表乘方,**后面的数代表几次方,此处给平方这个列表赋值为value的平方

print (pingfang)

# 对数字列表执行简单的统计
my_list = list(range(1,11))
print (max(my_list)) # 列表中的最大值
print (min(my_list)) # 列表中的最小值
print (sum(my_list)) # 列表数值求和

# 列表解析(1-10的平方数的简单做法):
pingfang = [value**2 for value in range(1,11)]
print (pingfang)