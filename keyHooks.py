# https://github.com/boppreh/keyboard

import keyboard
import time
# hotkey = "alt + ctrl + e"
# # Remember that the order in which the hotkey is set up is the order you need to press the keys.

# while True:
#     time.sleep(0.1)
#     if keyboard.is_pressed(hotkey):
#         print("Hotkey is being pressed")


def hook(hotkey, callback, args=None):
    keyboard.add_hotkey(hotkey, callback, args=args)


def unhook(hotkey):
    keyboard.remove_hotkey(hotkey)


def wait(key):
    keyboard.wait(key)


def loop():
    keyboard.wait()


# def waitFor(hotkey, list):
#     # go = [True]
#     # def call_exit():
#     #     global go
#     #     print('calling')
#     #     go[0] = False #set to continue doing the action
#     while(list[0]):
#         if(keyboard.is_pressed(hotkey)):
#             list[0] = True
#             break
#         print(list[0])
#         time.sleep(0.2)


# wait on for specific input

# keyboard.unhook_all()
# keyboard.unhook_all_hotkeys()
# keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
# keyboard.wait()
