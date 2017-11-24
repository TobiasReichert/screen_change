#!/usr/bin/python

import sys
import os
import subprocess

LD = "LVDS-1-1" # Laptop Display
D1 = "DP-1"     # Display 1
D2 = "DP-2"     # Display 2

temp_file = "/tmp/dock.save"

def dock():
    os.system("xrandr --output " + LD + " --off")
    os.system("xrandr --output " + D1 + " --auto")
    os.system("xrandr --output " + D2 + " --auto --left-of " + D1 + " --primary")
    open(temp_file, "w").write("1")

def undock():
    os.system("xrandr --output " + D1 + " --off")
    os.system("xrandr --output " + D2 + " --off")
    os.system("xrandr --output " + LD + " --auto --primary")
    open(temp_file, "w").write("0")

def is_docked():
    """
    Checks if a external display is connected
    """
    output = subprocess.check_output("xrandr")
    return not D2 + " disconnected" in output

def decide():
    # if Display is disconnected undock
    if not is_docked():
        undock()
        return
    # if file not exits
    if not os.path.isfile(temp_file):
        # check docked
        if is_docked():
            dock()
        else:
            undock()
        return
    # read the temp file 
    value = open(temp_file, "r").read()
    if value == "1":
        undock()
        return
    else:
        dock()
        return

def main():
    if len(sys.argv) == 1:
        decide()
    else:
        if sys.argv[1] == "-d":
            dock()
        elif sys.argv[1] == "-u":
            undock()
        else:
            print("ERROR: wrong arg")

if __name__ == "__main__":
    main()
