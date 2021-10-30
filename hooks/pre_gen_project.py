import sys
import re

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


pkg_name = "{{ cookiecutter.pkg_name }}"
pip_name = "{{ cookiecutter.project_slug }}"


if not pip_name.startswith("masonite-"):
    print(
        WARNING
        + "%s is not a valid Masonite pip package! Reasons: pip package name should start with masonite-."
        % pkg_name
        + TERMINATOR
    )
    sys.exit(1)

if not re.match(r"^[a-z0-9_-]+$", pip_name):
    print(
        WARNING
        + "%s is not a valid Masonite pip package! Reasons: Python pip package should contain only a-z,0-9,_,-."
        % pkg_name
        + TERMINATOR
    )
    sys.exit(1)

if "masonite" in pkg_name:
    print(
        WARNING
        + "%s is not a valid Masonite package! Reasons: package name cannot contains masonite as it will be imported from 'masonite.'."
        % pkg_name
        + TERMINATOR
    )
    sys.exit(1)

if not re.match(r"^[a-z0-9_]+$", pkg_name):
    print(
        WARNING
        + "%s is not a valid Python package! Reasons: package name should contain a-z,0-9,_ only."
        % pkg_name
        + TERMINATOR
    )
    sys.exit(1)
