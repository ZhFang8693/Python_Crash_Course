#使用while和输入配合进行使用

def get_name(first_name, last_name, middle_name=''):
    full_name = first_name + middle_name + last_name
    return full_name.title()

while True:
    print ('Would you like tell me your name?')
    f_name = input('Your first name is: \n')
    m_name = input('Do you have mid name? if not, please enter space: \n')
    l_name = input('Your last name is: \n')

    if f_name or l_name or m_name == 'q':
        break
# 这里再次搞错了,一定要注意调用函数时,函数形参和调用实参的对应关系!
named = get_name(f_name,l_name,m_name)
print ('Hello, and now i know your name is ' + named)
