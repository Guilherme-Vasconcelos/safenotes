At the moment, installation is a little inconvenient, but it will be better
once the package is published.

Right now, in order to use Safenotes you must:

0. [Install Poetry](https://python-poetry.org/docs/#installation), which is used for managing dependencies.
1. Clone the repository: `git clone https://github.com/Guilherme-Vasconcelos/safenotes`
2. Change into the repository's directory: `cd safenotes`
3. Create a virtual environment in which dependencies will be installed
(make sure you're using Python 3.8 or greater): `python3 -m venv .venv`
4. Source the local Python (should be done automatically by most IDEs. If not,
run `source .venv/bin/activate`).
5. Install all dependencies: `poetry install`
6. Run Safenotes with: `python src/safenotes.py`.
