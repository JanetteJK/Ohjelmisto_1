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




car = Car("ABC-123", 142)

print(f"{car.licence} top speed is {car.topspeed}km/h currently traveling {car.speed}km/h and traveled for {car.distance}km ")
car.exhilerate(30)
print(f"Cars current speed is {car.speed}km/h")
car.exhilerate(70)
print(f"Cars current speed is {car.speed}km/h")
car.exhilerate(50)
print(f"Cars current speed is {car.speed}km/h")
car.exhilerate(-200)
print(f"Cars current speed is {car.speed}km/h")