#!/usr/bin/env python3

from safenotes.displayer import Displayer
from safenotes import files_accessor


def main():
    files_accessor.ensure_safenotes_dir_exists()
    files_accessor.ensure_safenotes_data_file_exists()

    if not files_accessor.password_file_exists():
        files_accessor.define_user_password()

    password = files_accessor.load_user_password()
    displayer = Displayer(password)
    displayer.display_initial_menu()


if __name__ == "__main__":
    main()
