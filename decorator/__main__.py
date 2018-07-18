from decorator.coffees import Espresso, DarkRoast, HouseBlend
from decorator.condiments import Mocha, Whip, Soy


beverage = Espresso()
print("{} ${}".format(beverage.get_description(), beverage.cost()))

beverage2 = DarkRoast()
beverage2 = Mocha(beverage2)
beverage2 = Mocha(beverage2)
beverage2 = Whip(beverage2)
print("{} ${}".format(beverage2.get_description(), beverage2.cost()))

beverage3 = HouseBlend()
beverage3 = Soy(beverage3)
beverage3 = Mocha(beverage3)
beverage3 = Whip(beverage3)
print("{} ${}".format(beverage3.get_description(), beverage3.cost()))

