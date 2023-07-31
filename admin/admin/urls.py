from django.contrib import admin
from django.urls import path, include
from apps.products.urls import urlpatterns as url_products
from apps.clients.urls import urlpatterns as url_clients


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', include(url_products)),
    path('api/v1/clients/', include(url_clients))
]
