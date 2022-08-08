
def dog_profile(name,color,**others):
    basic_profile = {}
    
    basic_profile['Name'] = name
    basic_profile['Color'] = color

    for key,value in others.items():
        basic_profile[key] = value

    return basic_profile

zpp_profile = dog_profile('Zhangpaopao', 'Golden' , weights= '34.7kg', height = '54cm')

print (zpp_profile)