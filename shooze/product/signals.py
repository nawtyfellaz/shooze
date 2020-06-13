from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver, Signal

from shooze.product.models import Product
from shooze.utils.functionality import unique_slug_generator, unique_sku_number_generator

@receiver(pre_save, sender=Product)
def create_products_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    if not instance.sku:
        instance.sku = unique_sku_number_generator(instance)
