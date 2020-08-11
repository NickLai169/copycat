import pyautogui
import time
import os
import sys

sep = os.path.sep
directory = os.path.dirname(os.path.realpath(__file__))
recordings_path = directory + sep + "recordings"

f = open(recordings_path + sep + "peepee.txt", "w+")
f.write("Hell omy friends")
f.write("Welcome to Game theory")
f.close()

"""
Basic Recording function that records all the inputs and returns a new file
"""
def record(args):
    recording_path = directory + sep + "recordings"
    now = time.localtime()
    duration = 10
    name = "{0}-{1}-{2} {3}:{4}:{5}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if len(args) == 1:
        try:
            duration = float(args[0])
        except ValueError:
            name = args[0]
    elif len(args) == 2:
        try:
            duration = float(args[0])
            name = args[1]
        except ValueError:
            name = args[0]
            duration = float(args[1])

    # print("name: " + name + "({0})".format(type(name)))
    # print("duration: " + str(duration) + "({0})".format(type(duration)))
    return
    def on_move(x, y):
        print("mouse is at position ({0}, {1})".format(x, y))


    def on_click(x, y, button, pressed):
        print("Pressed: {0} | Button: {1} | position ({2}, {3})".format(pressed, button, x, y))


    def on_scroll(x, y, dx, dy):
        print("Scrolling at ({0}, {1}) for dx: {2} and dy: {3}".format(x, y, dx, dy))


    """ Keyboard Listener below"""

    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))


    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            return False

    def time_me(t=3):
        time.sleep(t)
        kl.stop()
        ml.stop()

    with key_listener(on_press=on_press,on_release=on_release) as kl:
        with mouse_listener(on_click=on_click, on_scroll=on_scroll) as ml:
            time_me(duration)
            ml.join()
            kl.join()
