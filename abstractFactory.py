class Dog:

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):

        return "Dog Food!"


class PetStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by {}".format(pet.speak()))
        print("Its food is {}".format(food))


# Create a Concrete Factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
shop = PetStore(factory)

# Invoke the Utility method to show the details of our pet
shop.show_pet()
