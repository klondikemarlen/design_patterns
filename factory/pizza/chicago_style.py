from factory.pizza.generic import CheesePizza, PepperoniPizza, ClamPizza, \
    VeggiePizza


class ChicagoStyleCheesePizza(CheesePizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza into square slices.")


class ChicagoStylePepperoniPizza(PepperoniPizza):
    pass


class ChicagoStyleClamPizza(ClamPizza):
    pass


class ChicagoStyleVeggiePizza(VeggiePizza):
    pass
