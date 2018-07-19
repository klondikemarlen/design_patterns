from factory.pizza.california_style import CaliforniaStyleCheesePizza, CaliforniaStylePepperoniPizza, \
    CaliforniaStyleClamPizza, CaliforniaStyleVeggiePizza
from factory.pizza_store.generic import PizzaStore


class CaliforniaStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None

        if pizza_type == "cheese":
            pizza = CaliforniaStyleCheesePizza()
        elif pizza_type == "pepperoni":
            pizza = CaliforniaStylePepperoniPizza()
        elif pizza_type == "clam":
            pizza = CaliforniaStyleClamPizza()
        elif pizza_type == "veggie":
            pizza = CaliforniaStyleVeggiePizza()

        return pizza
