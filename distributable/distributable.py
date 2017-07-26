"""
Decorator for tasks that can be delegated by a distributor
"""
import functools


class Distributable(object):
    def __init__(self, mode, queue):
        self.mode = mode
        self.queue = queue

    def __call__(self, func):
        self.queue.add_topic(func.__name__)
        if self.mode == "development":
            return self.development_decorator(func)
        if self.mode == "supervised_workers":
            return self.supervised_decorator(func)
        if self.mode == "server":
            return self.server_decorator(func)
        if self.mode == "worker":
            return self.worker_decorator(func)

    def development_decorator(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(self.mode)
            return func(*args, **kwargs)
        return wrapper

    def supervised_decorator(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(self.mode)
            return func(*args, **kwargs)
        return wrapper

    def server_decorator(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(self.mode)
            return func(*args, **kwargs)
        return wrapper

    def worker_decorator(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(self.mode)
            return func(*args, **kwargs)
        return wrapper


@Distributable(mode="local")
def func(x, y):
    return x, y

if __name__ == '__main__':
    print func(1, 2)
