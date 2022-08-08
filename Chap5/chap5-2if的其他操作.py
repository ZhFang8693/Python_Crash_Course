car = 'audi'

if car == 'Audi':
    print ('Yes')
else:
    print ('No')
# 在Python中,对字符串的相等检查是区分大小写的

if car.lower() == 'audi':
    # 如果大小写无关紧要,可以使用lower()\upper()来转换为小写再进行比较,函数lower()不会改变原函数值
    print ('Yes')
else:
    print ('No')

whatiwant = 'money'
if whatiwant != 'food':# 在此处与whatiwant对比,如果不相等则返回True,否则返回False.
    print ('That`s my favor')

#检查and
age_me = 35
age_she = 27
if age_me > 36 and age_she < 30:
    print ('Y')
else:
    print ('N')

#检查or
age_me = 35
age_she = 27
if (age_me > 36) or (age_she < 30):# 加括号增加可读性
    print ('Y')
else:
    print ('N')

# 检查特定值是否包含在列表
my_favor = ['beer','meat','pork','cola']
if 'wine' in my_favor:
    print ('No')
else:
    print ('Yes')