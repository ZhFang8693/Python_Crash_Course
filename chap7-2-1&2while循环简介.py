
current_num = 1
while current_num <= 5:
    
    #结果是23456
    #current_num += 1
    #print (current_num)
   
    print (current_num)
    current_num += 1

sec = 'There is a password, if u input it right, u can get out of this circle'
sec += '\nInput the password: '
paswd = ''

while paswd != 'quit':
    paswd = input(sec)
# 退出后不显示"quit"
if paswd == 'input':
    print (paswd)
