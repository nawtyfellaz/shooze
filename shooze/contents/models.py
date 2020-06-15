from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
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
    PositiveIntegerField,
    OneToOneField,
    ManyToManyField,
    Q,
    SlugField,
    CASCADE,
    SET_NULL,
    URLField
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from model_utils.models import TimeStampedModel #created & modified fields
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from shooze.utils.functionality import unique_slug_generator, get_filename

from shooze.contents.managers import CategoryManager, ReviewManager


User = settings.AUTH_USER_MODEL


def image_file_path(instance, filename):
    return "shooze/images/{filename}".format(filename=filename)


class Category(MPTTModel):
    title       = CharField(_('category_title'), max_length=120, null=True, blank=True, unique=True)
    slug        = SlugField(unique=True, null=True, blank=True, max_length=350)
    active      = BooleanField(default=True)
    parent      = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=CASCADE)
    created     = models.DateTimeField(default=timezone.now)
    modified    = models.DateTimeField(auto_now=True)
    # content_type= ForeignKey(ContentType, on_delete=CASCADE)
    # object_id   = PositiveIntegerField()
    # content_obj = GenericForeignKey()

    objects = CategoryManager()

    def __str__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return _('title'), _('parent')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        managed = True
        verbose_name = _('Category')
        verbose_name_plural = _('Categroies')
        ordering = ['title', '-created', '-modified']

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs

    def get_absolute_url(self):
        return f"/category/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"





class Review(TimeStampedModel):
    author      = ForeignKey(User, _('reviewer'), related_name=_('reviewer'), null=True)
    content_type= ForeignKey(ContentType, on_delete=CASCADE)
    text        = RichTextUploadingField()
    active      = BooleanField(default=True)
    object_id   = PositiveIntegerField()
    content_obj = GenericForeignKey()

    class Meta:
        ordering = ['-created']

    def _str_(self):
        request = self.request
        if request.user.ia_authenticated:
            text = 'Comment by {}'.format(request.user.username)
        else:
            text = 'Comment by {}'.format(self.author)
        return text




