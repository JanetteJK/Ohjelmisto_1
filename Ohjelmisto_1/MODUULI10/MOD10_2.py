class Elevator:
    def __init__(self, first_floor, top_floor):
        self.first_floor = first_floor
        self.top_floor = top_floor
        self.current_floor = first_floor

    def move_up(self):
        self.current_floor = self.current_floor+1
        print(f"Elevator is now on floor {self.current_floor}")

    def move_down(self):
        self.current_floor = self.current_floor-1
        print(f"Elevator is now on floor {self.current_floor}")

    def move_to_floor(self, floor):
        while self.current_floor < floor:
            Elevator.move_up(self)
        while self.current_floor > floor:
            Elevator.move_down(self)

class House:
    def __init__(self, first_floor, top_floor, elevators):
        self.first_floor = first_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(elevators):
            self.elevators.append(Elevator(self.first_floor, self.top_floor))

    def use_elevator(self, elevator, desired_floor):
        self.elevator = elevator
        self.desired_floor = desired_floor
        print(f'Elevator number {elevator} moving to floor {desired_floor}')
        self.elevators[elevator].move_to_floor(desired_floor)





house = House(1, 6, 6)
house.use_elevator(3,5)














