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


def ending(racenr, winner, length, time_start):
    time_finish = length * (datetime.now() - time_start)
    time_all = str(time_finish).split('.')[0]
    with open('results.txt', mode='a') as file:
        file.write(f'\n{racenr}, {winner}, {time_all}')
