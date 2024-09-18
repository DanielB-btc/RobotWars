def user_name(name):
    return name


def ui_input(width, height):
    return width, height


temp_name = input("Enter your name")
temp_ui_width = input("Width")
temp_ui_height = input("Height")

user_name = user_name(temp_name)
ui_scale = ui_input(temp_ui_width, temp_ui_height)

print(user_name, ui_scale)