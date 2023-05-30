import os
import shutil


def make_sim(parameters: dict, source_dir: str, main_dir: str):

    text = '*KEYWORD\n*PARAMETER\n'
    new_dir_name = 'drop_'

    for key in parameters.keys():
        newline = f'R {key:<8}{parameters[key]:>8}\n'
        new_dir_name += f'{key}{parameters[key]}_'
        text += newline

    text += '*END\n'
    new_dir_name += 'sim'

    new_dir = os.path.join(main_dir, new_dir_name)
    os.makedirs(new_dir, exist_ok=True)

    for filename in os.listdir(source_dir):
        old_path = os.path.join(source_dir, filename)
        new_path = os.path.join(new_dir, filename)
        print(new_path)
        shutil.copy2(old_path, new_path)

    with open(os.path.join(new_dir, 'Parameter.k'), 'w') as my_text:
        my_text.write(text)  # save text file


