from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from products.models import Cart, Product, Review

from .permissions import IsAuthorOrReadOnly
from .serializers import (CartSerializer, PrdouctSerializer,
                          ProductReviewsSerializer, ReviewSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PrdouctSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductReviewsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        queryset = product.reviews.all()  # type: ignore
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user,
                                product_id=kwargs.get('product_id'))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def update(self, request, pk=None):
        review = get_object_or_404(self.queryset, pk=pk)
        if request.user.is_authenticated:
            if request.user == review.author:
                serializer = self.serializer_class(review, data=request.data)
                if serializer.is_valid():
                    serializer.save(product=review.product,
                                    author=request.user)
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        review = get_object_or_404(self.queryset, pk=pk)
        if request.user == review.author:
            review.delete()
            return Response("performed", status=status.HTTP_204_NO_CONTENT)
        return Response("not performed", status=status.HTTP_403_FORBIDDEN)


class CartViewSet(viewsets.ViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = get_object_or_404(Cart, user=user)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
