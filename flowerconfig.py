import os

AMQP_ADMIN_USERNAME = os.getenv('AMQP_ADMIN_USERNAME', 'user')
AMQP_ADMIN_PASSWORD = os.getenv('AMQP_ADMIN_PASSWORD', 'password')
AMQP_ADMIN_HOST = os.getenv('AMQP_ADMIN_HOST', 'localhost')
AMQP_ADMIN_PORT = int(os.getenv('AMQP_ADMIN_PORT', '15672'))

DEFAULT_BROKER_API = 'http://%s:%s@%s:%d/api/' \
                     % (
                         AMQP_ADMIN_USERNAME,
                         AMQP_ADMIN_PASSWORD,
                         AMQP_ADMIN_HOST,
                         AMQP_ADMIN_PORT
                     )

USERNAME = os.getenv('FLOWER_USERNAME', 'root')
PASSWORD = os.getenv('FLOWER_PASSWORD', 'changeit')

port = int(os.getenv('FLOWER_PORT', '5555'))
broker_api = os.getenv('FLOWER_BROKER_API', DEFAULT_BROKER_API)
max_tasks = int(os.getenv('FLOWER_MAX_TASKS', '3600'))
basic_auth = [os.getenv('FLOWER_BASIC_AUTH', '%s:%s'
                        % (USERNAME, PASSWORD))]
