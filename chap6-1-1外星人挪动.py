from shutil import move


aliens = {'x-position':0,'y-position':15,'speed':'slow'}
print ('Now this fuking aliens is in X:' + str(aliens['x-position']) + '; Y:' + str(aliens['y-position']))

if aliens['speed'] == 'slow':
    fly = 1
elif aliens['speed'] == 'mid':
    fly = 2
else:
    fly = 3

print ('The aliens flying' + aliens['speed'] + ',' + 'so it moved to X:' + str(aliens['x-position']+fly))