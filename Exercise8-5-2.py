def my_profile(first_name,last_name,**other_profile):
    zhfang_profile = {}

    zhfang_profile['first name'] = first_name
    zhfang_profile['last name'] = last_name
    for key,value in other_profile.items():
        zhfang_profile[key] = value
    return zhfang_profile

Zhfangs = my_profile (
    'Fang', 'Zhang', weight = '180kg', height = '172cm', favor = 'beer'
)
print (Zhfangs)