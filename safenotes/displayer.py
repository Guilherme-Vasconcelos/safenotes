from safenotes.helpers import display_colored_text
from safenotes.paths import SAFENOTES_DIR_PATH
from safenotes.colors import red, blue
from typing import Callable, Dict
from os import system
from sys import exit

import safenotes.files_accessor as files_accessor
import questionary


class Displayer:
    """
    Class for displaying all notes, handling user action, etc.
    """
    def __init__(self, password: str) -> None:
        self.password = password

    def display(self) -> None:
        """ Used to display all notes and allowing user to create new ones, edit existing, etc. """
        system('clear')

        special_choices = ['New note', 'Quit', 'Refresh encryptions']
        choice = questionary.select(
            'Available notes',
            choices=special_choices + files_accessor.get_saved_notes_filenames(),
            qmark=''
        ).ask()

        self.handle_choice(choice)

    def create_new_note(self) -> None:
        """ Creates a new note and encrypts it """
        display_colored_text('Please decide on a name for the file ', blue)
        display_colored_text('(this name WILL be publicly accessible): ', red)
        file_name = input()
        file_name = file_name.replace(' ', '\\ ')
        note_path = str(SAFENOTES_DIR_PATH / file_name)
        files_accessor.edit_file_and_encrypt(note_path, self.password)
        self.display()

    def edit_note(self, note_path: str) -> None:
        """ Unencrypts a note, allows user to edit it, then encrypts it again """
        if not files_accessor.is_file_encrypted(note_path):
            raise ValueError('It seems you are trying to edit an unencrypted file. ' +
                             'Please, consider refreshing the encryptions.')
        files_accessor.decrypt_file(note_path, self.password)
        note_path = note_path.replace('.gpg', '')
        files_accessor.edit_file_and_encrypt(note_path, self.password)
        self.display()

    def refresh_encryptions(self) -> None:
        files_to_encrypt = [
            f for f in files_accessor.get_saved_notes_filenames() if not files_accessor.is_file_encrypted(f)
        ]

        for file in files_to_encrypt:
            file_path = str(SAFENOTES_DIR_PATH / file)
            files_accessor.encrypt_file(file_path, self.password)
        self.display()

    def handle_choice(self, choice: str) -> None:
        """ Call the correct method based on user's input """
        available_choices: Dict[str, Callable] = {
            'New note': self.create_new_note,
            'Quit': exit,
            'Refresh encryptions': self.refresh_encryptions
        }

        if choice in available_choices:
            available_choices[choice]()
        else:  # Else is assumed to be edit action, choice is the file name
            choice = choice.replace(' ', '\\ ')
            self.edit_note(str(SAFENOTES_DIR_PATH / choice))
