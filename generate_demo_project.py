"""Small script to update demo package when this cookiecutter is updated."""

import os
import shutil
import sys
from cookiecutter.main import cookiecutter

# display info on the README about this cookiecutter thing
project_description = """Demo package to show Masonite cookiecutter scaffolding result.

**This package has been generated with [Cookiecutter Masonite Package](https://github.com/girardinsamuel/cookiecutter-masonite-package). The badges will display correctly at first Github release and first PyPi publish.**

**To report bugs or request features please use the [Cookiecutter Masonite Package](https://github.com/girardinsamuel/cookiecutter-masonite-package) repo directly.**"""

# Clean old generated masonite demo package which are not cleaned by cookiecutter because hidden
shutil.rmtree("../masonite-demo-package/.github/", ignore_errors=True)

# Get template to use
options = sys.argv
tag = None
template = "https://github.com/girardinsamuel/cookiecutter-masonite-package.git"

if len(options) == 2:
    tag = options[1]

# Generate the project
print(f"Crafting project from: {template} {tag if tag else ''}")
cookiecutter(
    template,
    output_dir="../",
    no_input=True,
    overwrite_if_exists=True,
    checkout=tag,
    extra_context={
        "project_name": "Demo Package",
        "project_description": project_description,
    },
)

os.chdir("../masonite-demo-package")

# Then commit manually "update with vX.X"
