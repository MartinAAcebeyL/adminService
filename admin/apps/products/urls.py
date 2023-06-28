from django.urls import path
from views import ProductViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='products'),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='products'),
]
