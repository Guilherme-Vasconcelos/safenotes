from colors import red
import files_accessor


def main():
    files_accessor.ensure_safenotes_dir_exists()

    if not files_accessor.password_file_exists():
        print(red('It seems you do not have a password yet.'))
        print('Please, define it below:')
        files_accessor.define_user_password()

    print(files_accessor.load_user_password())


if __name__ == "__main__":
    main()
