import random

class Competition:
    def __init__(self, name, lenght, cars):
        self.name = name
        self.lenght = lenght
        self.cars = cars

    def hour_passes(self):
        winner_found = False
        while not winner_found:
            for car in cars:
                car.exhilerate(random.randint(-10, 15))
                car.travelled(1)

    def current_score(self):
        print(f"{cars}, {Car.distance}")

    def competition_over(self):
        winner_found = False
        if cars.distance >= 10000:
            winner_found = True
            cars.sort(key=lambda a: a.distance)
            for car in cars:
                print(f'{car.licence}, {car.topspeed}km/h, {car.speed}km/h {car.distance}km')


class Car:
    def __init__(self, licence, topspeed):
        self.licence = licence
        self.topspeed = topspeed
        self.speed = 0
        self.distance = 0

    def exhilerate(self, speed_change):
        self.speed = speed_change + self.speed
        if self.speed > self.topspeed:
            self.speed = self.topspeed
        elif self.speed < 0:
            self.speed = 0

    def travelled(self, hours):
        self.distance = self.distance + self.speed * hours


competition = Competition("Suuri romuralli", 8000, 10)
cars = []
for i in range(competition.cars):
    topspeed = random.randint(100,200)
    cars.append(Car(f'ABC-{i}', topspeed))
hours = 0
while not Competition.competition_over(True):
    hours = hours +1
    Competition.hour_passes(1)
    if hours>9:
        Competition.current_score
        hours = 0





