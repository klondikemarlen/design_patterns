from abc import ABC


class Pizza(ABC):
    def prepare(self):
        print("Preparing a pizza.")

    def bake(self):
        print("Baking a pizza.")

    def cut(self):
        print("Cutting a pizza.")

    def box(self):
        print("Boxing a pizza.")


class CheesePizza(Pizza):
    pass


class PepperoniPizza(Pizza):
    pass


class ClamPizza(Pizza):
    pass


class VeggiePizza(Pizza):
    pass
