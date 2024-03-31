# Goal: Build a Car object and print its details


class Director:

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):  # Will return a completed car
        return self._builder.car


class Builder:
    """Abstract Builder --> Interface
    Create a Car object and keeps its attributes"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """
    Concerte Builder --> Implements the interface
    Provide parts and tools to work on.
    Provide methods to be used by Director Class
    """

    def add_model(self):
        self.car.model = "SkyLark"

    def add_tires(self):
        self.car.tires = "Regular Tires"

    def add_engine(self):
        self.car.engine = "Turbo Engine"


class Car:
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)
