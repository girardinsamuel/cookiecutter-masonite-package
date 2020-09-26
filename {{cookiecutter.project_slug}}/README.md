# {{ cookiecutter.project_name }}

<p align="center">
<img src="https://i.imgur.com/rEXcoMn.png" width="130px">
</p>

<p align="center">

[![Test Application](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/Test%20Application/badge.svg?branch=master)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/)
<img src="https://img.shields.io/badge/python-{{cookiecutter.python_min}}+-blue.svg" alt="Python Version">
<a href="https://pypi.org/project/{{cookiecutter.project_slug}}/"><img alt="PyPI" src="https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}"></a>

</p>

## Introduction

{{ cookiecutter.project_description }}

## Features

- _Add your package main features here_
- _and here_

## Official Masonite Documentation

New to Masonite ? Please first read the [Official Documentation](https://docs.masoniteproject.com/).
Masonite strives to have extremely comprehensive documentation 😃. It would be wise to go through the tutorials there.
If you find any discrepencies or anything that doesn't make sense, be sure to comment directly on the documentation to start a discussion!

Also be sure to join the [Slack channel](http://slack.masoniteproject.com/)!

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

## Configuration

Add {{cookiecutter.project_name|replace(' ', '')}}Provider to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from masonite.{{ cookiecutter.pkg_name }} import {{cookiecutter.project_name|replace(' ', '')}}Provider

# ...
PROVIDERS = [
    # ...

    # Third Party Providers
    {{cookiecutter.project_name|replace(' ', '')}}Provider,

    # ...
]
```

Then install OR publish the reqired package files (configuration, views ...):

```bash
python craft {{cookiecutter.pkg_name}}:install
```

OR (depending on your preferences)

```bash
python craft publish {{cookiecutter.project_name|replace(' ', '')}}Provider
```

## Usage

_Explain how to use your package_

## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

## License

{% if cookiecutter.open_source_license == 'Not open source' -%}
{{ cookiecutter.project_name}} is a closed-sourced software.
{% else %}
{{ cookiecutter.project_name}} is open-sourced software licensed under the [{{ cookiecutter.open_source_license }}](LICENSE).
{% endif %}
