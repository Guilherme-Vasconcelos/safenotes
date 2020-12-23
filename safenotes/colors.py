from colorama import init, Fore, Style

init()


def red(text: str) -> str:
    return Fore.RED + text + Style.RESET_ALL


def green(text: str) -> str:
    return Fore.GREEN + text + Style.RESET_ALL


def yellow(text: str) -> str:
    return Fore.YELLOW + text + Style.RESET_ALL


def blue(text: str) -> str:
    return Fore.BLUE + text + Style.RESET_ALL
