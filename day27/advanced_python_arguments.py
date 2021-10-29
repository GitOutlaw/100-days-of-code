# Unlimited Positional Arguments

# def add(*args):
#     print(args[0])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(1,5,5,15))


# Keyword Arguments (optinal)
# def calculate(n,**kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     # print(kwargs["add"])

#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2,add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.year = kwargs.get("year")
        self.seats = kwargs.get("seats")

my_car = Car(make="Volvo", model="S60")
print(my_car.model)



