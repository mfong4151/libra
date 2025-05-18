# Text Formatting:

#     \033[0m: Reset all text attributes (color, bold, underline, etc.) to their default values.
#     \033[4m: Set text to underline.
#     \033[7m: Invert text colors (swap foreground and background colors).

# Background Color:

#     \033[40m: Black background.
#     \033[41m: Red background.
#     \033[42m: Green background.
#     \033[43m: Yellow background.
#     \033[44m: Blue background.
#     \033[45m: Magenta background.
#     \033[46m: Cyan background.
#     \033[47m: White background.

#Text colors
BOLD = "\033[1m"
CYAN = "\033[36m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"


def colorize(target: str, text:str, default:str ='\033[0m') -> str:
    return f"{target}{text}{default}"