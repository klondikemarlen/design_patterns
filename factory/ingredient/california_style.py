from factory.ingredient.generic import PizzaIngredientFactory


class CaliforniaPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return GlutenFreeDough()

    def create_sauce(self):
        return BarbecueSauce()

    def create_cheese(self):
        return DaiyaCheeseShreds()

    def create_veggies(self):
        return [Kale(), Jalapenos(), Zucchini()]

    def create_pepperoni(self):
        return SlicedFieldRoastMexicanChipotleSausage()

    def create_clam(self):
        return TofuClam()


class GlutenFreeDough: pass
class BarbecueSauce: pass
class DaiyaCheeseShreds: pass
class Kale: pass
class Jalapenos: pass
class Zucchini: pass
class SlicedFieldRoastMexicanChipotleSausage: pass
class TofuClam: pass
