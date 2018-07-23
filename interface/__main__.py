from interface.ducks import MallardDuck, ModelDuck
from interface.fly_behaviors import FlyRocketPowered

mallard = MallardDuck()
mallard.perform_quack()
mallard.perform_fly()

model = ModelDuck()
model.perform_fly()
model.fly_behavior = FlyRocketPowered()
model.perform_fly()
