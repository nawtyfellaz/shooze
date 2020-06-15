from django.db import models

class CategoryManager(models.Manager):
    def get_queryset(self):
        # All posts
        return super().get_queryset()

    def all_active(self):
        # All active posts
        return super().get_queryset().filter(active=True)

    def all_inactive(self):
        # All inactive posts
        return super().get_queryset().filter(active=False)

class ReviewManager(models.Manager):
    def get_queryset(self):
        # All reviews
        return super().get_queryset()

    def all_active(self):
        # All active reviews
        return super().get_queryset().filter(active=True)

    def all_inactive(self):
        # All inactive reviews
        return super().get_queryset().filter(active=False)

    