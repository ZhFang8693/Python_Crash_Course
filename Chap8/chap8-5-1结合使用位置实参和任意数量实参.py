
# 如果要函数接受任意数量的实参,就必须把该形参放在最后
def make_dog_food(weight,name,*things):
    print (
        "I will make " + str(weight) + " dog food for " + str(name) + 
        " with next things:"
        )
    for thing in things:
        print (thing)
# 函数会自动将实参一对一的匹配到前面形参,并将剩下的实参全部纳入到最后的不限数量的元组形参中
make_dog_food(1200, 'fubaobao', 'meat', 'chickens', 'broccoli', 'potato')