from command.remote import RemoteControlWithUndo
from command.vendors.light import Light
from command.vendors.tv import TV
from command.vendors.stereo import Stereo
from command.vendors.hot_tub import HotTub
from command.interface.light import LightOnCommand, LightOffCommand
from command.interface.stereo import StereoOnWithCDCommand, StereoOffCommand
from command.interface.tv import TVOnCommand, TVOffCommand
from command.interface.hot_tub import HotTubOnCommand, HotTubOffCommand
from command.interface.generic import MacroCommand

remote_control = RemoteControlWithUndo()

light = Light("Living Room")
tv = TV("Living Room")
stereo = Stereo("Living Room")
hot_tub = HotTub()

light_on = LightOnCommand(light)
stereo_on = StereoOnWithCDCommand(stereo)
tv_on = TVOnCommand(tv)
hot_tub_on = HotTubOnCommand(hot_tub)

light_off = LightOffCommand(light)
stereo_off = StereoOffCommand(stereo)
tv_off = TVOffCommand(tv)
hot_tub_off = HotTubOffCommand(hot_tub)

party_on_macro = MacroCommand(light_on, stereo_on, tv_on, hot_tub_on)
party_off_macro = MacroCommand(light_off, stereo_off, tv_off, hot_tub_off)

remote_control.set_command(0, party_on_macro, party_off_macro)

print(remote_control)
print("--- Pushing Macro On ---")
remote_control.on_button_was_pressed(0)
print("--- Pushing Macro Off ---")
remote_control.off_button_was_pressed(0)

