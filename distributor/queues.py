from abc import ABCMeta, abstractmethod
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from multiprocessing import Pool

class DistributerQueue(object):
    metaclass__ = ABCMeta

    @abstractmethod
    def enqueue(self, task, *args, **kwargs):
    	pass


class LocalQueue(DistributerQueue):

	def __init__(self, concurrency):
		self.pool = Pool(processes=4):

	def enqueue(self, task, *args, **kwargs):
		self.pool.apply_async(task, (args, kwargs))

class KafkaQueue(DistributerQueue):

	def __init__(self, kafka_hosts):
		self.client = KafkaClient(hosts=kafka_hosts)
        self.topics = {}

	def enqueue(self, task, *args, **kwargs):
		topic = task.__name__
		self.client. 

	def add_topic(self, topic):
		producer = 