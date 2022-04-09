# 创建几个字典
#创建个空列表
batmans =[]

#batman1 = {'strenth':8,'intelligence':5,'agility':7}
#batman2 = {'strenth':8,'intelligence':5,'agility':7}
#batman3 = {'strenth':8,'intelligence':5,'agility':7}

for batman_number in range(30):#range循环
    new_batman = {'strenth':8,'intelligence':5,'agility':7}
    batmans.append(new_batman)#将new_batman添加到列表batmans[]里

for batman in batmans[:5]:#打印前5个元素
    print (batman)
print ('...')
print ('There are ' + str(len(batmans)) + ' batmans!')

for High_batman in batmans[:3]:#选择前3个
    if High_batman['strenth'] == 8:#创建超级兵
        High_batman['strenth'] == 12
        High_batman['intelligence'] == 10
        High_batman['agility'] =9
for High_batman in batmans[:5]:
    print (High_batman)
print ('...')
