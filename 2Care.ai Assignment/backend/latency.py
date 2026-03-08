import time
from contextlib import contextmanager

@contextmanager
def measure_latency(name):

    start = time.time()

    yield

    end = time.time()

    latency = (end - start) * 1000

    print(f"{name} latency: {latency:.2f} ms")