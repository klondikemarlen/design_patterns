"""
To make any object in Python an iterable you need to implement
the __iter__ method (https://docs.python.org/3.5/tutorial/classes.html?highlight=iterator#iterators). Python Enum is something different from the Java Enumeration Iterator.

To iterate through an Iterable in Python:

for x in example_iterable:
    print(x)

All that being said ... possible translation is:
"""

from abc import ABC, abstractmethod


class Enumeration(ABC):
    @abstractmethod
    def has_more_elements(self):
        pass

    @abstractmethod
    def next_element(self):
        pass


class Iterator(ABC):
    """A Java/Python iterator mash-up interface.

    NOTE: Python only requires the __iter__ method to make an iterable.

    I chose to make this code more similar to the book and mapped
    Java next to Python __next__. I made the iterator automatically
    supply an __iter__ but require __next__ to implement the iterator
    as it fit better with Java Enumeration Interface.
    """
    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def remove(self):
        pass


class EnumerationIterator(Iterator):
    """Translate a Javaesque Enum to a Pythonesque Iterator

    With a pointless remove method.
    """
    def __init__(self, enum):
        self.enum = enum

    def __next__(self):
        """Call Java enum.next_element.

        Pure Python style would probably do:
        try:
            self.enum.next_element()
        except NoMoreElementsExampleError:
            raise StopIteration
        """
        if self.enum.has_more_elements() is False:
            raise StopIteration
        return self.enum.next_element()

    def has_next(self):
        """Implement Java Enumeration has_more_elements.

        This wouldn't be used in Python much as
        "It is better to ask for forgiveness than permission."
        Instead you would do:

        try:
            next(self)
        except StopIteration:
            print("No more elements")

        For loops are very clean in python an handle this for you.
        So you can instead do:
        for element in Iterator():
            print(element)
        """
        self.enum.has_more_elements()

    def remove(self):
        """Prevent using of remove.

        I chose TypeError as seeming most conceptually similar to
        Java UnsupportedOperationException
        """
        raise TypeError("This object can't support this operation.")


"""
This would now allow you to do:

enum = ExampleEnumeration()

adapted_enum = EnumerationIterator(enum)

for element in adapted_enum:
    print(element)
"""
