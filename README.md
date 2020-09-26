# Cookiecutter Masonite Package

<p align="center">
  <img src="https://pyup.io/repos/github/girardinsamuel/cookiecutter-masonite-package/shield.svg" class="badge-modal-trigger shield" data-toggle="tooltip" data-placement="top" title="" id="shield" data-original-title="show url">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/girardinsamuel/cookiecutter-masonite-package">
  <img alt="GitHub" src="https://img.shields.io/github/license/girardinsamuel/cookiecutter-masonite-package">
</p>

**Demo**
You can see a demo repository, to have an overview of the scaffolded package result:
[masonite-demo-package](https://github.com/girardinsamuel/masonite-demo-package)

## Masonite Official Documentation

First check the Official Documentation on [creating packages](https://docs.masoniteproject.com/advanced/creating-packages) !
You can also creating a package from the Official Github template: [starter-package](https://github.com/MasoniteFramework/starter-package).

## Crafting the package

1. Install the latest `cookiecutter` version:

```bash
$ pip install -U cookiecutter
```

2. Generate your Masonite package project following prompt options:

```bash
$ cookiecutter https://github.com/girardinsamuel/cookiecutter-masonite-package.git
```

(_For cookiecutter CLI options, check directly [cookiecutter](https://github.com/cookiecutter/cookiecutter)_).

**Masonite Package Naming Guidelines ⚠️ **

To have a consistent Masonite package ecosystem, it is advised to follow Masonite [Naming Guidelines](https://github.com/MasoniteFramework/starter-package).

**TL;DR:**

- The verbose/human name of your package should start with `Masonite` such as `Masonite API`, `Masonite Events`, `Masonite Nice Package`.
- You can slugify this name to get a Python package name (installable with pip). All Masonite packages should have a
  Python package name starting with **masonite-** such as `masonite-api`, `masonite-events`, `masonite-nice-package`.

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

## Dev Quick Start

Whatever crafting option you choose when your repository is created, you should start by creating a virtual environment and activate it:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Init dependencies (this will install Masonite, a few development related packages and the package itself):

```
$ make init
```

Finally you can run the tests and start building your application:

```
$ python -m pytest
```

You can start the test project in the repo to test your package at `http://localhost:8000/`:

```
$ python craft serve
```

**Setup coverage**

The repository is setup to use `Coveralls` to publish the package coverage.

1. You just have to login/register at [coveralls.io](https://coveralls.io/).
2. Connect with Github provider and select your package repository.
3. Finally you must get your `SECRET_TOKEN` and add it as a Secret Github token in the repo settings. (_check if correct method_)

Github CI will run tests, compute coverage and upload it to coveralls. The badge is already configured for
Coveralls and should display correctly at first coveralls score publish.

Of course you can use `codecov` if you prefer, you will have to edit Github workflow and the badge.

**Publish your package on PyPi**

To publish the package read the Official Documentation guide on [publishing package to PyPi](https://docs.masoniteproject.com/advanced/creating-packages#uploading-to-pypi).

A Github workflow is already configure to publish the package to PyPi when
a release is created.

More info in [Contributing Documentation](CONTRIBUTING.md).
