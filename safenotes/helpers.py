from typing import Callable


def display_colored_text(text: str, color: Callable) -> None:
    """ Displays the colored text without newline """
    print(color(text), end='', flush=True)
