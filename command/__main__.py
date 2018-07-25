from command.remote import RemoteControlWithUndo
from command.vendors.ceiling_fan import CeilingFan
from command.interface.ceiling_fan import CeilingFanMediumCommand, CeilingFanHighCommand, CeilingFanOffCommand

remote_control = RemoteControlWithUndo()

ceiling_fan = CeilingFan("Living Room")

ceiling_fan_medium = CeilingFanMediumCommand(ceiling_fan)
ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

remote_control.set_command(0, ceiling_fan_medium, ceiling_fan_off)
remote_control.set_command(1, ceiling_fan_high, ceiling_fan_off)

remote_control.on_button_was_pressed(0)
remote_control.off_button_was_pressed(0)
print(remote_control)
remote_control.undo_button_was_pressed()

remote_control.on_button_was_pressed(1)
print(remote_control)
remote_control.undo_button_was_pressed()
