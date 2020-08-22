# celery-flower-docker

Docker container for monitoring celery

## Running with docker

In order to run flower using  docker, run command: 

```
sudo docker run -it --rm --name flower -p 5555:5555 jcpaiva/celery-flower
```

## Access Flower

To access flower go to url: [http://localhost:5555](http://172.17.42.1:5555).
The default credentials for the flower instance is username:root  password:changeit.
(It is highly recommended to change the default credentials. See run configuration.)

If your are using dynamic port mapping using (-P), inspect the container to determine the mapped
port for 5555.

## Run Configuration (Environment Variables)

| Env Variable        | Description                                   | Default Value (Docker) |
| ------------------- | --------------------------------------------- | ---------------------- |
| FLOWER_PORT         | Port to be used by flower                     | 5555                   |
| FLOWER_MAX_TASKS    | Max tasks to be stored in memory.             | 3600                   |
| FLOWER_USERNAME     | Flower username                               | root                   |
| FLOWER_PASSWORD     | Flower password                               | changeit               |
| FLOWER_BASIC_AUTH   | Authentication for flower (username:password) | root:changeit          |
| AMQP_USERNAME       | RabbitMQ broker username                      | user                   |
| AMQP_PASSWORD       | RabbitMQ broker password                      | password               |
| AMQP_HOST           | RabbitMQ host                                 | localhost              |
| AMQP_PORT           | RabbitMQ port                                 | 5672                   |
| AMQP_ADMIN_USERNAME | RabbitMQ admin username                       | user                   |
| AMQP_ADMIN_PASSWORD | RabbitMQ admin password                       | password               |
| AMQP_ADMIN_HOST     | RabbitMQ admin host                           | localhost              |
| AMQP_ADMIN_PORT     | RabbitMQ admin port                           | 15672                  |
