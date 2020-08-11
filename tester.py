import pyautogui
import time
import os
import sys

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

dir_path = os.path.dirname(os.path.realpath(__file__))
sep = os.sep
screen_dim = pyautogui.size()

lower_half_screen = (0, int(screen_dim[1]/2), screen_dim[0], int(screen_dim[1]/2))
centre_screen = (int(screen_dim[0]/3), int(screen_dim[1]/3), int(screen_dim[0]/3), int(screen_dim[1]/3))


"""
[TESTING BEGINS]
"""
from pynput.mouse import Listener as mouse_listener
from pynput.keyboard import Listener as key_listener
from pynput import keyboard

""" Mouse Listener below"""
def on_move(x, y):
    print("mouse is at position ({0}, {1})".format(x, y))


def on_click(x, y, button, pressed):
    print("Pressed: {0} | Button: {1} | position ({2}, {3})".format(pressed, button, x, y))


def on_scroll(x, y, dx, dy):
    print("Scrolling at ({0}, {1}) for dx: {2} and dy: {3}".format(x, y, dx, dy))


def time_me_ml(t):
    time.sleep(t)
    ml.stop()
    print("[[[MOUSE_LISTENER STOPPED]]]")

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

def time_me_kl(t):
    time.sleep(t)
    ml.stop()
    print("[[[KEYBOARD_LISTENER STOPPED]]]")

def time_me(t=3):
    time.sleep(t)
    kl.stop()
    ml.stop()

with key_listener(on_press=on_press,on_release=on_release) as kl:
    with mouse_listener(on_click=on_click, on_scroll=on_scroll) as ml:
        time_me(3)
        ml.join()
        kl.join()
