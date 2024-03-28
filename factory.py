class Dog:
    """A simle dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    """A simple cat class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """The Factory Method"""

    pets = dict(dog=Dog("Tomy"), cat=Cat("Manno"))
    return pets[pet]


d = get_pet("dog")
print(d._name, d.speak())

c = get_pet("cat")
print(c._name, c.speak())
