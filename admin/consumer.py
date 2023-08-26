from decouple import config
import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from apps.products.models import Product

URL = config("URL")
params = pika.URLParameters(url=URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in Admin Consumer')
    try:
        id = json.loads(body)
        print(id)
        product = Product.objects.get(id=id)
        product.likes = product.likes + 1
        product.save()
    except Exception as e:
        print('Product does not exist!')


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)
print('Started Admin Consuming')
channel.start_consuming()
# channel.close()
