# 创建一个包含魔术师名字的列表,并将其传递给一个show_magicicans()函数

magicians = ['Johnason', 'Jay', 'Aowson']

# print name
def show_magicians(magic_names):
    
        for magic_name in magic_names:
            print (magic_name)

show_magicians(magicians)

# add great 

def make_great(magic_names):
    #great = 'The great'
    for magic_name in magic_names:
# TODO:这里为什么不能用自相加的方式?
        magic_name = 'The Great ' + magic_name

make_great(magicians)
show_magicians(magicians)

def add_great(magic_names,add = 'The Great'):
    for magic_name in magic_names:
        great_name = add + ' ' + magic_name
        print (great_name)
# TODO:不是说函数会永久改变列表信息么?为什么这里函数调用后,再打印,却没有改变信息
add_great(magicians)
print (magicians)



# --------------------------------
# 修改你为完成练习8-10而编写的程序，在调用函数make_great() 时，向它传递魔术
# 师列表的副本。由于不想修改原始列表，请返回修改后的 列表，并将其存储到另一个列表中。分
# 别使用这两个列表来调用show_magicians() ，确认一个列表包含的是原来的魔术师名字，而另
# 一个列表包含的是添加了字 样“the Great”的魔术师名字。
# --------------------------------
# TODO:由于上述函数没有改变列表magicians的值,那么该题无法继续