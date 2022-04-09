ur_name = input("What's your name?\n")
print ('Hello, ' + ur_name)

#多行字符串换行
long_sentece = 'Tell me what is your name, and i will send u a private message what u want to see.'
long_sentece += '\nNow, What is your name?\n'
my_name = input(long_sentece)
print ('Hello, ' + my_name + '!')

#转换输入为int
how_old = input('How old are you?\n')
how_old = int(how_old)
print(how_old+20)

