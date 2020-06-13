import datetime 
import os
import random
import string
import math

from django.db.models import Count, Sum, Avg
from django.utils import timezone
from django.utils.text import slugify


def random_integer_generator(size=12, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_sku_number_generator(instance):
    """
    This is for a Django project with a identity carfield
    """
    size = random.randint(7, 7)
    new_result_number = random_integer_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(sku=new_result_number).exists()

    if qs_exists:
        return unique_slug_generator(instance)
    return new_result_number

def get_filename(path): #/abc/filename.mp4
    return os.path.basename(path)

def unique_order_id_generator(instance):
    """
    This is for a Django project with an order_id field
    """
    order_new_id = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
