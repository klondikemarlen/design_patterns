from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Baking for 25 minutes at 350.")

    def cut(self):
        print("Cutting the pizza into diagonal slices.")

    def box(self):
        print("Placing pizza in official PizzaStore box.")
