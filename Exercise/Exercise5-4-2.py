usernames_in_zhihu = ['zhfang','zhangfang','ppooisoad','zfkill1']
usernames_in_mhxy = ['fupaopao','fubaobao','ZhFang','PPooisoad']

for username_in_mhxy in usernames_in_mhxy:
    if username_in_mhxy.lower() in usernames_in_zhihu:
        print ('This username ' + username_in_mhxy + ' is used in zhihu, pls choose another one!')
    else:
        print ('This username ' + username_in_mhxy + ' is not used, u can use it!')
    