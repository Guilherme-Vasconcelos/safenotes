At the moment, installation is a little inconvenient, but it will be better
once the package is published.

Right now, in order to use Safenotes you must:

1. [Install Poetry](https://python-poetry.org/docs/#installation), which is used for managing dependencies.
2. Clone the repository: `git clone https://github.com/Guilherme-Vasconcelos/safenotes`
3. Change into the repository's directory: `cd safenotes`
4. Create a virtual environment in which dependencies will be installed: `python3 -m venv .venv`
5. Source the local Python (should be done automatically by most IDEs. If not,
run `source .venv/bin/activate`).
6. Install all dependencies: `poetry install`. It is recommended to run this command
even if the dependencies have are already been previously installed, since it will create
the `safenotes` command.
7. Run Safenotes with: `safenotes`. This requires the virtual environment to be activated.
If you wish to run it manually instead, you can do so with `python3 safenotes/cli/__init__.py`.
