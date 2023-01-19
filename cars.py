from car import *
from datetime import datetime

car1 = Car(
    name='B',
    type='Audi',
    color='blue',
    power=100
)
car2 = Car(
    name='R',
    type='BMW',
    color='red',
    power=101
)


def track(length, place, car):
    for x in range(0, place):
        print('_', end='')
    print('', end=car)
    for x in range(place, length):
        print('_', end='')


# TODO: racenr is a confusing parameter name. Change to "race_number".
#  Do not be afraid of using longer, descriptive names
def ending(racenr, winner, length, time_start):
    time_finish = length * (datetime.now() - time_start)
    time_all = str(time_finish).split('.')[0]
    with open('results.txt', mode='a') as file:
        file.write(f'\n{racenr}, {winner}, {time_all}')
