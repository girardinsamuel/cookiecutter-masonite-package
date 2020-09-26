# Cookiecutter Masonite package

<p align="center">
  <img src="https://pyup.io/repos/github/girardinsamuel/cookiecutter-masonite-package/shield.svg" class="badge-modal-trigger shield" data-toggle="tooltip" data-placement="top" title="" id="shield" data-original-title="show url">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/girardinsamuel/cookiecutter-masonite-package">
  <img alt="GitHub" src="https://img.shields.io/github/license/girardinsamuel/cookiecutter-masonite-package">
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

_For more options, check directly [cookiecutter](https://github.com/cookiecutter/cookiecutter)_

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

## Setup coverage

The repository is setup to use `Coveralls` to publish the package coverage.

1. You just have to login/register [coveralls.io][https://coveralls.io/]
2. Connect with Github provider and select your package repository
3. Finally you must get your `SECRET_TOKEN` and add it as a Secret Github token in the repo settings

Github CI will run tests, compute coverage and upload it to coveralls. The badge is already configured for
Coveralls and should display correctly at first coveralls score publish.

Of course you can use `codecov` if you prefer, you will have to edit Github workflow and the badge.

## Publish your package on PyPi

To publish the package read the Official Documentation guide on [publishing package to PyPi](https://docs.masoniteproject.com/advanced/creating-packages#uploading-to-pypi).

A Github workflow is already configure to publish the package to PyPi when
a release is created.
