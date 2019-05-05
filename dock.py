#!/usr/bin/python

import sys
import os
import subprocess

LD = "LVDS1"    # Laptop Display
D1 = "HDMI2"    # Display 1
D2 = "HDMI3"    # Display 2

temp_file = "/tmp/dock.save"


def dock():
    os.system("xrandr --output " + LD + " --off")
    os.system("xrandr --output " + D1 + " --auto")
    os.system("xrandr --output " + D2 + " --auto --left-of " + D1 + " --primary")
    os.system("xrandr --dpi 96")
    open(temp_file, "w").write("1")


def undock():
    os.system("xrandr --output " + D1 + " --off")
    os.system("xrandr --output " + D2 + " --off")
    os.system("xrandr --output " + LD + " --auto --primary")
    os.system("xrandr --dpi 96")
    open(temp_file, "w").write("0")


def init():
    os.system('xrandr --newmode "1600x1200_60.00"  161.00  1600 1712 1880 2160  1200 1203 1207 1245 -hsync +vsync')
    os.system('xrandr --addmode HDMI2 "1600x1200_60.00"')
    os.system('xrandr --output HDMI2 --mode "1600x1200_60.00"')


def is_docked():
    """
    Checks if a external display is connected
    """
    output = subprocess.check_output("xrandr")
    return not D2 + " disconnected" in output


def decide():
    # init if temp_file not exists
    if not os.path.isfile(temp_file):
        init()

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
        elif sys.argv[1] == "-i":
            init()
        else:
            print("ERROR: wrong arg")

if __name__ == "__main__":
    main()
