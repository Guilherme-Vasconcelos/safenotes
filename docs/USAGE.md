# Usage

If you have not yet installed Safenotes, please refer to docs/INSTALLATION.md.

Safenotes is a work in progress, so not all features are available yet. More
things will be added here once they are implemented.

---

### Table of contents

- [Safenotes for the first time](#safenotes-for-the-first-time)
- [Precautions](#precautions)
- [Creating or editing notes](#creating-or-editing-notes)
- [Refresh encryptions](#refresh-encryptions)

---

### Safenotes for the first time

After following the installation steps, you can use the command `safenotes`
to run the program. If you went with the manual installation, you must make
sure your virtual environment is activated, otherwise you will not have the
dependencies and the `safenotes` command. If you see an unrecognized command
error, please refer to docs/INSTALLATION.md.

After that, it will ask you to define a password. Make sure you pick one you
will remember, because recovering it is not possible without losing access
to your notes, the reason being this is the passphrase which will be used to
encrypt the notes.

### Precautions

- After you finish editing your note, you must save it and leave the text editor.
If you close your terminal without leaving the text editor, the note will NOT
be encrypted. Refer to [Refresh encryptions](#refresh-encryptions) for more details.

### Creating or editing notes

After you've been prompted for your password and "logged in", you can:

- Create new notes by selecting the "New note" button
- Edit current notes by selecting the note

Once you select one of these two options, your system's default editor will open.
If you have not customized the EDITOR environment variable, it will probably
be nano. You can save your text with ctrl s and quit the editor with ctrl x.
Then you will be back to Safenotes' menu, in which you will be able to quit if
you want. Be careful not to close the terminal without quiting safenotes first,
as this can currently lead to files not being encrypted.

### Refresh encryptions

If you have closed your terminal without quiting Safenotes first, there is a
possibility that some notes will not be encrypted (you can tell if a note is
encrypted by checking if its name ends with `.gpg`).

If this happened to you, you can pick the option `Refresh encryptions`, which
will go over each file, and encrypt it if it is not already.

[<- Go back to docs root](README.md)
