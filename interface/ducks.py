import abc

from interface.quack_behaviors import Quack
from interface.fly_behaviors import FlyWithWings, FlyNoWay


class Duck(abc.ABC):
    """Duck that implements arbitrary fly and quack behaviors.

    NOTE on set/get in python:
    In the simplest use case you don't need these methods in Python!
    Using a method allows for more complex modifications than simple assignment.

    def set_fly_behavior(self, fb):
        print("Duck transformed!")
        self.fly_behavior = fb

    duck.set_fly_behavior(ExampleFlyBehavior())
    """

    @abc.abstractmethod
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    @abc.abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck.")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck.")
