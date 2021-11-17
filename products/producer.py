import pika
from pika import connection
from pika import channel

params = pika.URLParameters('amqps://drtzmlak:mt7OkZ_SML55NTPGgMqJ_tq8KQ3G_wG-@woodpecker.rmq.cloudamqp.com/drtzmlak')

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')