#!/usr/bin/env python
import os
from requests.utils import requote_uri

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

pkg_name = "{{ cookiecutter.project_name }}"

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if "Not open source" == "{{ cookiecutter.open_source_license }}":
    remove_file("LICENSE")

print(
    "Masonite package successfully crafted ! => cd masonite-{{cookiecutter.project_slug}}"
    + TERMINATOR
)
