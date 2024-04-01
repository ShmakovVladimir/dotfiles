import subprocess
import sys

def replace_string_in_file(file_path, old_str, new_str):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        modified_content = content.replace(old_str, new_str)
        with open(file_path, 'w') as file:
            file.write(modified_content)
        
        print("String replaced successfully!")
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


now_name = open('/home/vladimir/projects/theme-switcher/theme_name.txt').read()
print(now_name)
vs_code_theme_names = {'latte': 'Catppuccin Latte', 
                       'frappe': 'Catppuccin Frappé',
                       'everforest': 'Everforest Dark'}
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

subprocess.run('/home/vladimir/bin/random_wallpaper')
subprocess.run('/home/vladimir/.config/bspwm/bspwmrc')
subprocess.run(['killall', '-USR1', 'kitty'])
with open('/home/vladimir/projects/theme-switcher/theme_name.txt', 'w') as f:
    f.write(new_theme)
