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


#>>> first line

height = 6

first_line = (("*"*10) * height)+"*"


# TEMP DON'T STEAL
print(first_line)

def second_line(width):
    stern = "*"
    space = " "
    second_line = ((stern + space *9)*width)+stern
    while width >0:
        print(second_line)
        width -= 1

second_line(height)

print(first_line)

second_line(height)
print(first_line)
second_line(height)
print(first_line)