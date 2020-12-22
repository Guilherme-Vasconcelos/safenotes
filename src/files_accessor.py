from pathlib import Path
from colors import red
from crypt import crypt

SAFENOTES_DIR_PATH = Path('~/.config/Safenotes/').expanduser()
PASSWORD_FILE_PATH = str(SAFENOTES_DIR_PATH / 'password')


def ensure_safenotes_dir_exists() -> None:
    """ Creates safenotes directory if it does not exist """
    SAFENOTES_DIR_PATH.mkdir(parents=True, exist_ok=True)


def password_file_exists() -> bool:
    """ Whether the file containing password hash exists or not """
    try:
        open(PASSWORD_FILE_PATH, 'r')
    except FileNotFoundError:
        return False
    return True


def define_user_password() -> None:
    """
    Defines a password for the user.
    Caller must decide whether this really must be done.
    """
    print(red('It seems you do not have a password yet.'))
    print('Please, define it below:')

    password = input('>>>')
    hashed_passwd = crypt(password)
    with open(PASSWORD_FILE_PATH, 'w') as f:
        f.write(hashed_passwd)
