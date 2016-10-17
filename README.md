# mksymlink

A dotfiles management tool with Dropbox.


## Usage

Create a _dotfiles_ directory in your Dropbox.
Then, put your dotfiles and this script (`mksymlink.py`) into the _dotfiles_ directory.

You should write the target list on the `target` list of `mksymlink.py` like this:

```
target = [
    '.ssh/config',
    '.ssh/keys',
    '.zshrc',
    '.gitconfig'
]
```

Now, run:

```
python mksymlink.py
```
