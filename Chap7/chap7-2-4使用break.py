# use break to stop the program

favorcity = 'Tell me the city u favor,and if you done it, pls enter quit:'

# while true为开头的循环将不断运行,直到遇到Break
while True:
    cities = input(favorcity)

    if cities == 'quit':
        break
    else:
        print (cities)