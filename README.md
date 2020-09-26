# Cookiecutter Masonite package

<p align="center">
  <img src="https://pyup.io/repos/github/girardinsamuel/cookiecutter-masonite-package/python-3-shield.svg?t=1600644773859" class="badge-modal-trigger-py3 shield" data-toggle="tooltip" data-placement="top" title="show url" id="py3-shield">
  <img src="https://pyup.io/repos/github/girardinsamuel/cookiecutter-masonite-package/shield.svg" class="badge-modal-trigger shield" data-toggle="tooltip" data-placement="top" title="" id="shield" data-original-title="show url">
</p>

## Demo

You can see a demo repository, to have an overview of the scaffolded package result:
[masonite-demo-package](https://github.com/girardinsamuel/masonite-demo-package)

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.5.0 or higher):

```bash
pip install -U cookiecutter
```

Generate your Masonite package project and follow prompt options:

```bash
cookiecutter https://github.com/girardinsamuel/cookiecutter-masonite-package.git
```

(For more options, check directly [cookiecutter](https://github.com/cookiecutter/cookiecutter).)

**⚠️ Package naming**

To have a consistent Masonite package ecosystem, it is advised to follow auto naming provided by `cookiecutter`:

- All packages should have a pip install name like `masonite-my-package`: masonite-api, masonite-events.
- A package name should be `Masonite My Package`: Masonite API, Masonite Events... .
- A package should be imported from `masonite` namespace:

```
from masonite.api import X
from masonite.events import Y
from masonite.my_package import Z
```

When you are first prompted for the name of your package, enter the readable human name without `Masonite`:

```
project_name [Package Name]: My Package
```

Then the following prompts should not require modifications:

```
project_slug [masonite-my-package]:
project_description [Package description in one line displayed e.g. in README]:
pkg_name [my_package]:
[...]
repository [https://github.com/girardinsamuel/masonite-my-package]:

```

## Masonite Official Documentation

Check the Official Documentation on [creating packages](https://docs.masoniteproject.com/advanced/creating-packages) !

You can also create a package from a GitHub template repo [starter-package](https://github.com/MasoniteFramework/starter-package/generate) but you will have to
name all your files manually and update all configuration files with your name, GitHub repository name and so on...
