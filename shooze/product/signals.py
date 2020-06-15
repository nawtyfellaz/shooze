from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver, Signal

from shooze.product.models import Product, Brand, Seller
from shooze.utils.functionality import unique_slug_generator, unique_sku_number_generator

@receiver(pre_save, sender=Product)
def create_products_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    if not instance.sku:
        instance.sku = unique_sku_number_generator(instance)

@receiver(pre_save, sender=Brand)
def create_brand_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Seller)
def create_seller_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

