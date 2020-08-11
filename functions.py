import pyautogui
import time
import os
import sys

def record(args):
    duration = 10
    if args != []:
        duration = float(args[0])
    
