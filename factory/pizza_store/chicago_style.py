from factory.pizza_store.generic import PizzaStore
from factory.pizza.veggie import VeggiePizza
from factory.pizza.clam import ClamPizza
from factory.pizza.pepperoni import PepperoniPizza
from factory.pizza.cheese import CheesePizza
from factory.ingredient.chicago_style import ChicagoPizzaIngredientFactory


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "Chicago Style Cheese Pizza"
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "Chicago Style Pepperoni Pizza"
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "Chicago Style Clam Pizza"
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "Chicago Style Veggie Pizza"

        return pizza
