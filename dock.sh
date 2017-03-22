#!/bin/bash

## LTP T410 Arch
#LD="LVDS1" # Laptop Display
#D1="HDMI2" # Display 1
#D2="HDMI3" # Display 2

## LTP T420s Mint
LD="LVDS-1-1" # Laptop Display
D1="DP-1" # Display 1
D2="DP-2" # Display 2
function dock {
        xrandr --output $LD --off
        xrandr --output $D1 --auto
        xrandr --output $D2 --auto --left-of $D1 --primary
        echo '1' > /tmp/dock.save
}

function undock {
        xrandr --output $D1 --off
        xrandr --output $D2 --off
        xrandr --output $LD --auto --primary
        echo '0' > /tmp/dock.save
}

if [ "$1" == "-d" ] ; then
	dock
fi


if [ "$1" == "-u" ] ; then
        undock
fi



if [ "$#" -ne 1 ]; then
    if [ -f /tmp/dock.save ]; then
        value=`cat /tmp/dock.save`
        if [ $value == "1" ]; then
           undock
        else
           dock
        fi
    else
    
	if xrandr | grep "HDMI3 disconnected"; then
		undock
	else
		dock
	fi
    fi
fi

