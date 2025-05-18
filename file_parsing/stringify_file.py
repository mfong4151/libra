from os.path import splitext

TWO_BACKSLASH = set(['.js', '.tsx', '.ts' , '.css', '.cpp', '.java'])
HASHTAGS = set(['.py', '.rs'])

def clean_file_path(shortened_cwd: str, file_path: str) -> str:
    loc_cwd = file_path.rfind(shortened_cwd)
    return file_path[loc_cwd:]

def file_attrs(shortened_cwd, file_path: str, file_body: str):
    displayed_file_path = clean_file_path(shortened_cwd, file_path)
    _, ext = splitext(file_path)
    comment = '#' if ext in HASHTAGS else '//'
    return '\n'.join([f"{comment}{displayed_file_path}", file_body])


def stringify_file(shortened_cwd: str, file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            return file_attrs(shortened_cwd, file_path, file.read())
    except FileNotFoundError:
        return ''
    except Exception as e:
        return ''

