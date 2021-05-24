import pika, json
QUEUE_NAME = 'Job_id_queue'
EXCHANGE_NAME = 'JOB SCHEDULER EXCHANGE'

def random_data(value):
    return  {"job_id":value,
               "action":'update',
               "value":value*10+value
               }

# establish synchronous connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', 
                              pika.PlainCredentials('user', 'password')))
channel = connection.channel() # create channel on next available number
print(channel)
channel.queue_declare(queue=QUEUE_NAME) # declare which queue youll be using. Will create if needed
for i in range(10):
    channel.basic_publish(exchange=EXCHANGE_NAME, 
                      routing_key=QUEUE_NAME, body=json.dumps(random_data(i)))

connection.close()