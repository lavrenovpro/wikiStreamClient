import os
import json
import sys

from kafka import KafkaProducer
from sseclient import SSEClient as EventSource


def run_client():
    bootstrap_server = get_env_parameter_or_panic('BOOTSTRAP_SERVER')
    wiki_url = get_env_parameter_or_panic('WIKI_URL')
    topic_name = get_env_parameter_or_panic('TOPIC_NAME')

    producer = KafkaProducer(bootstrap_servers=[bootstrap_server],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    for event in EventSource(wiki_url):
        if event.event == 'message':
            data = event.data
            producer.send(topic_name, data)


def get_env_parameter_or_panic(parameter_name):
    try:
        return os.environ[parameter_name].lower()
    except KeyError:
        sys.exit(parameter_name + ' is not specified')


if __name__ == '__main__':
    run_client()
