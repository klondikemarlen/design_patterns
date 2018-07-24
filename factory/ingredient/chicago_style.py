from factory.ingredient.generic import PizzaIngredientFactory


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return Mozzarella()

    def create_veggies(self):
        return [Spinach(), BlackOlives(), EggPlant()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClam()


class ThickCrustDough: pass
class PlumTomatoSauce: pass
class Mozzarella: pass
class Spinach: pass
class BlackOlives: pass
class EggPlant: pass
class SlicedPepperoni: pass
class FrozenClam: pass
