import random, csv
from cars import *
from time import sleep
from datetime import datetime

print('== == == == == WELCOME TO THE == == == == ==')
print('== = == NEED FOR SPEED TERMINAL RACE == = ==\n')

number_of_cars = 0
racenr = 0
place = {}
speed = {}
car = {}

with open('cars.csv') as cars_csv:
    csv_reader = csv.DictReader(cars_csv)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        car[line_count - 1] = row['NAME']
        line_count += 1
    number_of_cars = line_count - 1

race = True
while race:
    for x in range(number_of_cars):
        place[x] = 0
    length = random.randint(15, 25)
    racenr += 1
    answer = input(
        '\nChoose the option (type option number):\n'
        f'1 Start race {length}\n'
        '2 See score - board\n'
        '3 Quit the game\n'
    )
    racetrack = True
    if answer == '1':
        print(f'Race on track-length {length}')
        for x in range(number_of_cars):
            print(*get_track(place[x], car[x], length))
        print()
        sleep(1.5)
        time_start = datetime.now()
        while racetrack:
            for x in range(number_of_cars):
                speed[x] = random.randint(1, 2)
                place[x] += speed[x]
                print(*get_track(place[x], car[x], length))
            print()
            for y in range(number_of_cars):
                if place[y] >= length:
                    print(f'Car {car[y]} win! ')
                    get_save(racenr, car[y], length, time_start)
                    racetrack = False
                    break
            sleep(0.5)
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
