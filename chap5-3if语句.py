# if-elif-else语句

#单elif语句
age_me = 35
if age_me < 21:
    print ('Too young to work!')
elif age_me <= 34:
    print ('U r siut to work!')
else: #else后面不用接条件,其他条件的余值即是else  
    print ('Too old to work in IT!')
#仅在前面的测试未通过的情况下才会执行下一个条件语句

#多elif语句+省略else
age = 35
if age < 25:
    salary = 5000
elif age <32:
    salary = 15000
elif age <= 35:
    salary = 20000
elif age >35:
    salary =6000

print ('Your salary is $' + str(salary)+'!')

#if-elif-else只能检查单个条件,如要检查多个条件是否满足,需要用多个if:
muwu = ['beer','pork','mutton','beef','bean']

if 'beer' in muwu:
    print ('Beer added')
if 'mutton' in muwu:
    print ('Mutton added')
if 'peanut' in muwu:
    print ('Peanut added')

print ('Your Menu done!')