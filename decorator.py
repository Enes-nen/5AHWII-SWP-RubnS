import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator

def decorator2(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_decorator

@decorator
def say_hi(name):
    print(name)

@decorator2
def say_whee():
    print("whee")

say_hi("Enes")
say_whee()


def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"DEGUG: Methode {func.__name__} wird aufgerufen")
        result = func(*args, **kwargs)
        print(f"DEGUG: Methode {func.__name__} wird abgeschlossen")
        return result
    return wrapper

class Device:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    @log_action
    def turn_on(self):
        print(f"{self.name} wird eingeschaltet.")

d = Device("Lenovo", 10)
d.turn_on()