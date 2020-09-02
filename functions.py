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
Basic Recording function that records all the inputs and returns a new file.
Doesn't allow files with duplucate names
@param args: the input parameters on the command line in a list
    - duration: float representing the duration of the recording
    - name: string representing the of the file (without .txt appeneded)
    - delay: float representing the time to wait before recording
        takes the form of "delay=[float]"
@return File which the record function has written to.
"""
def record(args):
    recording_path = directory + sep + "recordings"
    now = time.localtime()
    duration = 3
    name = "{0}-{1}-{2} {3}, {4}, {5}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    delay = 0

    try:
        for arg in args:
            if "delay" in arg:
                delay = float(arg[6:])
                args.remove(arg)
                break;
    except ValueError:
        print("Formatting Error: Remember that delay should be in the form of: delay=[length]")
        return

    if len(args) > 3:
        print("Too many arguments")
        return

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

    if ".txt" not in name:
        name += ".txt"

    if os.path.exists(recording_path + sep + name):
        print('Recording named "{0}" already exists. Please use alternative name or delete file'.format(name))
        return

    # print("name: {0}".format(name))
    # print("duration: {0}".format(str(duration)))
    # print("delay: {0}".format(str(delay)))
    # return

    while delay > 1:
        delay -= 1
        print("[====== {0} seconds until recoring begins ======]".format(delay))
        time.sleep(1)
    time.sleep(delay)

    f = open(recordings_path + sep + name, "a+")
    print("<========[RECORDING STARTING for {0} SECONDS INTO FILE {1}]========>".format(duration, name))
    f.write("Start_Time: {0} \n".format(time.time_ns()))

    """
    Mouse position is formatted as: [time] mouse_pos [x] [y]
    @param x: the horizontal pixel-position of the mouse
    @param y: the vertical pixel-position of the mouse
    """
    def on_move(x, y):
        # print("mouse is at position ({0}, {1})".format(x, y))
        f.write("{2} mouse_pos {0} {1} \n".format(x/screen_dim[0], y/screen_dim[1], time.time_ns()))

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
        f.write("{4} click_pos {0} {1} {2} {3} \n".format(x/screen_dim[0], y/screen_dim[1], button, pressed, time.time_ns()))


    """
    Scrolling is formatted as: [time] scoll [x] [y] [dx] [dy]
    @param x: the horizontal pixel-position of the mouse
    @param y: the vertical pixel-position of the mouse
    @param dx: the horizontal scrolling of the mouse
    @param dy: the vertical scrolling of the mouse
    """
    def on_scroll(x, y, dx, dy):
        # print("Scrolling at ({0}, {1}) for dx: {2} and dy: {3}".format(x, y, dx, dy))
        f.write("{0} scroll {1} {2} {3} {4} \n".format(time.time_ns(), x/screen_dim[0], y/screen_dim[1], dx/screen_dim[0], dy/screen_dim[1]))

    """
    Key presses are formatted as: [time] pressed [key]
    @param key: The key object that was pressed
    """
    def on_press(key):
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            f.write("{1} pressed {0} \n".format(str(key.char), time.time_ns()))
        except AttributeError:
            # print('special key {0} pressed'.format(key))
            f.write("{1} pressed {0} \n".format(str(key), time.time_ns()))

    """
    Key releases are formatted as: [time] pressed [key]
    @param key: The key object that was pressed
    """
    def on_release(key):
        f.write('{1} release {0}\n'.format(str(key), time.time_ns()).replace("'", ""))
        if key == keyboard.Key.esc:
            print("<######[RECORDING PREMATURELY TERMINATED VIA ESC-Key]######>")
            return False

    """
    Timer function to terminate the listener after the indicated duration has passed
    @param t: The duration that the listener should record for
    """
    def time_me(t):
        time.sleep(t)
        kl.stop()
        ml.stop()

    with key_listener(on_press=on_press,on_release=on_release) as kl:
        with mouse_listener(on_click=on_click, on_scroll=on_scroll) as ml:
            time_me(duration)
            ml.join()
            kl.join()

    f.close()
    print("<========[RECORDING STOPPED]========>")

"""
Moves the mouse from starting x, y position to finishing x,y position
"""
def move_mouse(delay, x_start, y_start, x_finish, y_finish, duration):
    print("nothing yet")

def perform(args):
    print("nothing yet")
