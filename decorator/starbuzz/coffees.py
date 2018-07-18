from decorator.starbuzz.interfaces.beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self):
        return 0.89


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Dark Roast Coffee"

    def cost(self):
        return 0.99


class Decaf(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Decaf Coffee"

    def cost(self):
        return 1.05
