from django.test import TestCase

from product.models import Brand, Product
from product.serializers import ProductSerializer


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="Test Brand")
        self.new_brand = Brand.objects.create(name="New Brand")
        self.product = Product.objects.create(sku="SKU123", name="Test Product", brand=self.brand)
        self.serializer_data = {"sku": "SKU123", "name": "Test Product", "brand": "Test Brand"}
        self.invalid_data = {"sku": "", "name": "", "brand": ""}

    def test_valid_data(self):
        serializer = ProductSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        self.assertEqual(product.sku, "SKU123")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.brand, self.brand)

    def test_invalid_data(self):
        serializer = ProductSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIsNotNone(serializer.errors)

    def test_retrieve_data(self):
        serializer = ProductSerializer(self.product)
        data = serializer.data
        self.assertEqual(data["id"], self.product.id)
        self.assertEqual(data["sku"], "SKU123")
        self.assertEqual(data["name"], "Test Product")
        self.assertEqual(data["brand"], self.brand.name)

    def test_update_data(self):
        new_data = {"brand": "New Brand"}
        serializer = ProductSerializer(self.product, data=new_data, partial=True)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        self.assertEqual(product.brand, self.new_brand)
        self.assertEqual(product.sku, "SKU123")
        self.assertEqual(product.name, "Test Product")

    def test_valid_slug(self):
        serializer = ProductSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["brand"], self.brand)
