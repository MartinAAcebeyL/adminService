from .factory import create_client
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--cant', type=int, default=10, help='Indicates the number of clients to be created')

    def handle(self, *args, **options):
        cant = options['cant']
        create_client(cant)
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {cant} clients'))
