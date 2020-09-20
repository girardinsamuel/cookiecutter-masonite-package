""" Web Routes """
from masonite.routes import Get, Post

ROUTES = [
    Get('/', '{{cookiecutter.project_name|replace(' ', '')}}Controller@show').name('welcome'),
]
