# 给列表中每一个用户传递一个hello

def sayhi(names):
    for name in names:
        say_hello = 'Hello, ' + name.title() + '.'
        print (say_hello)

my_fam = ['fupaopao', 'fubaobao', 'zhangpaopao']

sayhi(my_fam)