# What is this
Small client just to get a data stream for exercises

# Building and running
Build container:
```shell
git clone https://github.com/lavrenovpro/wiki_stream_client.git
cd wiki_stream_client
docker build -t wiki_stream_client .
```
Update parameters for your environment:
```shell
vi config/.env.dev
```
```yaml
BOOTSTRAP_SERVER=your_kafka_broker_hostname:9092
WIKI_URL=https://stream.wikimedia.org/v2/stream/revision-create
TOPIC_NAME=wiki_revision_create_topic_name
```
Run:
```shell
docker-compose up -d
```

