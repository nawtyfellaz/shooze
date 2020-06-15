from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver, Signal

from shooze.contents.models import Category, Review
from shooze.utils.functionality import unique_slug_generator, unique_sku_number_generator

@receiver(pre_save, sender=Category)
def create_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

@receiver(pre_save, sender=Review)
def create_review_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


