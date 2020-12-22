import os
from hmac import compare_digest as compare_hash
from paths import SAFENOTES_DIR_PATH, PASSWORD_FILE_PATH
from crypt import crypt
from colors import red, green


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
        open(PASSWORD_FILE_PATH, 'r')
    except FileNotFoundError:
        return False
    return True


def define_user_password() -> None:
    print(red('It seems you do not have a password yet.'))
    print('Please, define it below:')
    password = input('>>>')
    hashed_passwd = crypt(password)
    with open(PASSWORD_FILE_PATH, 'w') as f:
        f.write(hashed_passwd)
    print(green('Password set successfully.'))


def encrypt_file(file_path: str, password: str) -> None:
    """
    Saves an encrypted version of the file and deletes the original one
    """
    os.system(f'gpg --passphrase \'{password}\' -c --batch {file_path} && shred -u {file_path}')


def decrypt_file(file_path: str, password: str) -> None:
    """
    Saves an unencrypted version of the file and deletes the original (encrypted) one
    """
    os.system(f'gpg --passphrase \'{password}\' --batch {file_path} && rm {file_path}')


def load_user_password() -> str:
    """
    Prompts for password until user gets it right (i.e. hashes match)
    """
    hashed_passwd = open(PASSWORD_FILE_PATH, 'r').read()
    print('Please, type in your password to have access to your notes:')
    password_typed = input('>>>')
    while not compare_hash(hashed_passwd, crypt(password_typed, hashed_passwd)):
        print(red('Wrong password. Please, try again.'))
        password_typed = input('>>>')

    return password_typed
