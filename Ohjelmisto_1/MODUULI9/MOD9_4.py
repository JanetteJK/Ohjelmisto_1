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

cars = []
for i in range(10):
    topspeed = random.randint(100,200)
    cars.append(Car(f'ABC-{i}', topspeed))

winner_found = False

while not winner_found:
    for car in cars:
        car.exhilerate(random.randint(-10, 15))
        car.travelled(1)
        if car.distance >= 10000:
            winner_found = True



cars.sort(key=lambda a: a.distance)
for car in cars:
    print(f'{car.licence}, {car.topspeed}km/h, {car.speed}km/h {car.distance}km')
