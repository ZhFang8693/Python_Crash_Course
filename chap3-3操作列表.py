# chap3-3 组织列表

# 使用.sort()对原列表进行永久性重新排序
family = ['zhangfang','fupaopao','zhangpaopao','fubaobao']
family.sort()
print (family)

# 使用.sorted()对原列表进行暂时性排序
family = ['zhangfang','fupaopao','zhangpaopao','fubaobao']
print (sorted(family))
# 调用函数sorted()后,可以直接临时排序,但是family的顺序并没有变:
print (family)

# 让列表的元素按照索引反着排,需要用到reverse()方法:
family.reverse()
print (family)
# reverse()对列表的修改和.sort()一样,是永久性的;但是我们随时可以更改回来:再用一次reverse()即可

# 确定列表的长度,使用到的函数是len();需要注意的是,在python中对长度的计算,与C语言等不一样,有多少
# 个元素则长度就为几,不会减1;索引则还是一样从0算起,最后的索引值会比长度少1;
print (len (family))


