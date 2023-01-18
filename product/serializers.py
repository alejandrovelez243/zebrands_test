from rest_framework import serializers
from production.models import Product, Brand


class ProductSerializer(serializers.ModelSerializer):
    brande = serializers.SlugField(

    )
    class Meta:
        model = Product
        fields = ['id', 'sky', 'name', 'brand']