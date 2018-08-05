from adapter.turkey_example.turkey import Turkey


class DuckAdapter(Turkey):
    def __init__(self, duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        self.duck.fly()
        print("... a short distance")
