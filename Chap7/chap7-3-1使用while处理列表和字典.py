# 列表挪动
family_members = ['zhangpaopao','fubaobao','fupaopao']
in_house_members = []
# while会循环直到到family_member为空
while family_members:
# 创建一个in_house_member,用来承载family_members的元素
# .pop函数作用是每次从列表末尾删除一个元素
    in_house_member = family_members.pop()
    print ('Checked out!' + in_house_member.title() + ' is at home!')
# 将.pop删除的元素用.append方法赋值到in_house_members下面的in_house_member上
    in_house_members.append(in_house_member)

print ('All the members at home is ')
for in_house_member in in_house_members:
    print(in_house_member.title())

print(in_house_members)
member = 'zhangpaopao'
while member in in_house_members:
# 用.remove方法删除指定元素;这种方法要指定的是列表,而不是列表中的元素.
# TODO:如何指定用while XX=xx来删掉fubaobao
    in_house_members.remove(member)
print(in_house_members)
