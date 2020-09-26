"""A {{cookiecutter.project_name|replace(' ', '')}}Provider Service Provider."""

from masonite.provider import ServiceProvider
from masonite.{{cookiecutter.pkg_name}}.commands.InstallCommand import InstallCommand


class {{cookiecutter.project_name|replace(' ', '')}}Provider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind("InstallCommand", InstallCommand())

    def boot(self):
        """Boots services required by the container."""
        pass
