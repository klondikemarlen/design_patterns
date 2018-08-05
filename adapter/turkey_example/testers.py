from adapter.turkey_example.duck import MallardDuck
from adapter.turkey_example.turkey import WildTurkey
from adapter.turkey_example.turkey_adapter import TurkeyAdapter


def test_duck(duck):
    duck.quack()
    duck.fly()


def test_turkey_adapter():
    duck = MallardDuck()
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)

    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe duck says...")
    test_duck(duck)

    print("\nThe TurkeyAdapter says...")
    test_duck(turkey_adapter)
