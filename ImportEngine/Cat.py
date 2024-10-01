class Cat():
    def __init__(self, name: str, age: int, is_indoor=True):
        self.name = name
        self.age = age
        self.is_indoor = is_indoor

    def speak(self):
        print('rrr')

    def __repr__(self):
        return f'<{self.name}, {self.age}, {self.is_indoor}>'
