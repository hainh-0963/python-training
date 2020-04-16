import time
def timer(f):
    return time.time()

@timer
def add(x, y):
    return print(x + y)