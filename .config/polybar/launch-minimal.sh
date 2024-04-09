#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done
echo "all killed..."


polybar -c $HOME/.config/polybar/bars/minimal nord-top&

if [[ $(xrandr -q | grep 'DP-1 connected') ]]; then
	polybar -c $HOME/.config/polybar/bars/minimal nord-top-second_monitor&
fi

echo "Bars launched..."
