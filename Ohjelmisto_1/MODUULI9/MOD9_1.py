class Car:
    def __init__(self, licence, topspeed):
        self.licence = licence
        self.topsteed = topspeed
        self.speed = 0
        self.distance = 0

car = Car("ABC-123", 142)

print(f"{car.licence} top speed is {car.topsteed}km/h currently traveling {car.speed}km/h and traveled for {car.distance}km ")
