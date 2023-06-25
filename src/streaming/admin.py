from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import UnknownTopicOrPartitionError, TopicAlreadyExistsError

from streaming.config import KAFKA_SERVER, KAFKA_NUM_PARTITIONS, KAFKA_REPLICATION_FACTOR


def create_topic(topic: str):
    admin_client = KafkaAdminClient(bootstrap_servers=[KAFKA_SERVER])
    try:
        admin_client.create_topics([
            NewTopic(
                name=topic,
                num_partitions=KAFKA_NUM_PARTITIONS,
                replication_factor=KAFKA_REPLICATION_FACTOR
            )
        ])
    except TopicAlreadyExistsError:
        pass


def delete_topic(topic: str):
    admin_client = KafkaAdminClient(bootstrap_servers=[KAFKA_SERVER])
    try:
        admin_client.delete_topics(topic)
    except UnknownTopicOrPartitionError:
        pass
