from abc import ABC, abstractmethod

from decorator.starbuzz.interfaces.beverage import Beverage


class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    @abstractmethod
    def get_description(self):
        pass
