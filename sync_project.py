import subprocess
import os

TEST_PROJECT_PATH = "masonite-{{cookiecutter.project_slug}}/tests/integrations/"

# subprocess.call(f"masonite-package pull --directory {TEST_PROJECT_PATH}")

# add provider to config/providers.py
import_lines = [
    "\n",
    "# register local package\n",
    "from src.{{cookiecutter.pkg_name}} import {{cookiecutter.project_name|replace('Masonite', '')|replace(' ', '')}}Provider\n",
    "\n",
]
insert_lines = [
    "\n",
    "PROVIDERS += [ {{cookiecutter.project_name|replace('Masonite', '')|replace(' ', '')}}Provider ]\n",
]

import_index = None
insert_index = None
new_lines = []
with open(os.path.join(TEST_PROJECT_PATH, "config", "providers.py"), "r") as f:
    file_lines = f.readlines()
    for index, line in enumerate(file_lines):
        if "PROVIDERS =" in line:
            import_index = index - 1
        if "]" in line:
            insert_index = index
    new_lines = (
        file_lines[0:import_index]
        + import_lines
        + file_lines[import_index:]
        + insert_lines
    )


with open(os.path.join(TEST_PROJECT_PATH, "config", "providers.py"), "w") as f:
    f.writelines(new_lines)
