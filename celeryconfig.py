import os

AMQP_USERNAME = os.getenv('AMQP_USERNAME', 'user')
AMQP_PASSWORD = os.getenv('AMQP_PASSWORD', 'password')
AMQP_HOST = os.getenv('AMQP_HOST', 'localhost')
AMQP_PORT = int(os.getenv('AMQP_PORT', '5672'))

DEFAULT_BROKER_URL = [
    'amqp://{}:{}@{}:{}'.format(
        AMQP_USERNAME, AMQP_PASSWORD, host.strip(), AMQP_PORT
    ) for host in AMQP_HOST.split(',') if host.strip()
]

BROKER_URL = os.getenv('BROKER_URL', DEFAULT_BROKER_URL)
