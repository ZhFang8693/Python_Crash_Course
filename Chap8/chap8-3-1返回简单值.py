# 试试返回值
def full_names(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

my_name = full_names('zhang', 'fang')
print (my_name)

# 默认值作为"可选值"的操作
# 指定为默认值的,要在后面,不能在前面,且一次只能指定一个默认值
def ful_name(first_name,last_name,middle_name=''):
    full_name_1 = first_name + ' ' + middle_name + ' ' + last_name
    return full_name_1.title()
zf_name = ful_name('zhang','fang')
# 用位置实参的时候,要注意顺序
paopao_name = ful_name('fu','ning','ya')
print('\n' + zf_name)
print(paopao_name)