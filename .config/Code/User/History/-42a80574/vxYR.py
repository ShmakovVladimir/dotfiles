import os


def replace_string_in_file(file_path, old_str, new_str):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Replace the string
        modified_content = content.replace(old_str, new_str)
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)
        
        print("String replaced successfully!")
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
now_name = open('theme_name.txt').read()
print(now_name)
vs-code-theme-names = {'latte': 'Catppuccin Latte', 'frappe': 'Catpuccin Frappe'}
new_theme = input("new theme: ")
path_to_polybar = r"/home/vladimir/.config/polybar/nord-top"
path_to_polybar_2 = r"/home/vladimir/.config/polybar/bars/separate-bars"
old_str = f"colors-{now_name}"
new_str = f"colors-{new_theme}"
replace_string_in_file(path_to_polybar, old_str, new_str)
replace_string_in_file(path_to_polybar_2, old_str, new_str)
replace_string_in_file('/home/vladimir/.config/kitty/kitty.conf', now_name, new_theme)
replace_string_in_file('/home/vladimir/.config/rofi/config.rasi', now_name, new_theme)
with open('theme_name.txt', 'w') as f:
    f.write(new_theme)