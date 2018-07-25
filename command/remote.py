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
        display = "\n------ Remote Control ------\n"
        for i in range(len(self.on_commands)):
            display += "[slot {}] {}    {}\n".format(i, self.on_commands[i].__class__.__name__, self.off_commands[i].__class__.__name__)
        return display
