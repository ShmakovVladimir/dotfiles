#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done
echo "all killed..."

#polybar -c $HOME/.config/polybar/bars/dark-config nord-top-left &
#polybar -c $HOME/.config/polybar/bars/dark-config nord-top-center& 
#polybar -c $HOME/.config/polybar/bars/dark-config nord-top-right&
#polybar -c $HOME/.config/polybar/bars/dark-config nord-top&
polybar -c $HOME/.config/polybar/bars/separate-bars run&
polybar -c $HOME/.config/polybar/bars/separate-bars bspwm&
polybar -c $HOME/.config/polybar/bars/separate-bars power&
polybar -c $HOME/.config/polybar/bars/separate-bars ai&
polybar -c $HOME/.config/polybar/bars/separate-bars clock&
polybar -c $HOME/.config/polybar/bars/separate-bars info&
#polybar -c $HOME/.config/polybar/bars/separate-bars music&


if [[ $(xrandr -q | grep 'DP-1 connected') ]]; then
 # polybar -c $HOME/.config/polybar/bars/dark-config nord-top-rounded-second 
 # polybar -c $HOME/.config/polybar/bars/dark-config nord-top-left-monitor &
 # polybar -c $HOME/.config/polybar/bars/dark-config nord-top-center-monitor& 
 # polybar -c $HOME/.config/polybar/bars/dark-config nord-top-right-monitor&
   polybar -c $HOME/.config/polybar/bars/separate-bars run-second&
polybar -c $HOME/.config/polybar/bars/separate-bars bspwm-second&
polybar -c $HOME/.config/polybar/bars/separate-bars power-second&
polybar -c $HOME/.config/polybar/bars/separate-bars ai-second&
polybar -c $HOME/.config/polybar/bars/separate-bars clock-second&
polybar -c $HOME/.config/polybar/bars/separate-bars info-second&

fi

echo "Bars launched..."
