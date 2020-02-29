# python sketchbook

This is a sketchbook for kemokemo to write various python code while learning with the following books.

- [Python Workout](https://www.manning.com/books/python-workout)
- [Tiny Python Projects](https://www.manning.com/books/tiny-python-projects)

## preparation

### macOS

Use python installed by pyenv instead of standard macOS python to make it easy to switch versions and to allow pip installation without sudo.

```sh
brew install pyenv 
```

Check the available versions.

```sh
pyenv install --list
```

Install it your version wirh options as it is needed by the [PyInstaller](https://pypi.org/project/PyInstaller/) which creates a single executable file.

```sh
PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install {your_version}
```

Switch to your version.

```sh
pyenv grobal 3.8.1
```

Add the following contents to `.bash_profile` or `.zshrc` and restart shell.

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

## packages

You can find many awesome packages for python from the [pypi.org](https://pypi.org/).
