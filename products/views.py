from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Product, User
from .serializers import ProductSerializer
from rest_framework.views import APIView
import random
from .producer import publish


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        publish()
        return Response(serializer.data, status=status.HTTP_200_OK)



    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response ({"Message" : "Product not found"}, status=status.HTTP_404_NOT_FOUND)


    def update(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(instance=product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Product.DoesNotExist:
            return Response ({"Message" : "Product not found"}, status=status.HTTP_404_NOT_FOUND)


    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            product.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response ({"Message" : "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class UserAPIView(APIView):
    def get(self, _):
        """
        return a random user
        """
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id' : user.id
        }, status=status.HTTP_200_OK)