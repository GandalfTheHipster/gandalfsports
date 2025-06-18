from classes.person import Person

class Player(Person):
    def __init__(self, name, position, age=None, energy=100):
        super().__init__(name, age)  # Calls base class constructor
        self.position = position
        self.energy = energy

    def __repr__(self):
        return f"{super().__repr__()} ({self.position})"

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def shoots(self):
        print(f"{self.name} shoots!")

    def name(self):
        print(f"{self.name}")

    def runs(self, distance):
        self.energy = max(0, self.energy - distance * 0.5)
        print(f"{self.name} runs {distance}m and now has {self.energy:.1f} energy.")

    def rest(self, time):
        self.energy = min(100, self.energy + time * 2)
        print(f"{self.name} rests for {time} min and recovers to {self.energy:.1f} energy.")

    def pass_to(self, teammate):
        if isinstance(teammate, Player):
            print(f"{self.name} passes to {teammate.name}")
        else:
            print(f"{self.name} can't pass to non-players.")

    def is_tired(self):
        return self.energy < 30