from django.contrib import admin
from shooze.contents.models import Category, Review
from mptt.admin import DraggableMPTTAdmin

admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Review)
