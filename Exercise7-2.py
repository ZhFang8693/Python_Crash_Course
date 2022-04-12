
tickit_price = input('please tell me your age, and i will tell you how much u need to pay:')

while tickit_price:
    if int(tickit_price) < 3:
        print ('your age is ' + str(tickit_price) + ' and your ticket price is FREE!')
    
    elif int(tickit_price) < 12 and int(tickit_price) >= 3:
        print ('your age is ' + str(tickit_price) + 'and your ticket price is 10$!')
    else:
        print ('your age is ' + str(tickit_price) + 'and your ticket price is 15$!')
# 没有这句就会一直打印一直打印
    if tickit_price != '':
        break
# 肥肠村炮的一种解决办法
#TODO 