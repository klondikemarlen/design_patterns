"""
Thread-safe concept from https://gist.github.com/werediver/4396488
Metaclass concept from https://stackoverflow.com/q/6760685

Please note that there are at least 4 other pretty sensible ways of doing
this but I opted for this one, as it is the most resistant to modification.
A method I believe warrants special mention is the Module approach as Python modules are essentially Singleton instances.

If you want code that you could just drop into a class, and avoid using
inheritance you could do:

import threading

class ExampleSingleton:
    _singleton_lock = threading.Lock()
    _singleton_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton_instance:
            with cls._singleton_lock:
                if not cls._singleton_instance:
                    cls._singleton_instance = super().__new__(cls, *args, **kwargs)
        return cls._singleton_instance

    @classmethod
    def get_instance(cls):
        return cls._singleton_instance if cls._singleton_instance is not None else cls()
"""

import threading


class SingletonMeta(type):
    """Thread safe singleton metaclass.

    Do to the nature of metaclasses (that you can only have one of them),
    this code should be safe from multiple inheritance conflicts.

    NOTE: you only need the thread safe version if you are running
    multi-threaded code.
    """
    _singleton_lock = threading.Lock()
    _singleton_instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._singleton_instance:
            with cls._singleton_lock:
                if not cls._singleton_instance:
                    cls._singleton_instance = type.__call__(cls, *args, **kwargs)
        return cls._singleton_instance


class Singleton(metaclass=SingletonMeta):
    """Inheritable Singleton.

    You can use it like:
    class Example(Singleton):
        pass

    I took the idea of using a metaclass + regular class from the Python
    'abc' module.

    NOTE: do to the metaclass architecture you can use either:
    Example() or Example.get_instance()

    They do the same thing.
    """
    @classmethod
    def get_instance(cls):
        return cls._singleton_instance if cls._singleton_instance is not None else cls()

