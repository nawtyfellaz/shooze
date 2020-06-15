from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator
)
from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    EmailField,
    FileField,
    ForeignKey,
    ImageField,
    IntegerField,
    OneToOneField,
    ManyToManyField,
    Q,
    SlugField,
    CASCADE,
    SET_NULL,
    URLField
)
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel #created & modified fields

from ckeditor_uploader.fields import RichTextUploadingField
from shooze.product.validator import file_validator

from shooze.utils.functionality import unique_slug_generator, get_filename
from shooze.product.managers import ProductManager, StoreManager
from shooze.contents.models import Category, Review

User = settings.AUTH_USER_MODEL


# Create your models here.
def brand_logo(instance, filename):
    return "product/brand/{filename}".format(filename=filename)

def seller_file_path(instance, filename):
    return "product/sellers/{filename}".format(filename=filename)

def product_file_path(instance, filename):
    return "product/files/{filename}".format(filename=filename)


class Brand(TimeStampedModel):
    title       = CharField(_('Brand_Name'), blank=False, null=True, max_length=300)
    slug        = SlugField(unique=True, null=True, blank=True, max_length=350)
    logo        = ImageField(_('brand_logo'), upload_to=brand_logo, null=True, blank=True)
    active      = BooleanField(default=True)

    def __str__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return 'title'

    class Meta:
        managed = True
        verbose_name = _('Brand')
        verbose_name_plural = _('Stores')
        ordering = ['title', 'active']

    def get_absolute_url(self):
        return f"/brand/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"


class Seller(TimeStampedModel):
    owner       = OneToOneField(User, _('marchant'), related_name='marchant', null=True)
    title       = CharField(_('Store_Name'), blank=False, null=True, max_length=300)
    slug        = SlugField(unique=True, null=True, blank=True, max_length=350)
    active      = BooleanField(default=True)

    objects = StoreManager()

    def __str__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return 'title', 'owner'

    class Meta:
        managed = True
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
        ordering = ['title', 'active']

    def get_absolute_url(self):
        return f"/store/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"


class Product(TimeStampedModel):
    store      = ForeignKey(Seller, _('store_name'), null=True)
    title       = CharField(_('Product Name'), blank=False, null=True, max_length=300)
    slug        = SlugField(unique=True, null=True, blank=True, max_length=350)
    price       = DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    sku         = CharField(_('SKU'), max_length=7, blank=True, null=True)
    maf_date    = DateField(_('manufacturing_date'), auto_now=False, auto_now_add=False, null=True, blank=False)
    brand       = ForeignKey(Brand, _('product_brand'), related_name='product_brand', null=True)
    description = RichTextUploadingField()
    instock     = BooleanField(default=False)
    featured    = BooleanField(default=False)
    digital     = BooleanField(default=False)
    category    = ManyToManyField(Category, related_query_name='products')
    review      = GenericRelation(Review, related_query_name='product_reviews')

    objects = ProductManager()

    def __str__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return 'title', 'seller', 'maf_date'

    class Meta:
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['title', '-maf_date', '-created', '-modified']

    def get_absolute_url(self):
        return f"/product/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"



class Images(TimeStampedModel):
    product         = ForeignKey(Product, on_delete=CASCADE)
    title           = CharField(_('Product_image_title'), max_length=150)
    image           = ImageField(_('upload_images'), upload_to=product_file_path, null=True, blank=True)

    def __str__(self):
        return self.content_type.title

    class Meta:
        managed = True
        verbose_name = _('Product File')
        verbose_name_plural =  _('Product Files')
        ordering = ['-created']

