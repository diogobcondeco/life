import sys


def drinkCoffee():
    print ('hum, tasty coffee!')


def eatLunch():
    print ('let\'s lunch! awesome burger')


def eatDinner():
    print ('let\'s dinner! nice steak!')


def code():
    print ('let\'s code! print "hello world"')


alive = True
daysToLive = 50

while alive == True:
    if daysToLive > 0:
        answer = input('Is it morning, afternoon or night?')
        if answer == 'morning':
            print ('it\'s morning')
            drinkCoffee()
            drinkCoffee()
            code()
            print ('good morning')
        elif answer == 'afternoon':
            print ('it\'s afternoon')
            drinkCoffee()
            eatLunch()
            code()
            print ('good afternoon')
        elif answer == 'night':
            print ('it\'s night')
            eatDinner()
            code()
            print ('let\'s sleep it\'s good!')
            daysToLive -= 1
            print ('You have', daysToLive, 'left!')
    elif daysToLive == 0:
        alive = False
        print ('hello coding heaven')
        sys.exit(0)
