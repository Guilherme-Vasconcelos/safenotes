# Prerequisites

1. Safenotes is only guaranteed to work on GNU/Linux environments. I have
not been able to test it on Windows or Mac OS, so I cannot assure you that
it works. If problems occur, feel free to open an issue or pull request, but
I will probably not be able to test it if it is related to a different
operating system.

2. You need GPG (GNU Privacy Guard), since it is the software used for encrypting
and decrypting the files. If you are using a GNU/Linux distribution, you probably
already have it installed, but you can make sure with the command: `gpg --version`.

3. You need GNU coreutils for commands such as `rm`, `shred` and `mv`. It should
be installed by default in most GNU/Linux distributions. If not, please consult
your distribution manual to see installation instructions.

4. You need a compatible version of Python. It is guaranteed to work on version 3.8
or greater, but I have not tested on 3.7 and below. If you run into problems, please
let me know by opening an issue or pull request, I will be glad to fix compatibility
problems for older versions of Python 3.

[<- Go back to docs root](README.md) | [Proceed to installation ->](INSTALLATION.md)
