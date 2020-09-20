#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if 'Not open source' == '{{ cookiecutter.open_source_license }}':
    remove_file('LICENSE')

# Add Service Provider if masonite globally available
print("""You should now run:\n* python craft provider {{ cookiecutter.project_name|replace(' ', '') }}
\n* move it to src/masonite/{{cookiecutter.pkg_name}}/providers\n""")
