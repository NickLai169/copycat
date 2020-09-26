import pyautogui
import time
import os
import sys
from functions import *

function_map = {
"record": record,
"perform": perform,
"record_serial": record_serial,
}
"===================[MAIN FUNCTION(S)]==================="


def main():
    # if sys.argv[1] not in function_map:
    #     raise Exception("INCORRECT FUNCTION NAME")

    try:

        # function_to_run = function_map[sys.argv[1]]
        # inputs = sys.argv[2:]

        # function_to_run(inputs)
        exec(sys.argv[1] + "(sys.argv[2:])")
    except NameError:
        raise Exception("INCORRECT FUNCTION NAME 2.0")

if __name__ == "__main__":
    main()
