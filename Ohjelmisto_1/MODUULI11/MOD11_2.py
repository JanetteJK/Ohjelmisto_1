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

class Electric_car(Car):
    def __init__(self, licence, topspeed, battery):
        self.battery = battery
        super().__init__(licence, topspeed)


class Gas_car(Car):
    def __init__(self, licence, topspeed, tank):
        self.tank = tank
        super().__init__(licence,topspeed)

car1 = (Electric_car("ABC-15", "180", "52.5"))
car2 = (Gas_car("ACD-123", "165", "32.3"))

car1.speed = 160
car2.speed = 154
car1.travelled(3)
car2.travelled(3)
print(f"The electric car drove for {car1.distance}km.\nThe gas car drove for {car2.distance}km.")




