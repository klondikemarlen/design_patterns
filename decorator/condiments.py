from decorator.interfaces.condiment import CondimentDecorator


class Mocha(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()


class SteamedMilk(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Steamed Milk"

    def cost(self):
        return 0.10 + self.beverage.cost()


class Soy(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return 0.10 + self.beverage.cost()
