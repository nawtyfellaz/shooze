from rest_framework import serializers

from shooze.product.models import Products


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["title", "sku", "image", "size"]

        extra_kwargs = {
            "url": {"view_name": "api:product-detail", "lookup_field": "slug"}
        }
