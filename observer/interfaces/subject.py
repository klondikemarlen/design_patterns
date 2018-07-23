import abc


class Subject(abc.ABC):
    @abc.abstractmethod
    def add_observer(self, ob):
        pass

    @abc.abstractmethod
    def delete_observer(self, ob):
        pass

    @abc.abstractmethod
    def notify_observers(self):
        pass

    @property
    @abc.abstractmethod
    def changed(self):
        pass

    @abc.abstractmethod
    def set_changed(self):
        pass

    @abc.abstractmethod
    def clear_changed(self):
        pass


class Observable(Subject):
    @property
    def changed(self):
        return self._changed

    def __init__(self):
        self.observers = []
        self._changed = False

    def add_observer(self, ob):
        self.observers.append(ob)

    def delete_observer(self, ob):
        self.observers.remove(ob)

    def notify_observers(self, *args):
        if self.changed:
            for ob in reversed(self.observers):
                ob.update(self, *args)
        self.clear_changed()

    def set_changed(self):
        self._changed = True

    def clear_changed(self):
        self._changed = False
