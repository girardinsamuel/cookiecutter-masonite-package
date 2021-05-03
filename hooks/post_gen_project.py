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

# Generate Beyond code banner with https://banners.beyondco.de in README header
pip_name = "{{ cookiecutter.project_slug }}"
package_name = "{{ cookiecutter.project_name }}"
description = "{{ cookiecutter.project_description }}"
package_name_encoded = requote_uri(package_name)
description_encoded = requote_uri(description)
line = f"""<p align="center">
    <img src="https://banners.beyondco.de/{package_name_encoded}.png?theme=light&packageManager=pip+install&packageName={pip_name}&pattern=floorTile&style=style_1&description={description_encoded}&md=1&showWatermark=1&fontSize=100px&images=https%3A%2F%2Fgblobscdn.gitbook.com%2Fspaces%2F-L9uc-9XAlqhXkBwrLMA%2Favatar.png">
</p>
"""
with open(os.path.join(PROJECT_DIRECTORY, "README.md"), "r+") as f:
    content = f.read()
    f.seek(0, 0)
    f.write(line.rstrip("\r\n") + "\n" + content)

print(
    SUCCESS
    + "Your package is ready to be developed ! => cd {{cookiecutter.project_slug}}/"
    + TERMINATOR
)
