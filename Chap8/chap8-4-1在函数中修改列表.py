#将列表传递给函数后,函数就可以对列表进行修改

unprinted_design = ['iPhone case', 'Android case', 'Web case']
complete_cases = []

while unprinted_design:
    # 加强记忆: .pop()用于从行尾删除一个元素, .pop(元素名)用于删除指定元素
    current_design = unprinted_design.pop()

    print ('Print mode: ' + current_design)
    # 加强记忆: .append()在列表末尾增加元素
    complete_cases.append(current_design)

print ('The following case have been printed:')
for complete_case in complete_cases:
    print (complete_case)
#----------------------------------------------------------------
# 使用函数实现上述案例

# 创建一个专门处理两个列表间元素流动的函数
def print_case(unprinted_design,complete_cases):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print ('Printing Mode: ' + current_design)
        complete_cases.append(current_design)


# 创建一个打印和展示信息函数
def show_print(complete_cases):
    print ('The following case have been printed:')
    for complete_case in complete_cases:
        print (complete_case)

# 创建列表以便调用

unprinted_design = ['iPhone case', 'Android case', 'Web case']
complete_cases = []

# 使用函数

print_case(unprinted_design,complete_cases)
show_print(complete_cases)
# 在这种模式下,unprinted_design列表的内容就被函数永久的改变了

# 如果需要禁止函数修改列表,如将打印过的列表挪到complete_case列表,但是
# unprinted_design列表内容不希望变动,可以如下操作:
# fuction_name(list_name[:])
# [:]切片表示法:创建列表的副本
# 在上述案例中,实现方法就是:
print_case(unprinted_design[:],complete_cases)
# 除了一些特殊情况外,尽量不要使用副本传递