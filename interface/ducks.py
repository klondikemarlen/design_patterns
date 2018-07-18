import abc

from interface.quack_behaviors import Quack
from interface.fly_behaviors import FlyWithWings, FlyNoWay


class Duck(abc.ABC):
    def set_fly_behavior(self, fb):
        self._fly_behavior = fb

    def set_quack_behavior(self, qb):
        self._quack_behavior = qb

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @abc.abstractmethod
    def __init__(self):
        self._fly_behavior = None
        self._quack_behavior = None

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
        self._fly_behavior = FlyWithWings()
        self._quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck.")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self._fly_behavior = FlyNoWay()
        self._quack_behavior = Quack()

    def display(self):
        print("I'm a model duck.")
