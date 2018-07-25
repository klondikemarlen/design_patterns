from command.remote import SimpleRemoteControl
from command.vendors.light import Light
from command.vendors.garage_door import GarageDoor
from command.vendors.ceiling_fan import CeilingFan
from command.vendors.stereo import Stereo
from command.interface.light import LightOnCommand, LightOffCommand
from command.interface.ceiling_fan import CeilingFanOnCommand, CeilingFanOffCommand
from command.interface.garage_door import GarageDoorUpCommand, GarageDoorDownCommand
from command.interface.stereo import StereoOnWithCDCommand, StereoOffCommand

remote_control = SimpleRemoteControl()
# print(remote)

living_room_light = Light("Living Room")
kitchen_light = Light("Kitchen")
ceiling_fan = CeilingFan("Living Room")
garage_door = GarageDoor("")
stereo = Stereo("Living Room")

living_room_light_on = LightOnCommand(living_room_light)
living_room_light_off = LightOffCommand(living_room_light)
kitchen_light_on = LightOnCommand(kitchen_light)
kitchen_light_off = LightOffCommand(kitchen_light)

ceiling_fan_on = CeilingFanOnCommand(ceiling_fan)
ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

garage_door_up = GarageDoorUpCommand(garage_door)
garage_door_down = GarageDoorDownCommand(garage_door)

stereo_on_with_cd = StereoOnWithCDCommand(stereo)
stereo_off = StereoOffCommand(stereo)

remote_control.set_command(0, living_room_light_on, living_room_light_off)
remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
remote_control.set_command(3, stereo_on_with_cd, stereo_off)

print(remote_control)

remote_control.on_button_was_pressed(0)
remote_control.off_button_was_pressed(0)
remote_control.on_button_was_pressed(1)
remote_control.off_button_was_pressed(1)
remote_control.on_button_was_pressed(2)
remote_control.off_button_was_pressed(2)
remote_control.on_button_was_pressed(3)
remote_control.off_button_was_pressed(3)

