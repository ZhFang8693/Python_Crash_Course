muwu = ['beer','pork','mutton','beef','bean']
for cai in muwu:
    if cai == 'bean':
        print ('Sorry, bean sold out')
    else:
        print ('Add ' + cai + ' to the list.')

print ("That's ur list!")

# 确定列表是否为空
muwu = []
if muwu: #在if语句中将列表名用在条件表达式中时,如果列表至少包含一个元素,则返回True,否则返回False
    for cai in muwu:
        print ('Add ' + cai + ' to the list.')
    print ("That's ur list!")
else:
    print ('Your list is empty!')

#多个列表为条件
muwu = ['beer','pork','mutton','beef','bean']
iwant = ['beer','mutton','soap']

for things in iwant:
    if things in muwu:
        print ('OK,add ' + things + ' to the list!')
    else:
        print ('Sorry, muwu have no ' + things + '.')

print ("That's ur list!")
