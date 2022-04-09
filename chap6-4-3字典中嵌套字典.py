
users = {
    'zhangfang':
    {
        'firstname':'zhang',
        'lastname':'fang',
        'location':'Hubei'
    },
    'fupp':
    {
        'firstname':'fu',
        'lastname':'paopao',
        'location':'Guangdong'
    } 
}

for user_name,user_loc in users.items():#用user_name定义键,user_loc定义值,那么这里的值是一个字典
    print ("I'm " + user_name)
    full_name = user_loc['firstname'] + " " +user_loc['lastname']#就算值是字典,这里还是要用中括号
    location = user_loc['location']

    print ('\tFull Name:' + full_name.title())
    print ('\tLocation: ' + location.title())
