#!/bin/bash

# options to be displayed
option0="frappe"
option1="latte"
option2="everforest"
# options passed into variable
options="$option0\n$option1\n$option2"

chosen="$(echo -e "$options" | rofi -lines 3 -dmenu -p "theme")"
python3 /home/vladimir/bin/selector.py $chosen
