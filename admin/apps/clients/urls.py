from django.urls import path
from views import ClientApiView

urlpatterns = [
    path('clients', ClientApiView.as_view(), name='clients'),
]
