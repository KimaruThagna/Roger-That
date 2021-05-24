import pika

QUEUE_NAME = 'Job_id_queue'

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', 
                              pika.PlainCredentials("user", "password")))

channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME)

def callback(ch, method, properties, body): # invoked when consumer receives message from QUEUE_NAME
    print(f'[x] Received task {body}') 

channel.basic_consume(callback, queue=QUEUE_NAME, auto_ack=True)# immediately acknowledge to allow de-queueing
# for fault tolerance, you can do no_ack=True and do the ack manually when your job processing is successful

print(' [*] Ready to receive processing tasks')

channel.start_consuming()