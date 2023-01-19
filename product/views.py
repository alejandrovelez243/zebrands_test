from rest_framework import permissions, viewsets
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer
from product.services import send_slack_message


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(status=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.called += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        product = Product.objects.get(pk=response.data["id"])
        send_slack_message(
            f"A new product with name {product.name} and id {product.id} has been created."
        )

        return response
