import os

import requests
from kafka import KafkaProducer


def run_client():
    bootstrap_server = get_env_parameter('BOOTSTRAP_SERVER', 'latitude:9092')
    wiki_url = get_env_parameter('WIKI_URL', 'https://stream.wikimedia.org/v2/stream/revision-create')
    topic_name = get_env_parameter('TOPIC_NAME', 'wiki_revision_create')

    producer = KafkaProducer(bootstrap_servers=[bootstrap_server])

    r = requests.get(wiki_url, stream=True)
    for line in r.iter_lines():
        producer.send(topic_name, line)


def get_env_parameter(parameter_name, default_value):
    try:
        return os.environ[parameter_name].lower
    except KeyError:
        return default_value


if __name__ == '__main__':
    run_client()
