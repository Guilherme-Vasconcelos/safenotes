# Usage

Hello! Here you will find everything about Safenotes usage.
If you have not yet installed it, please refer to docs/INSTALLATION.md.

---

### Table of contents

- [Safenotes for the first time](#safenotes-for-the-first-time)
- [Precautions](#precautions)

---

### Safenotes for the first time

In order to run Safenotes, you must use the command: `python3 safenotes.py`

If it is your first time using Safenotes, it will ask you to define a password.
Make sure you pick a password you will remember, because recovering it is not
possible without losing access to your notes.

You can choose anything to be your password, but it is recommended
that it is at least 16 characters long.

# Precautions

Although you are able to edit notes manually without using the safenotes script,
this is highly unadvisable, as it could lead to corruption.
For instance, safenotes will use the file name for date of creation reference,
so if you manually rename the note, safenotes will no longer be able to tell
when it was created.
