from apps.clients.models import Client
from faker import Faker

faker = Faker()


def create_client(cant: int = 10):
    def create_single_client():
        return Client.objects.create(
            name=faker.name(),
            email=faker.email(),
            phone=faker.phone_number()[:14]
        )
    if cant == 1:
        return create_single_client()

    for _ in range(10):
        create_single_client().save()
