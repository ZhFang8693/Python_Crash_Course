# chap4-1for循环遍历列表

family = ['zhangfang','fupaopao','zhangpaopao','fubaobao']
# 当需要遍历列表,并对每个元素进行操作时,我们可以使用for循环;
for members in family: # for循环后面有冒号的
# 对于for循环中,临时存储值的变量(上面的member),我们可以指定任何符合规则的名称,因此在取名时选择描述单个元素有意义的名称
# 是很有意义的,这样有助于理解for循环对元素执行的操作
    print (members)
    print ('Do u miss me? ' + members.title() + '!\n') # \n必须在字符串内部才是换行

# for循环内部(带缩进)才会针对每一个元素进行重复执行,for循环外部(无缩进)只执行一次.
print ('OK, that`s my whole family!')