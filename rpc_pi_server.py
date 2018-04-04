#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('the_user', 'the_pass')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.43.50',5672,'/',credentials))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def getAction(state):   
   action = (np.argmax(model.predict(state, batch_size=1)))
   return action


def on_request(ch, method, props, body):
    print(body)
    distMat= str(body).split(",")[1:-1]
    distMat=list(map(int, distMat))
    print(distMat)

    saved_model = 'saved-models/128-128-64-50000-25000.h5'
    model = neural_net(NUM_SENSORS=3, [128, 128], saved_model)

    action=getAction(distMat) #get action here
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
