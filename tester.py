import pyautogui
import time
import os
import sys

from multiprocessing import Process

from pynput.mouse import Listener as mouse_listener
from pynput.keyboard import Listener as key_listener
from pynput import keyboard
from pynput.keyboard import Key

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

dir_path = os.path.dirname(os.path.realpath(__file__))
sep = os.sep
screen_dim = pyautogui.size()

import pickle

lower_half_screen = (0, int(screen_dim[1]/2), screen_dim[0], int(screen_dim[1]/2))
centre_screen = (int(screen_dim[0]/3), int(screen_dim[1]/3), int(screen_dim[0]/3), int(screen_dim[1]/3))


"""
[TESTING BEGINS]
"""
class John:
    me = "Henderson"

def func1():
    for i in range(10):
        print(i)
        time.sleep(1)

def func2(pip):
    time.sleep(2)
    if pip == 1:
        print("pop")
    else:
        print(pip)
        func2(pip/2)

# if __name__ == '__main__':
#     p1 = Process(target=func1)
#     p2 = Process(target=func2, args=[16])
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

# hon = John()
# hon.burger = "ferret"
# pickle.dump(hon, open("save.p", "w+b"))

print("heurrgg")
