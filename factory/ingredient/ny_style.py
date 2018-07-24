from factory.ingredient.generic import PizzaIngredientFactory


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClam()


class ThinCrustDough: pass
class MarinaraSauce: pass
class ReggianoCheese: pass
class Garlic: pass
class Onion: pass
class Mushroom: pass
class RedPepper: pass
class SlicedPepperoni: pass
class FreshClam: pass
