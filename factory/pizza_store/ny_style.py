from factory.pizza_store.generic import PizzaStore
from factory.pizza.veggie import VeggiePizza
from factory.pizza.clam import ClamPizza
from factory.pizza.pepperoni import PepperoniPizza
from factory.pizza.cheese import CheesePizza
from factory.ingredient.ny_style import NYPizzaIngredientFactory


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "New York Style Pepperoni Pizza"
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "New York Style Clam Pizza"
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "New York Style Veggie Pizza"

        return pizza
