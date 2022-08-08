
chosethecity = 'input the city u favor, and if you want quit,pls enter quit: '
cities = True

while cities:
    cityinput = input(chosethecity)
    if cityinput == 'quit':
        cities = False
    else:
        print(cityinput)
