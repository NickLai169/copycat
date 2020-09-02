import pyautogui
import time
import os
import sys
from functions import *

function_map = {
"record": record,
"perform": perform
}
"===================[MAIN FUNCTION(S)]==================="
def main():
    if sys.argv[1] not in function_map:
        raise Exception("INCORRECT FUNCTION NAME")

    function_to_run = function_map[sys.argv[1]]
    inputs = sys.argv[2:]

    function_to_run(inputs)

if __name__ == "__main__":
    main()
