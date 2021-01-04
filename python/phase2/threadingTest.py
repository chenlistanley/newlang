import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId=threadId
        self.name=name
        self.counter=counter
    def run(self):
        print("start: " + self.name)
        print_time(3, self.counter)
        print("exit: " + self.name)
def print_time(delay, counter):
    while counter:
        counter-=1
        time.sleep(delay)
        print("%s: %s: %s" %(threading.currentThread().name, time.ctime(), counter))

thread1=myThread(1, "Thread-1", 4)
thread2=myThread(2, "Thread-2", 6)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("exit main thread")