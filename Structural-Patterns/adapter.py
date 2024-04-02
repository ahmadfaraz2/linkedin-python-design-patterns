class Korean:
    """Korean Speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong!"


class British:
    """British Speaker"""

    def __init__(self) -> None:
        self.name = "British"

    def speak_british(self):
        return "Hello!"


class Adaptor:

    def __init__(self, object, **adapted_method) -> None:
        self._object = object

        # Add a new dictionary item that establish the mapping between generic method and individual method
        # For example speak() will be translated to speak_korean() if the object is instantiated koren
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of the attributes"""
        return getattr(self._object, attr)


# List to store speaker objects
objects = []

# Create a Korean object
korean = Korean()

# Create a British objec
british = British()

# Append the objects to the object list
objects.append(Adaptor(korean, speak=korean.speak_korean))
objects.append(Adaptor(british, speak=british.speak_british))


for obj in objects:
    print("{} says {}".format(obj.name, obj.speak()))
