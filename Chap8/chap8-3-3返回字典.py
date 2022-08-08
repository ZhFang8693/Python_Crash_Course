##使用函数创建并返回字典

def name_it(first_name,last_name,middle_name = ''):
    person_name = {'first':first_name,"last":last_name,'mid':middle_name}
    return person_name

my_ji = name_it('fu','ning','ya')

print (my_ji)