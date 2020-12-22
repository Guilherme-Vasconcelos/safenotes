from os import listdir, system
from os.path import isfile, join
from paths import SAFENOTES_DIR_PATH
from typing import List
import questionary


class Displayer:
    """
    Class for displaying all notes, keybinds, handling user action, etc.
    """

    def __init__(self, password):
        self.password = password

    def display(self):
        system('clear')

        # TODO: also display date if available and unencrypted/encrypted
        questionary.select(
            'Available notes',
            choices=self.get_saved_notes_filenames()
        ).ask()

    @staticmethod
    def get_saved_notes_filenames() -> List[str]:
        notes_path = str(SAFENOTES_DIR_PATH)
        filenames = [f for f in listdir(notes_path) if isfile(join(notes_path, f)) and f not in {'data', 'password'}]
        return filenames
