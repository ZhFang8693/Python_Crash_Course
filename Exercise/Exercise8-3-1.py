def city_country(cities,countries):
    c_cfull = cities + ' , '+ countries
    return c_cfull

china = city_country('shanghai','China')
print (china)

def make_album(artist,album_name):
    album_mess = {'Article Name':artist,'Album Name':album_name}
    return album_mess

a_album = make_album('Qi Li Xiang','Jay Chou')

print (a_album)
