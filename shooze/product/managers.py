from django.db import models

class ProductManager(models.Manager):
    def get_queryset(self):
        # All posts
        return super().get_queryset()

    def all_instock(self):
        return super().get_queryset().filter(stock=True)

    def all_featured(self):
        # All posts
        return super().get_queryset().filter(stock=True).filter(featured=True)

    def all_digital(self):
        return super().get_queryset().filter(stock=True).filter(digital=True)

    
class StoreManager(models.Manager):
    def get_queryset(self):
        # All posts
        return super().get_queryset()

    def all_active(self):
        return super().get_queryset().filter(active=True)

    def all_inactive(self):
        # All posts
        return super().get_queryset().filter(active=False)