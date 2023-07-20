from decouple import config
import pika

URL = config("URL")
params = pika.URLParameters(url=URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print("-"*50)
    print('Received in admin/consumer')
    print(body)
    print("-"*50)


channel.basic_consume(
    queue='admin', on_message_callback=callback)
channel.start_consuming()
channel.close()
