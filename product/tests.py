from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from product.models import Brand, Product
from product.serializers import ProductSerializer
from product.views import ProductViewSet


class ProductSerializerTest(TestCase):
    def setUp(self):
        """
        This setup the necessary values for the test.
        """
        self.brand = Brand.objects.create(name="Test Brand")
        self.new_brand = Brand.objects.create(name="New Brand")
        self.product = Product.objects.create(sku="SKU123", name="Test Product", brand=self.brand)
        self.serializer_data = {"sku": "SKU123", "name": "Test Product", "brand": "Test Brand"}
        self.invalid_data = {"sku": "", "name": "", "brand": ""}

    def test_valid_data(self):
        """
        It tests the serializer with valid data.
        """
        serializer = ProductSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        self.assertEqual(product.sku, "SKU123")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.brand, self.brand)

    def test_invalid_data(self):
        """
        The function tests that the serializer is not valid when the data is invalid
        """
        serializer = ProductSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIsNotNone(serializer.errors)

    def test_retrieve_data(self):
        """
        It tests the serializer.
        """
        serializer = ProductSerializer(self.product)
        data = serializer.data
        self.assertEqual(data["id"], self.product.id)
        self.assertEqual(data["sku"], "SKU123")
        self.assertEqual(data["name"], "Test Product")
        self.assertEqual(data["brand"], self.brand.name)

    def test_update_data(self):
        """
        It updates the data in the database.
        """
        new_data = {"brand": "New Brand"}
        serializer = ProductSerializer(self.product, data=new_data, partial=True)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        self.assertEqual(product.brand, self.new_brand)
        self.assertEqual(product.sku, "SKU123")
        self.assertEqual(product.name, "Test Product")

    def test_valid_slug(self):
        """
        It tests if the serializer is valid.
        """
        serializer = ProductSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["brand"], self.brand)


class ProductAPITest(APITestCase):
    def setUp(self):
        """
        This setup the necessary values for the test.
        """
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="glass onion"
        )
        self.brand = Brand.objects.create(name="Test Brand")
        self.new_brand = Brand.objects.create(name="New Brand")
        self.product = Product.objects.create(
            id=2, sku="SKU123", name="Test Product", brand=self.brand
        )

    def test_list_products(self):
        """
        It tests the list view of the ProductViewSet.
        """
        view = ProductViewSet.as_view(actions={"get": "list"})
        request = self.factory.get("/products/")
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["sku"], "SKU123")
        self.assertEqual(response.data[0]["name"], "Test Product")
        self.assertEqual(response.data[0]["brand"], "Test Brand")

    def test_create_product(self):
        """
        It creates a new product.
        """
        view = ProductViewSet.as_view(actions={"post": "create"})
        data = {"sku": "SKY456", "name": "Test Product 2", "brand": self.new_brand.name}
        request = self.factory.post("/products/", data)
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(sku="SKY456").name, "Test Product 2")

    def test_update_product(self):
        """
        I'm trying to update a product with a PUT request.
        """
        view = ProductViewSet.as_view(actions={"put": "update"})
        data = {"name": "Updated Name", "sku": "SKU123", "brand": "Test Brand"}
        request = self.factory.put("/products/", data)
        force_authenticate(request, user=self.user)
        response = view(request, pk=2)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.get(pk=2).name, "Updated Name")

    def test_retrieve_product(self):
        """
        I'm trying to test the retrieve method of the ProductViewSet class.
        """
        view = ProductViewSet.as_view(actions={"get": "retrieve"})
        request = self.factory.get("/products/1/")
        force_authenticate(request, user=self.user)
        response = view(request, pk=2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["sku"], "SKU123")
        self.assertEqual(response.data["name"], "Test Product")
        self.assertEqual(response.data["brand"], "Test Brand")
        self.assertEqual(Product.objects.get(pk=2).called, 1)
