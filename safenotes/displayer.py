from os import listdir, system
from os.path import isfile, join
from paths import SAFENOTES_DIR_PATH
from typing import List
from sys import exit
import os
import questionary

# TODO: add docstrings

class Displayer:
    """
    Class for displaying all notes, keybinds, handling user action, etc.
    """

    def __init__(self, password: str):
        self.password = password

    def display(self) -> None:
        system('clear')

        special_choices = ['New note', 'Quit']
        choice = questionary.select(
            'Available notes',
            choices=special_choices + self.get_saved_notes_filenames(),
            qmark=''
        ).ask()

        self.handle_choice(choice)

    def create_new_note(self) -> None:
        file_name = input('Please decide on a name for the file (this name WILL be publicly visible): ')
        system(f'{os.getenv("EDITOR")} {str(SAFENOTES_DIR_PATH / file_name)}')
        self.display()

    def edit_note(self, note_path: str) -> None:
        system(f'{os.getenv("EDITOR")} {note_path}')
        self.display()

    def handle_choice(self, choice: str) -> None:
        available_choices = {
            'New note': self.create_new_note,
            'Quit': exit
        }

        if choice in available_choices:
            available_choices[choice]()
        else:  # Else is assumed to be edit action
            if ' ' in choice:
                choice = choice.replace(' ', '\\ ')
            self.edit_note(str(SAFENOTES_DIR_PATH / choice))

    @staticmethod
    def get_saved_notes_filenames() -> List[str]:
        notes_path = str(SAFENOTES_DIR_PATH)
        filenames = [f for f in listdir(notes_path) if isfile(join(notes_path, f)) and f not in {'data', 'password'}]
        return filenames
