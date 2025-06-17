from person import Person

class Coach(Person):
    def __init__(self, name, age=None, energy=100):
        super().__init__(name, age)  # Calls base class constructor
        self.energy = energy

    def __repr__(self):
        return f"{super().__repr__()} who coaches"

    def __eq__(self, other):
        return isinstance(other, Coach) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def shoots(self):
        print(f"{self.name} shoots!")