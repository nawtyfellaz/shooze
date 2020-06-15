from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContentsConfig(AppConfig):
    name = 'shooze.contents'
    verbose_name = _("Contents")

    def ready(self):
        try:
            import shooze.contents.signals  # noqa F401
        except ImportError:
            pass