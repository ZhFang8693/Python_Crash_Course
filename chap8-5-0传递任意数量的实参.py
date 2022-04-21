# 使用 *name 为函数创建一个空的元组
# 复习:不可变的列表称之为元组,元组用圆括号表示,列表用方括号表示,字典用大括号表示
def make_pizza(*topping):
    print (topping)

make_pizza('peeper')
make_pizza('mushroom', 'peeper', 'beef', 'cheese')

# 元组一样可以进行循环:
def make_dog_food(*things):
    print ("I will make some dog food with things next: \n")
    for thing in things:
        print('-' + thing)

make_dog_food('chickens')
make_dog_food('meat', 'beef', 'chickens', 'broccoli')