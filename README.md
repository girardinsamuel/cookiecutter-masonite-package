# Cookiecutter Masonite Package

<p align="center">
  <img alt="GitHub Workflow Status (branch)" src="https://img.shields.io/github/workflow/status/girardinsamuel/cookiecutter-masonite-package/Test%20Application">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/girardinsamuel/cookiecutter-masonite-package">
  <img alt="GitHub" src="https://img.shields.io/github/license/girardinsamuel/cookiecutter-masonite-package">
</p>

**Demo**
You can see a demo repository, to have an overview of the scaffolded package result:
[masonite-demo-package](https://github.com/girardinsamuel/masonite-demo-package)

## Masonite Official Documentation

First check the Official Documentation on [creating packages](https://docs.masoniteproject.com/advanced/creating-packages) !
You can also create a package from the official Github template: [starter-package](https://github.com/MasoniteFramework/starter-package).

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

**Masonite Package Naming Guidelines** ⚠️

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
project_slug [my-package]:
project_description [Package description in one line displayed e.g. in README]:
pkg_name [my_package]:
[...]
repository [https://github.com/girardinsamuel/masonite-my-package]:
```
