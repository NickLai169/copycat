import sys

"""
Here are the original default settings that come with the project. Please don't
tamper with these, to reset settings please go to Settings.py
NOTE: If anything goes wrong with hte settings file, then feel free to get the
defaults from here.
"""
PYAUTOGUI_FAILSAFE_STATUS = True
PYAUTOGUI_PAUSE_DURATION = 0.5

RECORD_DURATION = 3
RECORD_DELAY = 0


"""
Script that updates the defaults according to the settings file.
"""
def load_settings():
    try:
        f = open(".settings", "r")
        all_lines = f.readlines()
        for i in all_lines:
            exec(i)
        f.close()
    except:
        print("Unexpected error: ", sys.exc_info()[0])
        while True:
            response = input("Would you like to perform a settings reset? (y/n)")
            if response.upper() == "Y":
                restore_defaults()
                print("Function run attempt exited")
                return
            elif response.upper() == "N":
                print("load_settings attempt aborted, exiting function")
                return
            else:
                print("Sorry, {0} is not a valid input.".format(response))


"""
Script that updates the settings within the .settings file.
@param args:
    - setting_name: The name of the setting default we're trying to overwrite
    - setting_value: The new value of said parameter
"""
def update_settings(args):
    setting_name = args[0]
    setting_value = args[-1]
    if len(args) > 2:
        print("too many arguments")
        return
    f = open(".settings", "r")
    all_lines = f.readlines()
    setting_found = False
    for i in range(len(all_lines)):
        if setting_name in all_lines[i]:
            try:
                if type(eval(all_lines[i].split()[-1])) != type(eval(setting_value)):
                    print("Invalid setting type {0} into {1}".format(str(type(eval(setting_value)))[7:-1]
                        , str(type(eval(all_lines[i].split()[-1])))[7:-1]))
                    return
            except NameError:
                print("Invalid setting type 'string' into {0}".format(str(type(eval(all_lines[i].split()[-1])))[7:-1]))
                return
            all_lines[i] = "".join([setting_name, " = ",  setting_value, "\n"])
            setting_found = True
            print("".join([setting_name, " updated to: ",  setting_value]))
            break
    f.close()
    if not setting_found:
        print('Setting name "{0}" not found!'.format(setting_name))
        return
    f = open(".settings", "w")
    f.writelines(all_lines)
    f.close()


"""
Restore the original default settings.
"""
def restore_defaults():
    f = open(".settings", "w")
    default_settings = [ \
    "PYAUTOGUI_FAILSAFE_STATUS = True\n",
    "PYAUTOGUI_PAUSE_DURATION = 0.5\n",
    "RECORD_DURATION = 3\n",
    "RECORD_DELAY = 0\n"]
    f.writelines(default_settings)
    f.close()
    print("Default settings restored")


"""
Shows all the current default settings.
"""
def show_defaults():
    f = open(".settings", "r")
    print(f.read())
    f.close()


####Functions that should run on startup
load_settings()
