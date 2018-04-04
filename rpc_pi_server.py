#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('the_user', 'the_pass')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.43.50',5672,'/',credentials))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def on_request(ch, method, props, body):
    print(body)
    distMat= str(body).split(",")[1:-1]
    distMat=list(map(int, distMat))
    print(distMat)
    action="1" #get action here
    response = action

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
