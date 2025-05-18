from typing import List
from utils.colorize import colorize, BOLD, BLUE
def display_config(config):
        headers = f'{BOLD}{BLUE}'
        folders = colorize(headers, 'Ignored Folders')
        files = colorize(headers, 'Ignored Files')
        print(folders)
        display(config['ignored_folders'])
        print(files)
        display(config['ignored_files'])
        return

def display(arr: List[str]):
    for i in arr:
        print(f"{i}")
        