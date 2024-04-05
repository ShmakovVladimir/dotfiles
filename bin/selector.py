import subprocess
import sys

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
        raise NotImplementedError("file not found")
    except Exception as e:
        raise NotImplementedError("NotImplemented error")


now_name = open('/home/vladimir/projects/theme-switcher/theme_name.txt').read()
print(now_name)
vs_code_theme_names = {'latte': 'Catppuccin Latte', 
                       'frappe': 'Catppuccin Frappé',
                       'everforest': 'Everforest Dark',
                       'tokio-night': 'Tokyo Night'}
new_theme = sys.argv[1]
path_to_polybar = r"/home/vladimir/.config/polybar/nord-top"
path_to_polybar_2 = r"/home/vladimir/.config/polybar/bars/separate-bars"
old_str = f"colors-{now_name}"
new_str = f"colors-{new_theme}"
replace_string_in_file(path_to_polybar, old_str, new_str)
replace_string_in_file(path_to_polybar_2, old_str, new_str)
replace_string_in_file('/home/vladimir/.config/bspwm/bspwmrc', now_name, new_theme)
replace_string_in_file('/home/vladimir/.config/kitty/kitty.conf', now_name, new_theme)
replace_string_in_file('/home/vladimir/.config/rofi/config.rasi', now_name, new_theme)
replace_string_in_file('/home/vladimir/.config/Code/User/settings.json',
                       vs_code_theme_names[now_name.replace('\n', '')], 
                       vs_code_theme_names[new_theme.replace('\n', '')])
replace_string_in_file('/home/vladimir/.config/zathura/zathurarc', now_name, new_theme)
replace_string_in_file('/home/vladimir/bin/random_wallpaper', now_name, new_theme)
replace_string_in_file('/home/vladimir/.var/app/org.mozilla.firefox/.mozilla/firefox/4fu5mgjd.default-release/chrome/includes/cascade-colours.css',
                        now_name, 
                        new_theme)
replace_string_in_file('/home/vladimir/.var/app/org.mozilla.firefox/.mozilla/firefox/4fu5mgjd.default-release/chrome/userContent.css',
                        now_name, 
                        new_theme)

subprocess.run('/home/vladimir/bin/random_wallpaper')
subprocess.run('/home/vladimir/.config/bspwm/bspwmrc')
subprocess.run(['killall', '-USR1', 'kitty'])
with open('/home/vladimir/projects/theme-switcher/theme_name.txt', 'w') as f:
    f.write(new_theme)
