zhangfang = {
    'age':35,
    'weight':180,
    'height':172,
}

for key,value in zhangfang.items():#items()方法,返回一个键-值对列表
    print ('\nkey: ' + str(key))
    print ('value: ' + str(value))
#返回的键-值列表和存储顺序可能并不一致,Python不关心顺序,只关心对应关系

#遍历所有键
for index in zhangfang.keys():
    print (index)

#遍历所有值
for nums in zhangfang.values():
    print (nums)

#确认某个键是否在字典:
index_others = 'blood type'
if index_others not in zhangfang.keys():
    print ('We dont have this' + index_others)
else:
    print ('The index of ' + index_others + 'is: ' + zhangfang.values(index_others))

#使用集合set.来对字典进行去重
for index in set(zhangfang.values()):#这时候index就被赋予成一个列表
    print (index)