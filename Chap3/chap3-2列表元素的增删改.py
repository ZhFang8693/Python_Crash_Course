# chap3-2 列表元素的增删改

from lib2to3.pgen2.literals import evalString


family = ['fupaopao']

# 新增元素
family.append('zhangfang')
print (family)
# .append()方法将会让元素添加到列表的最末尾,从而不影响列表中其他的元素

# 插入元素
family.insert(0,'zhangpaopao')
print (family)
# .insert()方法可以在指定地方插入元素

# 修改元素
family[0] = 'fubaobao'
print (family)
# 将二段新增的元素'zhangpaopao'改为'fubaobao'

# 彻底删除元素
del family[1]
print (family)
# del语句是彻底删除元素,使用del的条件是你必须清楚该元素在列表中的索引位置

# 弹出删除
runing = family.pop()
# 当.pop()括号里没有指定时,则将原列表中最后一个元素弹出列表,该元素可以继续使用
print (runing)

eating = family.pop(0)
# 当.pop()括号里有指定时,则弹出列表中指定索引的元素
print (eating)

# 当不知道索引位置时,使用.remove()方法
family.append('zhangfang')
family.append('fubaobao')
# 刚刚已经把元素都删完了,重新加入几个;另外.append()方法一次只能加一个元素
family.remove('fubaobao')
print (family)