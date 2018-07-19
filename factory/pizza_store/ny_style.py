from factory.pizza.ny_style import NYStyleCheesePizza, NYStylePepperoniPizza, \
    NYStyleClamPizza, NYStyleVeggiePizza
from factory.pizza_store.generic import PizzaStore


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None

        if pizza_type == "cheese":
            pizza = NYStyleCheesePizza()
        elif pizza_type == "pepperoni":
            pizza = NYStylePepperoniPizza()
        elif pizza_type == "clam":
            pizza = NYStyleClamPizza()
        elif pizza_type == "veggie":
            pizza = NYStyleVeggiePizza()

        return pizza
