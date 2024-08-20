# This module is ment to allow users to run functions on classes, when the class is created, and when a class is instantiated.
from apply import Apply


def on_subclass(*args, **kwargs):
    print("Subclass created", args, kwargs)

def on_instance(*args, **kwargs):
    print("Instance created", args, kwargs)

class TestClass(Apply(on_subclass=on_subclass, on_instance=on_instance)):
    ...

if __name__ == '__main__':
    t = TestClass()