import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "hecoto_backend.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import hecoto_backend.users.signals  # noqa: F401
