from factory.pizza_store.ny_style import NYStylePizzaStore
from factory.pizza_store.chicago_style import ChicagoStylePizzaStore

ny_store = NYStylePizzaStore()
chicago_store = ChicagoStylePizzaStore()

pizza = ny_store.ordering_pizza("cheese")
print("Ethan ordered a {}.\n".format(pizza.name))

pizza = chicago_store.ordering_pizza("cheese")
print("Joel ordered a {}.\n".format(pizza.name))
