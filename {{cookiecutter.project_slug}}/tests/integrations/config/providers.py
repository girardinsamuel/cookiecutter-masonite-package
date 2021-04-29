from masonite.providers import (
    RouteProvider,
    FrameworkProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    SessionProvider,
    QueueProvider,
    CacheProvider,
    EventProvider,
    StorageProvider,
    HelpersProvider,
    BroadcastProvider,
    AuthenticationProvider,
)
from masoniteorm.providers import ORMProvider

from masonite.{{cookiecutter.pkg_name}} import {{cookiecutter.project_name|replace(' ', '')}}Provider

PROVIDERS = [
    FrameworkProvider,
    HelpersProvider,
    RouteProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    SessionProvider,
    CacheProvider,
    QueueProvider,
    EventProvider,
    StorageProvider,
    BroadcastProvider,
    AuthenticationProvider,
    ORMProvider,
    {{cookiecutter.project_name|replace(' ', '')}}Provider,
]
