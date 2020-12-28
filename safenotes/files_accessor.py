from safenotes.paths import SAFENOTES_DIR_PATH, PASSWORD_FILE_PATH
from safenotes.colors import red, green, yellow, blue
from os.path import isfile, join, basename, dirname
from safenotes.helpers import display_colored_text
from hmac import compare_digest as compare_hash
from os import listdir, system
from getpass import getpass
from crypt import crypt
from typing import List

import os


def ensure_safenotes_dir_exists() -> None:
    """ Creates safenotes directory if it does not exist """
    SAFENOTES_DIR_PATH.mkdir(parents=True, exist_ok=True)


def ensure_safenotes_data_file_exists() -> None:
    """
    Creates safenotes data file (for storing data about
    each note) if it does not exist
    """
    open(str(SAFENOTES_DIR_PATH) + '/data', 'a')


def password_file_exists() -> bool:
    """ Whether the file containing password hash exists or not """
    try:
        open(str(PASSWORD_FILE_PATH), 'r')
    except FileNotFoundError:
        return False
    return True


def define_user_password() -> None:
    """ Prompts user for password and saves its hash on ~/.config/Safenotes/ """
    display_colored_text('It seems you do not have a password yet. Please, define it below.\n', red)
    display_colored_text('Password: ', yellow)
    password = input()
    hashed_passwd = crypt(password)
    with open(str(PASSWORD_FILE_PATH), 'w') as f:
        f.write(hashed_passwd)
    display_colored_text('Password set successfully.\n', green)


def is_file_encrypted(file_path: str) -> bool:
    """
    TODO: look for a better implementation
    Verifies if given file is encrypted
    """
    return '.gpg' in file_path


def encrypt_file(file_path: str, password: str) -> None:
    """ Saves an encrypted version of the file and deletes the original one """
    if is_file_encrypted(file_path):
        raise ValueError('It seems the file is already encrypted.')
    os.system(f'gpg --passphrase \'{password}\' -c --batch {file_path} && shred -u {file_path}')


def decrypt_file(file_path: str, password: str) -> None:
    """
    Saves an unencrypted version of the file and deletes the original (encrypted) one
    """
    if not is_file_encrypted(file_path):
        raise ValueError('It seems the file is not encrypted.')
    os.system(f'gpg --passphrase \'{password}\' --batch {file_path} && rm {file_path}')


def load_user_password() -> str:
    """ Prompts for password until user gets it right (i.e. hashes match) """
    hashed_passwd = open(str(PASSWORD_FILE_PATH), 'r').read()
    display_colored_text('Please, type in your password to have access to your notes.\n', blue)
    display_colored_text('This will not display any data.\n', blue)
    display_colored_text('Password: ', yellow)
    password_typed = getpass('')
    while not compare_hash(hashed_passwd, crypt(password_typed, hashed_passwd)):
        display_colored_text('Wrong password. Please, try again.\n', red)
        display_colored_text('Password: ', yellow)
        password_typed = getpass('')

    return password_typed


def open_os_editor_on_file(file_path: str) -> None:
    """ Opens the default OS editor on a given path. Unless user changed $EDITOR, it should probably be nano """
    os.system(f'{os.getenv("EDITOR")} {file_path}')


def edit_file_and_encrypt(file_path: str, password: str) -> None:
    """ Edits a file and saves an encrypted version of it """
    open_os_editor_on_file(file_path)
    encrypt_file(file_path, password)


def delete_encrypted_file(file_path: str) -> None:
    """ Deletes an encrypted file, or raises error if file is not encrypted. """
    if not is_file_encrypted(file_path):
        raise ValueError('It seems the file is not encrypted.')

    system(f'rm {file_path}')


def rename_encrypted_file(file_path: str) -> str:
    """ Renames an encrypted file, or raises error if file is not encrypted. Returns the new name """
    if not is_file_encrypted(file_path):
        raise ValueError('It seems the file is not encrypted.')

    system('clear')
    file_basename = basename(file_path)
    display_colored_text(
        f'Please decide on a new name for the note. The current name is {file_basename.replace(".gpg", "")}\n',
        blue
    )
    display_colored_text('(This name WILL be publicly accessible): ', red)
    new_name = input()
    if '.gpg' in file_basename and '.gpg' not in new_name:
        # Currently verifying for .gpg is redundant if it verifies for encrypted
        # file, but this may change in the future when the extension .gpg is no
        # longer used.
        new_name += '.gpg'

    system(f'mv {file_path} {dirname(file_path) + "/" + new_name}')
    return new_name


def get_saved_notes_filenames() -> List[str]:
    """ Get all filenames that are stored in .config/Safenotes/ and are not data/password files """
    notes_path = str(SAFENOTES_DIR_PATH)
    filenames = [f for f in listdir(notes_path) if isfile(join(notes_path, f)) and f not in {'data', 'password'}]
    return filenames


def note_full_path(note_name: str) -> str:
    """ Given a note name, returns its full path (i.e. /home/user/.config/.../note) """
    # Operations regarding files do not use built-in Python functions, so spaces
    # must be skipped
    note_name = note_name.replace(' ', '\\ ')
    return str(SAFENOTES_DIR_PATH / note_name)
