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
    HashServiceProvider,
)
from masonite.scheduling.providers import ScheduleProvider
from masonite.notification.providers import NotificationProvider
from masoniteorm.providers import ORMProvider

# register local package
from src.masonite.{{cookiecutter.pkg_name}} import {{cookiecutter.project_name|replace(' ', '')}}Provider

PROVIDERS = [
    FrameworkProvider,
    HelpersProvider,
    RouteProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    NotificationProvider,
    SessionProvider,
    CacheProvider,
    QueueProvider,
    ScheduleProvider,
    EventProvider,
    StorageProvider,
    BroadcastProvider,
    HashServiceProvider,
    AuthenticationProvider,
    ValidationProvider,
    ORMProvider,
    {{cookiecutter.project_name|replace(' ', '')}}Provider,
]
