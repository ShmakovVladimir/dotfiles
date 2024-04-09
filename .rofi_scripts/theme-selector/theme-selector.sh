#!/bin/bash

# options to be displayed
#
function exists_in_list() {
    LIST=$1
    DELIMITER=$2
    VALUE=$3
    LIST_WHITESPACES=`echo $LIST | tr "$DELIMITER" " "`
    for x in $LIST_WHITESPACES; do
        if [ "$x" = "$VALUE" ]; then
            return 0
        fi
    done
    return 1
}
option0="frappe"
option1="latte"
option2="everforest"
option3="tokio-night"
option4="rose-pine-dawn"
option5="rose-pine"
themes="$option0 $option1 $option2 $option3 $option4 $option5"
# options passed into variable
options="$option0\n$option1\n$option2\n$option3\n$option4\n$option5"

chosen="$(echo -e "$options" | rofi -lines 3 -dmenu -p "theme")"

if exists_in_list "$themes" " " $chosen; then
	python3 /home/vladimir/bin/selector.py $chosen
fi
