import os
import re


def create_screen(_path, screen_name_upper_camel):
    screen_name_snake = upper_camel_to_snake(screen_name_upper_camel)
    parent_dir = os.path.join(_path, screen_name_snake)
    os.makedirs(parent_dir, exist_ok=True)
    print(os.path.join(_path, screen_name_upper_camel))

    screen = open(os.path.join(parent_dir, screen_name_snake + '_screen_controller.dart'), 'w')

    screen.write("// TODO:implementation")

    state = open(os.path.join(parent_dir, screen_name_snake + '_screen_state.dart'), 'w')
    state.write("// TODO:implementation")


def upper_camel_to_snake(upper_camel):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake = pattern.sub('_', upper_camel).lower()
    return snake


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = input('親ディレクトリの絶対パスは?')
    screenName = input('スクリーンの名前は?（アッパーキャメル、Screenは入れない）例) HogeHogeScreenならHogeHoge')
    create_screen(path, upper_camel_to_snake(screenName))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
