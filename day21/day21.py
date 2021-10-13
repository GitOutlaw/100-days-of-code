class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

    def eats(self):
        print("Eats food.")


class Fish(Animal):

    # def __init__(self):
    #     super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")

    def swim(self):
        print("Moving in water.")


class Dog(Animal):

    def eats(self):
        super().eats()
        print("Eats dog food.")

    def bark(self):
        print("Woof Woof!")


nemo = Fish()
nemo.breathe()

fido = Dog()
# fido.breathe()
# fido.bark()
fido.eats()
