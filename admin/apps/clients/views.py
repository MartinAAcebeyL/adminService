from rest_framework import views
from rest_framework.response import Response
from .models import Client
import random


class ClientApiView(views.APIView):
    def get(self, _):
        client = Client.objects.all()
        client = random.choice(client)
        return Response({
            'id': client.id,
            'name': client.name,
        })
