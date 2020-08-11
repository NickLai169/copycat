import pyautogui
import time
import os
import sys

from pynput.mouse import Listener as mouse_listener
from pynput.keyboard import Listener as key_listener
from pynput import keyboard

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

sep = os.path.sep
directory = os.path.dirname(os.path.realpath(__file__))
recordings_path = directory + sep + "recordings"
screen_dim = pyautogui.size()



"""
Basic Recording function that records all the inputs and returns a new file
@param args: the input parameters on the command line in a list
@return File which the record function has written to.
"""
def record(args):
    recording_path = directory + sep + "recordings"
    now = time.localtime()
    duration = 10
    name = "{0}-{1}-{2} {3}:{4}:{5}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    retString = "Screen dimension: {0} | Date recorded: {1}".format(screen_dim, name)
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

    print("name: " + name + "({0})".format(type(name)))
    print("duration: " + str(duration) + "({0})".format(type(duration)))
    print(retString)

    """
    Mouse position is formatted as: [time] mouse_pos [x] [y]
    @param x: the horizontal pixel-position of the mouse
    @param y: the vertical pixel-position of the mouse
    """
    def on_move(x, y):
        # print("mouse is at position ({0}, {1})".format(x, y))
        retString += "{2} mouse_pos {0} {1} \n".format(x/screen_dim, y/screen_dim, time.time())

    """
    Mouse position is formatted as: [time] click_pos [x] [y] [button] [pressed]
    @param x: the horizontal pixel-position of the mouse
    @param y: the vertical pixel-position of the mouse
    @param button: which mouse button was pressed
    @param pressed: Boolean representing whether it was pressed down (True) or
        released (False)
    """
    def on_click(x, y, button, pressed):
        # print("Pressed: {0} | Button: {1} | position ({2}, {3})".format(pressed, button, x, y))
        retString += "{4} click_pos {0} {1} {2} {3} \n".format(x/screen_dim, y/screen_dim, button, pressed, time.time())


    """
    Scrolling is formatted as: [time] scoll [x] [y] [dx] [dy]
    @param x: the horizontal pixel-position of the mouse
    @param y: the vertical pixel-position of the mouse
    @param dx: the horizontal scrolling of the mouse
    @param dy: the vertical scrolling of the mouse
    """
    def on_scroll(x, y, dx, dy):
        # print("Scrolling at ({0}, {1}) for dx: {2} and dy: {3}".format(x, y, dx, dy))
        retString += "{0} scroll {1} {2} {3} {4} \n".format(time.time(), x/screen_dim, y/screen_dim, dx/screen_dim, dy/screen_dim)


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

    print(retString)

    # f = open(recordings_path + sep + "peepee.txt", "w+")
    # f.write("Hell omy friends")
    # f.write("Welcome to Game theory")
    # f.close()
