#
from toml import TomlDecodeError


sandwich_orders = ['Meat sandwich', 'Pork sandwich', 'Good sandwich', 'Bad sandwich']
Done_sandwichs = []

while sandwich_orders:
    Done_sandwich = sandwich_orders.pop()
    print ('I made your sandwichs' + Done_sandwich)
    Done_sandwichs.append(Done_sandwich)

print ('Now i made these sandwiches:\n')
print (Done_sandwichs)

x = 0

while x < 3:
    Done_sandwichs.append('Baobao sandwich')
    x += 1

print (Done_sandwichs)



while 'Baobao sandwich' in Done_sandwichs:
    Done_sandwichs.remove('Baobao sandwich')

print (Done_sandwichs)