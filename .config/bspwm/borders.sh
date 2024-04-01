while bspc subscribe -c 1 node_focus; do
    bspc config focused_border_color "#a6d189"
    bspc config normal_border_color "#a6d189"
    bspc config active_border_color "#a6d189"
    bspc config border_width 0
    bspc config -n focused border_width 3
    bspc config focused_border_color "#a6d189"
    bspc config normal_border_color "#a6d189"
    bspc config active_border_color "#a6d189"

done
