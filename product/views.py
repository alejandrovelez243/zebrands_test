from rest_framework import permissions, viewsets
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer
from product.services import send_slack_message


class ProductViewSet(viewsets.ModelViewSet):
    """
    The ProductViewSet class is a subclass of the ModelViewSet class. It has a queryset attribute
    that filters the Product model by status. It has a serializer_class attribute that specifies
    the ProductSerializer class. It has a permission_classes attribute that specifies the
    IsAuthenticatedOrReadOnly permission class. It has a retrieve method that overrides the retrieve
    method of the ModelViewSet class. It has a create method that overrides the create method of the
    ModelViewSet class
    """

    queryset = Product.objects.filter(status=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        """
        It retrieves the object, increments the called field by 1, saves the object, and returns the
        serializer data

        :param request: The request object
        :return: The instance of the object that was called.
        """
        instance = self.get_object()
        instance.called += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        It creates a new product, gets the product's id and name, and sends a slack message with the
        product's id and name

        :param request: The request object
        :return: The response is being returned.
        """
        response = super().create(request, *args, **kwargs)

        product = Product.objects.get(pk=response.data["id"])
        send_slack_message(
            f"A new product with name {product.name} and id {product.id} has been created."
        )

        return response
