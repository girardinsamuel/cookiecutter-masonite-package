"""Small script to update demo package when this cookiecutter is updated."""

import os
import shutil
import sys
from cookiecutter.main import cookiecutter

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
        "project_description": "Demo package to show Masonite package generator.",
    },
)

os.chdir("../masonite-demo-package")

# Then commit manually "update with vX.X"
