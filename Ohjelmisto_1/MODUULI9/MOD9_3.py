
class Car:
    def __init__(self, licence, topspeed):
        self.licence = licence
        self.topspeed = topspeed
        self.speed = 60
        self.distance = 2000
    def exhilerate(self, speed_change):
        self.speed = speed_change + self.speed
        if self.speed > self.topspeed:
            self.speed = self.topspeed
        elif self.speed < 0:
            self.speed = 0
    def travelled(self, hours):
        self.distance = self.distance + self.speed * hours
        print(f"New travelled distance is {self.distance}km")

car = Car("ABC-123", 142)
car.travelled(1.5)