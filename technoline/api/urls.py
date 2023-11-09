from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as rest_views

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)
router.register(
    r'product/(?P<product_id>[0-9]+)/reviews', views.ProductReviewsViewSet, basename='Product')
router.register(r'reviews', views.ReviewViewSet)
router.register(r'cart', views.CartViewSet, basename='Cart')


urlpatterns = [
    path('', include(router.urls)),
]

# auth_token
urlpatterns += [
    path('api-token-auth/', rest_views.obtain_auth_token),
]
