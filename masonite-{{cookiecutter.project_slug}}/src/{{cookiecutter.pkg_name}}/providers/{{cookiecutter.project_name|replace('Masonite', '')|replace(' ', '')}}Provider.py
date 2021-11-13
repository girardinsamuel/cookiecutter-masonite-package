"""A {{cookiecutter.project_name|replace('Masonite', '')|replace(' ', '')}}Provider Service Provider."""

from masonite.packages import PackageProvider


class {{cookiecutter.project_name|replace('Masonite', '')|replace(' ', '')}}Provider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("src/{{cookiecutter.pkg_name}}")
            .name("{{cookiecutter.project_slug}}")
            .config("config/{{cookiecutter.pkg_name}}.py", publish=True)
        )

    def boot(self):
        """Boots services required by the container."""
        pass
