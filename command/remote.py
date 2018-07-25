class SimpleRemoteControl:
    def __init__(self):
        self.on_commands = [None] * 7
        self.off_commands = [None] * 7

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
            display += "[slot {}] ".format(i)
            if self.on_commands[i] is not None:
                display += "{:<{width}}".format(self.on_commands[i].get_class_name(), width=width)
            else:
                display += "{:<{width}}".format("EMPTY_SLOT", width=width)
            if self.off_commands[i] is not None:
                display += "{}\n".format(self.off_commands[i].get_class_name())
            else:
                display += "{}\n".format("EMPTY_SLOT")
        return display
