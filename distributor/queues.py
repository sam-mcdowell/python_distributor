from abc import ABCMeta, abstractmethod
from kafka.client import KafkaClient
from kafka.consumer import KafkaConsumer
from kafka.producer import SimpleProducer
from multiprocessing import Pool, Process
import json

class DistributerQueue(object):
    metaclass__ = ABCMeta

    @abstractmethod
    def enqueue(self, task, *args, **kwargs):
        pass

    @abstractmethod
    def add_topic(self, topic):
        pass


class LocalQueue(DistributerQueue):

    def __init__(self, concurrency):
        self.pool = Pool(processes=concurrency)

    def enqueue(self, task, *args, **kwargs):
        self.pool.apply_async(task, (args, kwargs))


class KafkaQueue(DistributerQueue):

    CONSUMER_GROUP = "distributed_{}"

    def __init__(
        self,
        concurrency,
        kafka_hosts,
        topic=None,
        consumer_group=None
    ):
        self.concurrency = concurrency
        if topic:
            if consumer_group is None:
                consumer_group = CONSUMER_GROUP.format(topic)
            self.consumer = KafkaConsumer(
                topic,
                bootstrap_servers=kafka_hosts,
                group_id=consumer_group
            )
        else:
            self.producer = SimpleProducer(KafkaClient(hosts=kafka_hosts))

    def enqueue(self, task, *args, **kwargs):
        topic = task.__name__
        self.producer.send_messages(
            topic,
            json.dumps({"args": args, "kwargs": kwargs})
        )

    class Worker(Process)
    def dequeue(self):
        for message in self.consumer:
            arg_dict = json.loads(message)
            self.