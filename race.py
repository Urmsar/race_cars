import random
from cars import *
from time import sleep
from datetime import datetime

print('== == == == == WELCOME TO THE == == == == ==')
print('== =NEED FOR SPEED TERMINAL RACE == =\n')

race_nr = 0
place1 = place2 = 0
driver1 = car1.name
driver2 = car2.name
race = True
while race:
    place1 = place2 = 0
    length = random.randint(19, 20)
    race_nr += 1
    answer = input(
        '\nChoose the option (type option number):\n'
        f'1 Start race {length}\n'
        '2 See score - board\n'
        '3 Quit the game\n'
    )
    racetrack = True
    if answer == '1':
        print(f'Race on track-length {length}')
        while racetrack:

            time_start = datetime.now()
            speed1 = random.randint(1, 2)
            track(length, place1, driver1)
            print()
            speed2 = random.randint(1, 2)
            track(length, place2, driver2)
            print()
            sleep(1)
            if place1 >= length:
                print(f'Car {driver1} - {car1.color} win! ')
                winner = car1.color
                ending(race_nr, winner, length, time_start)
                break
            place1 += speed1
            print()
            if place2 >= length:
                print(f'Car {driver2} - {car2.color} win! ')
                winner = car2.color
                ending(race_nr, winner, length, time_start)
                break
            place2 += speed2
            print()
    elif answer == '2':
        with open('results.txt') as results:
            for line in results:
                print(line, end='')
            print()
    elif answer == '3':
        race = False
        print('See you on the next race!')
    else:
        print('no such option is offered')
