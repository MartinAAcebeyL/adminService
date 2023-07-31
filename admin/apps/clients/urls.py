from django.urls import path
from .views import ClientApiView

urlpatterns = [
    path('', ClientApiView.as_view(), name='clients')
]
