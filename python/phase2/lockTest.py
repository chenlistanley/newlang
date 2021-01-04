import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.name=name
        self.counter=counter
    def run(self):
        print("start: " + self.name)
        threadLock.acquire()
        print_time(self.counter)
        threadLock.release()
        print("exit: " + self.name)
def print_time(counter):
    while counter:
        counter-=1
        time.sleep(3)
        print("%s: %s: %s" %(threading.currentThread().name, time.ctime(), counter))
threadLock=threading.Lock()

t1=myThread("Thread_1", 4)
t2=myThread("Thread_2", 6)
t1.start()
t2.start()
t1.join()
t2.join()
print("exit main thread")