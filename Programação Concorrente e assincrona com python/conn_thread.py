import imp
import queue
from time import sleep
from threading import Thread
from queue import Queue

def gerador(queue):
    for i in range(1, 11):
        print(f"gerador {i}")
        sleep(2)
        queue.put(i)

def consumidor(queue):
    while queue.qsize() > 0:
        valor =queue.get()
        print(f"dado {valor * 2}")
        sleep(1)
        queue.task_done()

if __name__ == "__main__":
    queue = Queue()
    th1 = Thread(target=gerador, args=(queue,))
    th2 = Thread(target=consumidor, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()