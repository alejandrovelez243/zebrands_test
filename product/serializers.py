from rest_framework import serializers

from product.models import Brand, Product


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=Brand.objects.filter(status=True)
    )

    class Meta:
        model = Product
        fields = ["id", "sku", "name", "brand"]
