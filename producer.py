import pika, json
QUEUE_NAME = 'Job_id_queue'
EXCHANGE_NAME = 'JOB SCHEDULER EXCHANGE'
sample_data = {"job_id":1,
               "action":'update',
               "value":432
               }

# establish synchronous connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', 
                              pika.PlainCredentials('user', 'password')))
channel = connection.channel() # create channel on next available number
print(channel)
channel.queue_declare(queue=QUEUE_NAME) # declare which queue youll be using. Will create if needed
channel.basic_publish(exchange=EXCHANGE_NAME, 
                      routing_key=QUEUE_NAME, body=json.dumps(sample_data))

connection.close()