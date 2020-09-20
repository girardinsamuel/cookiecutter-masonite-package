import sys


pkg_name = '{{ cookiecutter.pkg_name }}'


if "masonite" in pkg_name:
    print('ERROR: %s is not a valid Masonite package! Reasons: package name cannot contains masonite.' % pkg_name)

    # exits with status 1 to indicate failure
    sys.exit(1)
