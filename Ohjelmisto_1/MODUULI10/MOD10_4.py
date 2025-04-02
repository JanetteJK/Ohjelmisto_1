import random


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


class Competition:
    def __init__(self, name, lenght, cars_list):
        self.name = name
        self.lenght = lenght
        self.car_list = cars_list
        self.cars = []
        self.time = 0

        for i in range(cars_list + 1):
            self.cars.append(f'car{i}')
            topspeed = random.randint(100, 200)
            self.cars[i - 1] = Car(f'ABC-{i}', topspeed)

    def hour_passes(self):
        for a in self.cars:
            gas = random.randint(-10, 15)
            a.exhilerate(gas)
            a.travelled(1)
            self.time = self.time + 1

    def current_score(self):
        for a in competition.cars:
            print(f'{a.licence}, {a.topspeed}km/h, {a.speed}km/h {a.distance}km')

    def competition_over(self):
        for a in self.cars:
            if a.distance >= self.lenght:
                competition.current_score()


competition = Competition("Suuri romuralli", 8000, 10)

while not Competition.competition_over():

    competition.hour_passes()
    print("An hour passes")
    competition.competition_over()
    if competition.time % 10:
        competition.current_score()

competition.current_score()
