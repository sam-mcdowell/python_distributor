"""
Python task distributor
"""
from distributable import distributable

SUPPORTED_MODES = [
	"development",
	"supervised_workers",
	"server",
	"worker"
	]

class Distributor(object):
    """
    Distributor for tasks.
    """
    def __init__(
        self,
        mode="development",
        queue=None,
        concurrency=1,
    ):

        self.mode = mode
        self.queue = self._configure_queue()
        self.concurrency = concurrency

    def distribute(self, queue=self.queue):
    	if isinstance(self.queue, KafkaQueue):
    		self.queue.add_topic(f.__name__)
        def decorator(f):
            handler = TaskHandler(f, topic, self, max_retries)
            self._register(task_type, handler)

            return handler

        return decorator

     def _configure_queue(self):
     	if self.queue:
     		return self.qeuue:
     	if mode.equals("development"):
     		return 