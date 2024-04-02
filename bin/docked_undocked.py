#!/usr/bin/ python3


def replace_string_in_file(file_path: str, old_str: str, new_str: str) -> None:
    """

    Args:
        file_path (str): file path
        old_str (str): old string
        new_str (str): new string
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        modified_content = content.replace(old_str, new_str)
        with open(file_path, 'w') as file:
            file.write(modified_content)
    except FileNotFoundError:
        raise FileNotFoundError("file not found")
    except Exception as e:
        raise NotImplementedError("NotImplemented error")



bspwm_config_path = r"/home/vladimir/.config/bspwm/bspwmrc"
undocked_config_string = 'bspc monitor eDP-1 -d 1 2 3 4 5 6 7'
docked_config_string = 'bspc monitor eDP-1 -d 1\nbspc monitor DP-1 -d 2 3 4 5 6 7'
docked = False
with open(bspwm_config_path) as bspwm_config:
    docked = not bool(sum([undocked_config_string in line for line in bspwm_config]))


if docked:
    replace_string_in_file(bspwm_config_path, docked_config_string, undocked_config_string)
else:
    replace_string_in_file(bspwm_config_path, undocked_config_string, docked_config_string)

