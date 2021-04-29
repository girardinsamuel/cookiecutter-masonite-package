"""A {{cookiecutter.project_name|replace(' ', '')}}Provider Service Provider."""

from masonite.providers import Provider
from masonite.{{cookiecutter.pkg_name}}.commands.InstallCommand import InstallCommand


class {{cookiecutter.project_name|replace(' ', '')}}Provider(Provider):
    """Provides Services To The Service Container."""

    def __init__(self, app):
        self.application = app

    def register(self):
        """Register objects into the Service Container."""
        self.application.make("commands").add(InstallCommand())

    def boot(self):
        """Boots services required by the container."""
        pass
