from functools import wraps


def make_blink(function):
    """Defines the Decorator"""

    @wraps(function)

    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


@make_blink
def hello_world():
    """Original Function"""

    return "Hello, World!"


print(hello_world())

print(hello_world.__name__)

print(hello_world.__doc__)


# ~~~~~~~~~~~~~~~~~~~~~~~~~Manual Decorator~~~~~~~~~~~~~~~~~~~~~~~


def my_decorator(func):
    def wrapper():
        print("Do something")
        func()
        print("The main function is finished.")

    return wrapper


@my_decorator
def greet_people_by_name():
    print("Hi Ahmad")


print(greet_people_by_name())
