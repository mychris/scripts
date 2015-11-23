#!/bin/sh

xrandr --output LVDS-1 --mode 1280x800 --right-of VGA-1 --output VGA-1 --mode 1920x1080 --primary

[ -x "$HOME/.fehbg" ] && "$HOME/.fehbg"

# arr=(`ps -aux | grep -v grep | grep urxvtd | cut -d " " --output-delimiter=" " -f 1-`)
#
# ( sleep 2 && eval "${arr[@]:10} &") &
# kill ${arr[1]}

# vim: ft=sh ts=2 sts=2 sw=2 et:
