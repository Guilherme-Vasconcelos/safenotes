'''
https://github.com/johnvictorfs/nyaa-cli/blob/master/nyaacli/colors.py

colors.py is a file taken from nyaa-cli: Copyright (c) 2019 John Victor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
'''

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
