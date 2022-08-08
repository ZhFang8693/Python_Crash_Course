# This file just creat for module

def make_pizza(size,*toppings):
    print ('Make a ' + str(size) + 
    '-inch pizza with the following toppings:'
    )
    for topping in toppings:
        print ('-' + topping)

