#!/usr/bin/env python
import os

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

# Add Service Provider if masonite globally available
# print("""You should now run:\n* python craft provider {{ cookiecutter.project_name|replace(' ', '') }}
# \n* move it to src/masonite/{{cookiecutter.pkg_name}}/providers\n""")
print(SUCCESS+"Your package is ready to be developed ! => cd {{cookiecutter.project_slug}}/"+TERMINATOR)
