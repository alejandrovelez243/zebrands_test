from django.core.mail import send_mail
from rest_framework import viewsets, permissions
from product.models import Product
from rest_framework.response import Response
from product.serializers import ProductSerializer

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

        product = Product.objects.get(pk=response.data['id'])
        # Todo agregar todos los admin activos
        send_mail(
            'New Product Created',
            f'A new product with name {product.name} and id {product.id} has been created.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        return response