from factory.pizza_store.generic import PizzaStore
from factory.pizza.veggie import VeggiePizza
from factory.pizza.clam import ClamPizza
from factory.pizza.pepperoni import PepperoniPizza
from factory.pizza.cheese import CheesePizza
from factory.ingredient.california_style import CaliforniaPizzaIngredientFactory


class CaliforniaStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None
        ingredient_factory = CaliforniaPizzaIngredientFactory()

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "California Style Cheese Pizza"
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "California Style Pepperoni Pizza"
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "California Style Clam Pizza"
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "California Style Veggie Pizza"

        return pizza
