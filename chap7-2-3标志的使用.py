# 在多个条件都会导致程序终止的情况下,设置一个标志,程序只需要判断这个标志是否符合判断即可

prompta = "tell me sth. and i will judge that if u can quit."
prompta += "\ninput ur content: "

# 设置activation为标志
activation = True
while activation :
    showing = input(prompta)
    # 判断输入的showing值是否是quit
    if showing == 'quit':
        activation = False
    else:
        print(showing)