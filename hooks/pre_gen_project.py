import sys

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


pkg_name = '{{ cookiecutter.pkg_name }}'


if "masonite" in pkg_name:
    print(WARNING + '%s is not a valid Masonite package! Reasons: package name cannot contains masonite.' % pkg_name + TERMINATOR)

    # exits with status 1 to indicate failure
    sys.exit(1)
