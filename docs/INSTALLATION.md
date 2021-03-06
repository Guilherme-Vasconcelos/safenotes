# Installation

### Automatic installation instructions

- To install the latest version:
`python3 -m pip install git+git://github.com/Guilherme-Vasconcelos/safenotes --user`
- If you wish to install a specific version instead:
`python3 -m pip install git+git://github.com/Guilherme-Vasconcelos/safenotes/tree/<tag> --user`
- After installing, you can launch safenotes with: `safenotes`

### Manual installation instructions

1. [Install Poetry](https://python-poetry.org/docs/#installation), which is used for managing
dependencies. Please remember to install Poetry with Python 3, because Safenotes
is not compatible with Python 2.
2. Clone the repository: `git clone https://github.com/Guilherme-Vasconcelos/safenotes`
3. Change into the repository's directory: `cd safenotes`
4. Create a virtual environment in which dependencies will be installed: `python3 -m venv .venv`
5. Source the local Python (should be done automatically by most
IDEs and text editors. If not, run `source .venv/bin/activate`). You can
make sure you have sourced the local Python with the command `which python3`,
which must output something like this: `/home/your_user/path/to/safenotes/.venv/bin/python3`.
If it outputs something like `/usr/bin/python3` instead, it means the local Python3
is **not** sourced.
6. Install all dependencies: `poetry install`. It is recommended to run this command
even if the dependencies have are already been previously installed, since it will create
the `safenotes` command.
7. Run Safenotes with: `safenotes`. This requires the virtual environment to be
activated (again, you can check if it is with `which python3`).
If you wish to run it manually instead, you can do so with `python3 safenotes/cli/__init__.py`.

[<- Go back to prerequisites](PREREQUISITES.md) | [Proceed to usage ->](USAGE.md)
