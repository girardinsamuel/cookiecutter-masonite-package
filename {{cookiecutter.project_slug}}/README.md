# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

<p align="center">
<img src="https://i.imgur.com/rEXcoMn.png" width="160px">
</p>

TODO : add badges
- min python
- pypi version
- black
- tests ci
- coverage
- license
- contributors


## Learning Masonite

Masonite strives to have extremely comprehensive documentation. All documentation can be [Found Here](https://masoniteframework.gitbooks.io/docs/content/) and would be wise to go through the tutorials there. If you find any discrepencies or anything that doesn't make sense, be sure to comment directly on the documentation to start a discussion!

Also be sure to join the [Slack channel](https://masoniteframework.gitbooks.io/docs/content/)!

## Installation
```bash
pip install {{ cookiecutter.project_slug }}
```

## Configuration
Add ServiceProvider to your app
```python
# ...
from masonite.{{ cookiecutter.pkg_name }} import XXXProvider
```

```bash
python craft {{cookiecutter.pkg_name}}:install
```
OR
```bash
python craft publish XXX
```

## Usage

## How to contribute

