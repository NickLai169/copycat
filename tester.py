import pyautogui
import time
import os
import sys
import pickle

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
recordings_path = dir_path + sep + "recordings"
screen_dim = pyautogui.size()

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

file = open(recordings_path + sep + "a_z.p", "r+b")
lists = pickle.load(file)

print(lists)

def do_tasks(lst_pair):
    task_lst = lst_pair[0]
    time_lst = lst_pair[1]

    for task in task_lst:
        bot = keyboard.Controller()
        bot.press(task)
        print("bot presses: " + str(task))
        time.sleep(1)

    for task in task_lst:
        bot.release(task)
        print("bot releases: " + str(task))

# do_tasks(lists)
print("DONEZO")


def hello(a):
    print(a)
    print("hello world")

lst = [1, 2, 3, 4]

exec("print(lst)")

def time_me(t, l):
    time.sleep(t)
    l.stop()

def on_activate():
    print('Global hotkey activated!')

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    on_activate)

def for_canonical(hotkeyfunc):
    def retfunc(input):
        print(input)
        print(type(input))
        if True:
            return hotkeyfunc(l.canonical(input))
        else:
            print(str(input))
    # if True:
    #     return lambda k: hotkeyfunc(l.canonical(k))
    # else:
    #     print(str(hotkeyfunc))
    return retfunc

with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    time_me(5, l)
    l.join()
