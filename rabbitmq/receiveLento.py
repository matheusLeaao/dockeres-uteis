#!/user/bin/env python

import pika;

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
print " connection created"

channel = connection.channel()

channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(randrange(0, 5))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume('hello',
                      callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
