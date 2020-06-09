from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver, Signal

from shooze.product.models import Products
from shooze.utils.functionality import unique_slug_generator

@receiver(pre_save, sender=Products)
def create_products_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
