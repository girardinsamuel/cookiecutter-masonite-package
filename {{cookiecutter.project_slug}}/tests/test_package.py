from masonite.testing import TestCase
from masonite.routes import Get

class Test{{cookiecutter.project_name|replace(' ', '')}}(TestCase):

    def setUp(self):
        super().setUp()
        self.routes(only=[
            Get('/home', '{{cookiecutter.project_name|replace(' ', '')}}Controller@show')
        ])
    
    def test_can_get_home_route(self):
        self.assertTrue(
            self.get('/home').contains('Hello World')
        )
