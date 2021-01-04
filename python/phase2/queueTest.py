import queue
import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.name=name
        self.counter=counter
    def run(self):
        print("Start: " + self.name)
        print_time(self.counter)
        print("Exit: " + self.name)
def print_time(counter):
    while counter:
        counter-=1
        data=getData()
        print("%s: %s: %s: %s" %(threading.currentThread().name, time.ctime(), counter, data))
        time.sleep(3)
def getData():
    data=''
    threadLock.acquire()
    if not workQueue.empty():
        data=workQueue.get()
    threadLock.release()
    return data

threadLock=threading.Lock()
workQueue=queue.Queue(10)
t1=myThread("Thread-1", 4)
t2=myThread("Thread-2", 4)
t1.start()
t2.start()
threadLock.acquire()
values=['abc','123','hello','bill']
for v in values:
    workQueue.put(v)
threadLock.release()
t1.join()
t2.join()
print("exit main thread")


