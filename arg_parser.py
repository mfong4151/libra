import argparse

parser = argparse.ArgumentParser(description="Makes copy pasting file contents for chatGPT easier")
parser.add_argument('--config', '-c', action='store_true', help='Displays the contents of the config file')
parser.add_argument('--ignore_files', '-ifi', help="Adds folders to ignore")
parser.add_argument('--ignore_folders', '-ifo', help="Adds folders to ignore")
parser.add_argument('--tree', '-t', action='store_true', help='Creates a tree diagram of the file structure.')
parser.add_argument("--sanitize", "-s", action="store_true", help="Sanitizes and copies items to the clipboard based on the config file.")