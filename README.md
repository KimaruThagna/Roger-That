# Roger-That
Using RabbitMQ to demonstrate message queues in Python. The environment will be managed by docker

# Spin up RabbitMQ
Use the docker command below to spin rabbitMq and the management console availabl at `localhost:15672`


```
docker run  --hostname my-rabbit -p 15672:15672 -p 5672:5672 --name rabbit-server -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management
```

# Run the components
To run the producer `python3 producer.py`

To run the consumer `python3 consumer.py`