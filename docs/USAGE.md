# Usage

If you have not yet installed Safenotes, please refer to docs/INSTALLATION.md.

---

### Table of contents

- [Safenotes for the first time](#safenotes-for-the-first-time)
- [Precautions](#precautions)
- [Creating notes](#creating-notes)
- [Refresh encryptions](#refresh-encryptions)
- [Selecting a note - Reading, editing and deleting](#selecting-a-note---reading-editing-and-deleting)

---

### Safenotes for the first time

After following the installation steps, you can use the command `safenotes`
to run the program. If you went with the manual installation, you must make
sure your virtual environment is activated, otherwise you will not have the
dependencies and the `safenotes` command. If you see an unrecognized command
error, please refer to docs/INSTALLATION.md.

After that, it will ask you to define a password. Make sure you pick one you
will remember, because recovering it is not possible without losing access
to your notes, because this is also the passphrase which will be used to
encrypt the notes.

### Precautions

- After you finish editing your note, you must save it and leave the text editor.
If you close your terminal without leaving the text editor, the note will NOT
be encrypted. Refer to [Refresh encryptions](#refresh-encryptions) for more details.

### Creating notes

After you've been prompted for your password and "logged in", you can create new
notes by selecting the "New note" button.

By selecting the "New note" button, your system's default editor will open. If
you have not changed the EDITOR environment variable, it will probably be nano.
You can save your text with ctrl + s and quit the editor with ctrl + x, then you
will be back to Safenotes' menu, in which you will be able to see the note you
just created.

### Refresh encryptions

If you have closed your terminal while the text editor was opened, there is a
possibility that some notes will not be encrypted (you can tell if a note is
encrypted by checking if its name ends with `.gpg`).

If this happened to you, you can pick the option `Refresh encryptions`, which
will go over each file, and encrypt it if it is not already.

### Selecting a note - Reading, editing and deleting

Besides the creating notes and refresh encryptions options, you can also select
a specific note. By doing so you will be sent to another menu, in which you can:

- Read/Edit: by selecting this option the file will be unencrypted and you will
be sent to your text editor to be able to read or edit the note.
- Delete: by selecting this option the file will be deleted. You should be aware
that you can only delete files that are currently encrypted. If your note is not
encrypted, you can encrypt it by going back to the initial menu and picking the
`Refresh encryptions` option.

[<- Go back to docs root](README.md)
