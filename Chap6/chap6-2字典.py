ages ={'zhfang':35,'fupp':28}
# 字典是"键-值"对,每个键都有一个值与之关联,与键相关联的值可以是字符串\数字\列表甚至是字典,事实上可以将任何Python对象
# 作为字典的值

print (ages['zhfang'])
#指定字典名&字典键值即可得到该键对应的值

#添加键-值:
ages ['zhangpp'] = '四岁半'
ages ['fubb'] = 1.8

print (ages['zhangpp'])

#修改键-值
ages ['fubb'] = 1.97
print (ages['fubb'])

#删除键-值
del ages['fubb']
print (ages)