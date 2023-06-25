import os

KAFKA_SERVER = os.environ.get('KAFKA_SERVER', 'localhost:9092')
KAFKA_NUM_PARTITIONS = int(os.environ.get('KAFKA_NUM_PARTITIONS', '4'))
KAFKA_REPLICATION_FACTOR = int(os.environ.get('KAFKA_REPLICATION_FACTOR', '1'))
