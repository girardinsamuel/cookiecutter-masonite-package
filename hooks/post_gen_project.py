#!/usr/bin/env python
import os
import pdb

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if 'Not open source' == '{{ cookiecutter.open_source_license }}':
    remove_file('LICENSE')

print(SUCCESS+"Your package is ready to be developed ! => cd {{cookiecutter.project_slug}}/"+TERMINATOR)
