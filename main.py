import os
import re


def create_screen(_path, screen_name_upper_camel):
    screen_name_snake = upper_camel_to_snake(screen_name_upper_camel)
    parent_dir = os.path.join(_path, screen_name_snake)
    os.makedirs(parent_dir, exist_ok=True)
    print(os.path.join(_path, screen_name_upper_camel))

    screen = open(os.path.join(parent_dir, screen_name_snake + '_screen.dart'), 'w')

    screen.write(
        f"""import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

part '{screen_name_snake}_scaffold.dart';
part '{screen_name_snake}_body.dart';

class {screen_name_upper_camel}Screen extends StatelessWidget {{
  const {screen_name_upper_camel}Screen();

  @override
  Widget build(BuildContext context) {{
    return const _Scaffold();
  }}
}}
""")

    scaffold = open(os.path.join(parent_dir, screen_name_snake + '_scaffold.dart'), 'w')
    scaffold.write(
        f"""part of '{screen_name_snake}_screen.dart';
class _Scaffold extends StatelessWidget {{
  const _Scaffold();

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      //TODO: title here
      appBar: AppBar(
        title: const Text('title'),
      ),
      body: const _Body(),
    );
  }}
}}
""")

    body = open(os.path.join(parent_dir, screen_name_snake + '_body.dart'), 'w')
    body.write(
        f"""part of '{screen_name_snake}_screen.dart';

class _Body extends StatelessWidget {{
  const _Body();

  @override
  Widget build(BuildContext context) {{
    return const SizedBox.shrink();
  }}
}}
""")


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
