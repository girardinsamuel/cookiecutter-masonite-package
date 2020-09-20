"""{{cookiecutter.project_name}} Controller"""

from masonite.view import View
from masonite.request import Request
from app.User import User

class {{cookiecutter.project_name|replace(' ', '')}}Controller:
    """Base controller for the package
    """

    def show(self, view: View, request: Request):

        return 'Hello World'
