class Pizza:
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


class GreekPizza(Pizza):
    pass


class PepperoniPizza(Pizza):
    pass


class ClamPizza(Pizza):
    pass


class VeggiePizza(Pizza):
    pass


class SimplePizzaFactory:
    def create_pizza(self, pizza_type):
        pizza = None

        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza()
        elif pizza_type == "clam":
            pizza = ClamPizza()
        elif pizza_type == "veggie":
            pizza = VeggiePizza()

        return pizza


class PizzaStore:
    def __init__(self, factory):
        self.factory = factory

    def ordering_pizza(self, pizza_type):
        pizza = self.factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


pizza_store = PizzaStore(SimplePizzaFactory())
pizza_store.ordering_pizza("cheese")
