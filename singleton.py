class Borg:
    """The Borg design pattern"""

    _shared_attribute = {}

    def __init__(self):
        self.__dict__ = self._shared_attribute


class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # update the attribute dictionary by inserting new key-value pair
        self._shared_attribute.update(kwargs)

    def __str__(self):
        return str(self._shared_attribute)  # Return the attribute dictionary


x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)

y = Singleton(SNMP="Simple Network Management Protocol")
print(y)
