""" Providers Configuration File """

from masonite.providers import (
    AppProvider,
    AuthenticationProvider,
    SessionProvider,
    RouteProvider,
    StatusCodeProvider,
    WhitenoiseProvider,
    MailProvider,
    UploadProvider,
    ViewProvider,
    HelpersProvider,
    QueueProvider,
    BroadcastProvider,
    CacheProvider,
    CsrfProvider,
)
from masoniteorm.providers.ORMProvider import ORMProvider

from masonite.{{cookiecutter.pkg_name}} import  {{cookiecutter.project_name|replace(' ', '')}}Provider

"""
|--------------------------------------------------------------------------
| Providers List
|--------------------------------------------------------------------------
|
| Providers are a simple way to remove or add functionality for Masonite
| The providers in this list are either ran on server start or when a
| request is made depending on the provider. Take some time to learn
| more about Service Providers in our documentation
|
"""


PROVIDERS = [
    # Framework Providers
    AppProvider,
    SessionProvider,
    RouteProvider,
    StatusCodeProvider,
    WhitenoiseProvider,
    ViewProvider,
    AuthenticationProvider,
    ORMProvider,

    # Optional Framework Providers
    MailProvider,
    UploadProvider,
    QueueProvider,
    CacheProvider,
    BroadcastProvider,
    CacheProvider,
    CsrfProvider,
    HelpersProvider,

    # Third Party Providers
    {{cookiecutter.project_name|replace(' ', '')}}Provider,

    # Application Provider

]
