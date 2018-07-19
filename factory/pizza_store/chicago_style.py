from factory.pizza.chicago_style import ChicagoStyleCheesePizza, ChicagoStylePepperoniPizza, \
    ChicagoStyleClamPizza, ChicagoStyleVeggiePizza
from factory.pizza_store.generic import PizzaStore


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None

        if pizza_type == "cheese":
            pizza = ChicagoStyleCheesePizza()
        elif pizza_type == "pepperoni":
            pizza = ChicagoStylePepperoniPizza()
        elif pizza_type == "clam":
            pizza = ChicagoStyleClamPizza()
        elif pizza_type == "veggie":
            pizza = ChicagoStyleVeggiePizza()

        return pizza
