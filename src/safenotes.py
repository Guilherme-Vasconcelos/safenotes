import files_accessor


def main():
    files_accessor.ensure_safenotes_dir_exists()

    if not files_accessor.password_file_exists():
        files_accessor.define_user_password()

    print(files_accessor.load_user_password())


if __name__ == "__main__":
    main()
