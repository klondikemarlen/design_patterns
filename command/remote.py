from command.interface.generic import NoCommand


class SimpleRemoteControl:
    def __init__(self):
        self.on_commands = [NoCommand()] * 7
        self.off_commands = [NoCommand()] * 7

    def set_command(self, slot_id, on_command, off_command):
        self.on_commands[slot_id] = on_command
        self.off_commands[slot_id] = off_command

    def on_button_was_pressed(self, slot_id):
        self.on_commands[slot_id].execute()

    def off_button_was_pressed(self, slot_id):
        self.off_commands[slot_id].execute()

    def __str__(self):
        """Pretty display of Remote Control."""
        width = 52
        display = "\n------ Remote Control ------\n"
        for i in range(len(self.on_commands)):
            display += "[slot {}] {:<{width}}{}\n".format(i, self.on_commands[i].get_class_name(), self.off_commands[i].get_class_name(), width=width)
        return display
