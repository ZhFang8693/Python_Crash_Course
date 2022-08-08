what_is_favor = {}
# 设定标志
runing = True
while runing:
    name = input('What is ur name? ')
    favor_food = input('\nAnd ur favor food is? ')
# 注意这里对字典的定义模式
    what_is_favor[name] = favor_food

    want_quit = input('Are u done?' )
    if want_quit == 'Yes':
        runing = False

print ('Ur name and favor food is\n')
print (what_is_favor)
    