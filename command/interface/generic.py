from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    def get_class_name(self):
        """Return a package.module.class style name variable.

        NOTE: Explanation of str(self.__class__).split("'")[1]

        str(self.__class__) -> "<class 'command.interface.light.LightOnCommand'>"

        But I only want the class name ...
        self.__class__.__name__ -> 'LightOnCommand'
        Which isn't enough.

        So I split the first string on "'".
        str(self.__class__).split("'") -> ['<class ', 'command.interface.light.LightOnCommand', '>']
        And kept only the index 1 term!
        str(self.__class__).split("'")[1] -> 'command.interface.light.LightOnCommand'
        """

        return str(self.__class__).split("'")[1]


class NoCommand(Command):
    def execute(self):
        pass
