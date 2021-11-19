import pika, os, django
from pika import connection
from pika import channel
import json 

'''
setup Django here so we can call models from outside the project
'''
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()

from products.models import Product


params = pika.URLParameters('amqps://drtzmlak:mt7OkZ_SML55NTPGgMqJ_tq8KQ3G_wG-@woodpecker.rmq.cloudamqp.com/drtzmlak')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    if properties.content_type == 'product-liked':
        print("Recieve in admin")
        id = json.loads(body)
        print("Liked product id:", id)
        product = Product.objects.get(id=id)
        print ("Producte:", product)
        product.likes += 1
        product.save()
        print ("Product likes increased")


channel.basic_consume(queue='admin', on_message_callback=callback)
print ("Started consuming -----")
channel.start_consuming()
channel.close()