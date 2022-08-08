def make_sandwich(*constituentpart):
    print ('The sandwich you want will contain: ')
    for contains in constituentpart:
        print('- ' + contains)
    
make_sandwich('bread')
make_sandwich('bread','meat')
make_sandwich('bread','meat','cheese')