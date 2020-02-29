# Hello python

## features

Like this!

![Image](media/hello.png)

## when you craete an executable file

Use [PyInstaller](https://pypi.org/project/PyInstaller/).

```sh
pip install pyinstaller
```

```sh
pyinstaller --onefile hello.py
```

### Note

The PyInstaller is not a cross-compiler.

> PyInstaller is tested against Windows, Mac OS X, and GNU/Linux. However, it is not a cross-compiler: to make a Windows app you run PyInstaller in Windows; to make a GNU/Linux app you run it in GNU/Linux, etc. PyInstaller has been used successfully with AIX, Solaris, FreeBSD and OpenBSD but testing against them is not part of our continuous integration tests.

Quote source: [PyInstaller Manual](https://pyinstaller.readthedocs.io/en/stable/index.html)

If you build an app on the CI (ex. TravisCI), use the target platforms to execute.
