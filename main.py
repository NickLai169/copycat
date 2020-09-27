import pyautogui
import time
import os
import sys
from functions import *
from settings import *

function_map = {
"record": record,
"perform": perform,
"record_serial": record_serial,
"update_settings": update_settings,
"restore_defaults": restore_defaults,
"show_defaults": show_defaults,
}
"===================[MAIN FUNCTION(S)]==================="


def main():
    # if sys.argv[1] not in function_map:
    #     raise Exception("INCORRECT FUNCTION NAME")

    try:

        # function_to_run = function_map[sys.argv[1]]
        # inputs = sys.argv[2:]

        # function_to_run(inputs)
        if len(sys.argv) > 2:
            exec(sys.argv[1] + "(sys.argv[2:])")
        else:
            exec(sys.argv[1] + "()")
    except NameError:
        print("Incorrect function name")
    except TypeError:
        print("Invalid inputs")
    except:
        print(sys.exc_info()[0])

if __name__ == "__main__":
    main()
