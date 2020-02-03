#!/usr/bin/env python

import pika

#Conexao


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port="5672"))
channel = connection.channel()

print "connection created"


queue = "hello"

q = channel.queue_declare(queue, passive=False, durable=False, exclusive=False, auto_delete=False, arguments=None, callback=None)

contador = q.method.message_count

print 'A fila %s possui: %s  mensagens'%(queue , contador)
