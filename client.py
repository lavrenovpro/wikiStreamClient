import os
import json
from kafka import KafkaProducer
from sseclient import SSEClient as EventSource


def run_client():
    bootstrap_server = get_env_parameter('BOOTSTRAP_SERVER', 'latitude:9092')
    wiki_url = get_env_parameter('WIKI_URL', 'https://stream.wikimedia.org/v2/stream/revision-create')
    topic_name = get_env_parameter('TOPIC_NAME', 'wiki_revision_create')

    producer = KafkaProducer(bootstrap_servers=[bootstrap_server],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    for event in EventSource(wiki_url):
        if event.event == 'message':
            data = event.data
            producer.send(topic_name, data)


def get_env_parameter(parameter_name, default_value):
    try:
        return os.environ[parameter_name].lower
    except KeyError:
        return default_value


if __name__ == '__main__':
    run_client()
