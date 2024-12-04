from keyHooks import hook, unhook, loop, wait, waitFor
import time
import keyboard

# hook('alt + j', lambda: print('next'))

go = [True]


def call_exit():
    global go
    print('calling')
    go[0] = False


keyboard.add_hotkey("ctrl + f1", call_exit)


waitFor('alt + j', go)


print('continue')

# hook('ctrl + f1', lambda: 1/0)

# wait('alt + j')

# print('cont')


# loop()
