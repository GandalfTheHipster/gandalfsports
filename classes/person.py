class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def speak(self, message):
        print(f"{self.name} says: {message}")

    def swear(self):
        print(f"{self.name} swears")

    def name(self):
        print(f"{self.name}")

    def __repr__(self):
        return f"{self.name}" if self.age is None else f"{self.name}, age {self.age}"