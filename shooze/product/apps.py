from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductConfig(AppConfig):
    name = 'shooze.product'
    verbose_name = _("product")

    def ready(self):
        # story_model = apps.get_model("etopoenergy.blog", "etopoenergy.blog.models.Post")
        # secretballot.enable_voting_on(story_model)
        try:
            import shooze.product.signals  # noqa F401
        except ImportError:
            pass


