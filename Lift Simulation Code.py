class Elevator:
    def __init__(self, min_floor=0, max_floor=10):
        self.current_floor = 0
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.requests = []

    def request_floor(self, floor):
        if floor < self.min_floor or floor > self.max_floor:
            print(f"Invalid floor: {floor}")
            return
        if floor not in self.requests:
            self.requests.append(floor)
            print(f"Floor {floor} requested.")

    def move(self):
        while self.requests:
            next_floor = self.requests.pop(0)
            print(f"Moving from floor {self.current_floor} to floor {next_floor}...")
            while self.current_floor != next_floor:
                if self.current_floor < next_floor:
                    self.current_floor += 1
                elif self.current_floor > next_floor:
                    self.current_floor -= 1
                print(f"Currently at floor {self.current_floor}")
            print(f"Arrived at floor {self.current_floor}. Doors opening...")

    def status(self):
        print(f"Current floor: {self.current_floor}")
        print(f"Pending requests: {self.requests}")


# Example Usage
lift = Elevator(min_floor=0, max_floor=5)

lift.request_floor(3)
lift.request_floor(1)
lift.status()

lift.move()
lift.status()
