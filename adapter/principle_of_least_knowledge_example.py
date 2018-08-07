class Doors:
    def lock(self):
        pass


class Car:
    def __init__(self):
        # Here is a component of this class. We can call its methods.
        self.engine = None

    def start(self, key):
        # Here we are creating a new object, its methods are legal.
        doors = Doors()

        # You can call a method on an object passed as a parameter.
        authorized = key.turns()

        if authorized:
            # You can call a method on a component of the object.
            self.engine.start()
            # You can call a local method within the object.
            self.update_dashboard_display()
            # You can call a method on an object you create or instantiate.
            doors.lock()

    def update_dashboard_display(self):
        pass
